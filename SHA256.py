import math

def bintoint(number):
    number = str(number)
    length = len(number)
    sum = 0
    for i in range(length):
        sum += int(number[length-i-1])*(2**(i-1))
    sum = str(sum)
    return sum

def float_bin(number, places = 3):     
    whole, dec = str(number).split(".")     
    whole = int(whole) 
    dec = int (dec)   
    res = bin(whole).lstrip("0b") + "." 
    for i in range(places):      
        whole, dec = str((decimal_converter(dec)) * 2).split(".")   
        i += 1
        i -= 1  
        dec = int(dec)     
        res += whole 
    return res 
  
 
def decimal_converter(num):  
    while num > 1: 
        num /= 10
    return num 

def primenumber(number, searchrange):
    upto = 0
    isPrime = True
    for num in range(searchrange):
        for i in range(2,int(math.sqrt(searchrange))):
            if i < num:
                if num % i == 0:
                    isPrime = False
                    break
        if isPrime:
            #print(num)
            upto += 1
        isPrime = True
        if upto == number + 2:
            #print(num)
            return num

def firstprimes(number, searchrange):
    for i in range(number):
        primenumber(i + 1, searchrange)

def dec_only(number):
    integer, decimal = str(number).split(".")
    integer = 0
    decimal = int(decimal) + integer
    return decimal

def rightrotate(num,howfar):
    number = str(num)
    firstpart = number[0:len(number) - howfar]
    secondpart = number[(len(number) - howfar):len(number)]
    rotated = secondpart + firstpart
    return rotated

def rightshift(num,howfar):
    number = str(num)
    secondpart = number[howfar:]
    for i in range(howfar):
        secondpart = "0" + secondpart
        i += 1
        i -= 1
    return secondpart

def binand(num1,num2):
    num1 = str(num1)
    num2 = str(num2)
    while len(num1)!=len(num2):
        if len(num2) < len(num1):
            num2 = "0" + num2
        elif len(num1) < len(num2):
            num1 = "0" + num1
    output = ""
    for i in range(len(num1)):
        if num1[i]==num2[i]=="1":
            output = output + "1"
        else:
            output = output + "0"
    return output

def binnot(num):
    num = str(num)
    output = ""
    for i in range(len(num)):
        if num[i]=="0":
            output = output + "1"
        else:
            output = output + "0"
    return output

def binxor(a,b):
    a = str(a)
    b = str(b)
    while len(a)!=len(b):
        if len(b) < len(a):
            b = "0" + b
        elif len(a) < len(b):
            a = "0" + a
    c = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            c = c + "0"
        else:
            c = c + "1"
    return c


