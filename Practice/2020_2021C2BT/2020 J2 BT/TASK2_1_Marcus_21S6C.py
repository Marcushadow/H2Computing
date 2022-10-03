def isPrime(n):
    if n == 1:
        return False
        
    else:
        prime = True
        for i in range(n//2, 1, -1):
            if n%i == 0:
                prime = False
        return prime
        
        
print("All prime numbers")
for i in range(1, 101):
    if isPrime(i):
        print(i)
        
print("\nSieve of Eratho")
        
def SieveOfErathostenes(n):
    store = []
    for i in range(0,n+1):
        store.append(i)
    store[0] = 0
    store[1] = 0
           
    p = 2
    
    while(p <= n):
        probe = p + p
        while(probe <= n):
            store[probe] = 0
            probe += p
        
        p += 1
        while( p <= n and store[p] == 0):
            p += 1
            
    for item in store:
        if item != 0:
            print(item)
        
SieveOfErathostenes(30)
        