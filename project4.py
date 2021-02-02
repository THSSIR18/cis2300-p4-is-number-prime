def isNumberPrime(number):
    countDivisor = 0
    
    for i in range(1, number+1):
        if number % i == 0:
            countDivisor += 1
            
    if countDivisor == 2:
        return True
    else: 
        return False
            
a = 22022
b = a + 5000
counter = 0

for num in range(a,b+1):
    if isNumberPrime(num):
        counter+=1
print(counter)
