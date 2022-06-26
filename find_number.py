import math


def find(a):
    r = []
    h =[]
    for i in a.split(','):
        r.append(i)

    for i in r:
        for j in i.split():
            if(j.isdigit()):
                h.append(j)
        
    
    ans = 0

    for i in reversed(range(2,len(h))):
        
        t = int(h[i])
        k = countDigit(ans)
        print(k)
        ans = t* (pow(10,k)) + ans

     
    return ans

def countDigit(n):
    if(n==0):
        return int(0)
    return math.floor(math.log10(n)+1)


