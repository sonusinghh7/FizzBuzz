

'''Develop a program that prints all is from 1 to 100, but for multiples of 3, print "Fizz," and
 for multiples of 5, print "Buzz.'''


i=0
while i<100:
    i=i+1
    if i%3==0:
        print(i,"Fizz")
    elif i%5==0:
        print(i,"Buzz")
    else:
        print(i)
    
    
# for i in range(1, 101):
#     if i % 3 == 0:
#         print(i,"Fizz")
#     elif i % 5 == 0:
#         print(i,"Buzz")
#     else:
#         print(i)
