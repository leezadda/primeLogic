#Program for prime numbers

def isPrime(number): #Tells you if the number is prime or not
    if number == 1:
        return False
    i = 2
    while i*i <= number:
        if number % i == 0: 
            return False
        i = i + 1
    return True

def firstNPrimes(numberOfPrimes): #Ask for n amount of prime numbers and receive them as a list
    prime = 0
    newList = []
    infinity = 0
    while infinity == 0:
        prime += 1
        if isPrime(prime) == True:
            newList.append(prime)
            if len(newList) == numberOfPrimes:
                break
    return newList

def primesInRange(x, y): #Give a range of prime numbers and receive them as a list
    newList = []
    for i in range(x, y+1):
        if isPrime(i) == True:
            newList.append(i)
    return newList

option = int(input("")) #Input from user
if option == 1:
    n = int(input(""))
    result = firstNPrimes(n)
    
else:
    minV = int(input(""))
    maxV = int(input(""))
    result = primesInRange(minV, maxV)
print(result)