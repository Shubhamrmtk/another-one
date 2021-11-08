# a=int(input("Enter any no"))
# if a==1 :
#     print("composit number")
# elif a==2 :
#     print("no is prime no")
# else :
#     i=1
#     c=1
#     while i<a/2 :
#         if a%i==0 :
#             c=c+1
#             i=i+1
#     if c>1 :
#         print("no is not prime")
#     else:
#         print("no is prime")
# a=int(input("enter any no"))
# if a==2 :
#     print("no is prime")
# else :
#     c=0
    
#     i=2
#     while i<a :
#         if a%i==0 :
#             print("no is not prime ")
#             break

#         else :
#             print("No is not primr")
#             break
#         i=i+1
#--------------------------------------------------------------------------------------------------------------------------------------
# def prime (a):
#     if a==0 :
#         return 1
#     # print(a)
#     prime(a-1)
#     print(a)
# # print(prime(5))
# prime(5)
#------------------------------------------------------------------------------------------------------------------------------------------
def checkprime(num) :
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                break
            else:
                print(num,"is a prime number")
                break
                
    else:
      print(num,"is not a prime number")
b=int(input("enter no"))
i=1
while i<=b :
    checkprime(i)
    i=i+1
            

    