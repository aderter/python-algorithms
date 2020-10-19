def binaryModularExponentiation(x,n,M):
    """
    finds the value of (x^n)%M
    Time complexity: O(log N)
    Space complexity: O(1)
    """
    result=1
    while(n>0):
        if(n&1):
            result=(result * x)%M
        x=(x*x)%M
        n>>=1
    return result  
    
print(binaryModularExponentiation(2,5,20))
