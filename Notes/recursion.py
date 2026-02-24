#ES 
for num in range (1,11):
    if num %2 ==0:
        print(num)

even = []


sume =5
num = 1

#for x in range(1,num +1):
    #sum *= x
#print(f"loop: {sum}")

def factorial(n):
    if n ==1: return 1
    return n * factorial(n-1)

print(f"recursion: {factorial(num)}")


fib = [1,1]

for i in range(1,11):
    fib.append(fib[i-1] + fib[1])
print(fib)


numbers = []
def fibonacci(n):
    #numbers.append(n)
    if n ==2:
        return 1
    elif n==1:
        return 0
    else:
        return n + fibonacci(n-1) + fibonacci(n-2)
fibonacci(10)
print(f"Recursion: {fibonacci(11)}")