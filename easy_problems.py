import math

# find the sum of all multiples of 3 or 5 below some max
# max = 1000
def problem1(max):
    sum = 0

    for i in range(0,max):
        if i%3==0 or i%5==0:
            sum += i

    print sum

# find the sum of the even numbered fibonacci terms that are less than some max
# max = 4000000
def problem2(max):
    sum = 0
    list = [0, 1] # init our fibonacci list

    while True:
        # see if the last element in our list is even
        if list[-1]%2==0:
            sum += list[-1]

        # add the next element to the list
        # unless it goes over our max (then just stop)
        if (list[-1]+list[-2])<max:
            list.append( list[-1] + list[-2] )
        else:
            break

    print sum

# find the largest prime factor of a number
# number = 600851475143
def problem3(number):
    primes = [2,3]

    # init list of prime factors
    if number%2==0 and number%3==0:
        factors = [2,3]
    elif number%2==0:
        factors = [2]
    elif number%3==0:
        factors = [3]
    else:
        factors = []

    # find primes, starting at 3
    i = 5
    
    while i<int(math.floor(number/2)):
        isPrime = True
        j = 0

        if math.sqrt(i)-int(math.sqrt(i))==0:
            isPrime = False
        else:
            while isPrime == True and j < len(primes):
                if i%primes[j]==0:
                    isPrime = False
                j += 1

        if isPrime == True:
            primes.append(i)

            if number%i==0:
                factors.append(i)

        i += 2

    print factors

problem3(600851475143)
