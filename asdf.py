##os.uname shows running on
##('Linux', 'DESKTOP-NLTR4V5', '4.4.0-17134-Microsoft', '#706-Microsoft Mon Apr 01 18:13:00 PST 2019', 'x86_64')
##with python version
##'2.7.15rc1 (default, Nov 12 2018, 14:31:15) \n[GCC 7.3.0]'
def sqprimes(n=1):
    data = []
    index = 2
    while True:
        isPrime = True
        for i in data:
            if index%i==0:
                isPrime = False
                break
        if isPrime:
            data.append(index)
            if index**2>n:
                yield index**2
        index+=1

def primes(n=1):
    data = []
    index = 2
    while True:
        isPrime = True
        for i in data:
            if index%i==0:
                isPrime = False
                break
        if isPrime:
            data.append(index)
            if index > n:
                yield index
        index+=1

def spsp(n):
    pr = primes()
    primelist = [next(pr)]
    while primelist[-1]**2<n:
        primelist.append(next(pr))
    while True:
        for i in primelist[:-1]:
            yield i+primelist[-1]**2
        primelist.append(next(pr))

##****************************************
##The code generating the primes 
##****************************************
##>>> f=sqprimes(1132484290)
##>>> for i in range(20):
##...     print(next(f))
##... 
##****************************************
##The results
##****************************************
##1134275041
##1135892209
##1136566369
##1137105841
##1138320121
##1138995001
##1139130001
##1139535049
##1140210289
##1140345361
##1140615529
##1141831681
##1142237209
##1143048481
##1143183721
##1144265929
##1144401241
##1145890201
##1146296449
##1146702769
##>>> 
