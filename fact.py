X=input()
def factorial(X):
    if X==1:
        return 1
    else:
        return (X*factorial(X-1))

print("the factorial of", X , "is" ,factorial(X))
    