def sha256(text):
    text = str(text)
    bintext = ""
    hashvalues = []
    roundconstants = []
    bintextchunks = []
    thirtytwobitwords = []
    for i in range(len(text)):
        bintext = bintext + bin(ord(text[i]))[2:]
    length = bin(len(bintext))[2:]
    bintext = bintext + "1"
    while len(bintext) % 512 != 448:
        bintext = bintext + "0"
    while len(length) < 64:
        length = "0" + length
    
    bintext = bintext + length
    #print(bintext)
    #print(len(bintext))

    for i in range(8):
        hashvalues.append(dec_only(float_bin(math.sqrt(primenumber(i+1,20)),32)))
    
    for i in range(len(hashvalues)):
        hashvalues[i] = str(hashvalues[i])
        while len(hashvalues[i]) < 32:
            hashvalues[i] = "0" + hashvalues[i]
    
    for i in range(len(hashvalues)):
        hashvalues[i] = bin(int(hashvalues[i]))[2:]
    
    for i in range(64):
        roundconstants.append(dec_only(float_bin(primenumber(i+1,500)**(1./3),32)))
    for i in range(len(roundconstants)):
        roundconstants[i] = bin(int(roundconstants[i]))
    #print("Roundconstants: ")
    #print(roundconstants)
    for num in range(int(len(bintext) / 512)):
        bintextchunks.append(bintext[num*512:((num+1) * 512)])
    #print(bintextchunks)
    for k in range(len(bintextchunks)):
        for i in range(1,int(len(bintextchunks[k]) / 32) + 1):
            thirtytwobitwords.append(str(bintextchunks[k])[(i - 1) * 32:i * 32])
        #print(thirtytwobitwords)
        for i in range(48):
            thirtytwobitwords.append('00000000000000000000000000000000')
        #print(thirtytwobitwords)
        #print(len(thirtytwobitwords))
        for i in range(16+64*k,64+64*k):
            a = hashvalues[0]
            b = hashvalues[1]
            c = hashvalues[2]
            d = hashvalues[3]
            e = hashvalues[4]
            f = hashvalues[5]
            g = hashvalues[6]
            h = hashvalues[7]
            s0 = binxor(binxor(rightrotate(thirtytwobitwords[i-15],7),rightrotate(thirtytwobitwords[i-15],18)),rightshift(thirtytwobitwords[i-15],3))
            s1 = binxor(binxor(rightrotate(thirtytwobitwords[i-2],17),rightrotate(thirtytwobitwords[i-2],19)),rightshift(thirtytwobitwords[i-2],10))
            thirtytwobitwords[i] = bin((int(thirtytwobitwords[i-16],2) + int(s0,2) + int(thirtytwobitwords[i-7],2) + int(s1,2))%(2**32))[2:]
        for i in range(64):
            thirtytwobitwords[i + k*64] = bin(int(thirtytwobitwords[i + k*64]))
        for i in range(64):
            S1 = bin(int(binxor(binxor(rightrotate(e,6),rightrotate(e,11)),rightrotate(e,25))))
            ch = bin(int(binxor(binand(e,f),binand(binnot(e),g))))
            temp1 = (int(h,base=2) + int(S1,base=2) + int(ch,base=2) + int(roundconstants[i],base=2) + int(thirtytwobitwords[i+k*64],base=2))%(2**32)
            S0 = bin(int(binxor(binxor(rightrotate(a,2),rightrotate(a,13)),rightrotate(a,22))))[2:]
            maj = bin(int(binxor(binxor(binand(a,b),binand(a,c)),binand(b,c))))[2:]
            temp2 = bin(int(S0 + maj)%(2**32))[2:]
            h = bin(int(g)%(2**32))[2:]
            g = bin(int(f)%(2**32))[2:]
            e = bin((int(d) + int(temp1))%(2**32))[2:]
            f = bin(int(d)%(2**32))[2:]
            d = bin(int(c)%(2**32))[2:]
            c = bin(int(b)%(2**32))[2:]
            b = bin(int(a)%(2**32))[2:]
            a = bin((int(temp1) + int(temp2))%(2**32))[2:]
        hashvalues[0] = bin((int(hashvalues[0]) + int(a))%(2**32))[2:]
        hashvalues[1] = bin((int(hashvalues[1]) + int(b))%(2**32))[2:]
        hashvalues[2] = bin((int(hashvalues[2]) + int(c))%(2**32))[2:]
        hashvalues[3] = bin((int(hashvalues[3]) + int(d))%(2**32))[2:]
        hashvalues[4] = bin((int(hashvalues[4]) + int(e))%(2**32))[2:]
        hashvalues[5] = bin((int(hashvalues[5]) + int(f))%(2**32))[2:]
        hashvalues[6] = bin((int(hashvalues[6]) + int(g))%(2**32))[2:]
        hashvalues[7] = bin((int(hashvalues[7]) + int(h))%(2**32))[2:]
    for i in range(8):
        hashvalues[i] = str(hashvalues[i])
        while len(hashvalues[i])<32:
            hashvalues[i] = "0" + hashvalues[i]
    
    endhash = ""
    for i in range(8):
        endhash += hashvalues[i]
    endhash = int(endhash,base=2)
    return endhash


        
            
    
    #print(thirtytwobitwords)

 

#primenumber(100, 10000)
#print(binnot(1101010001011))