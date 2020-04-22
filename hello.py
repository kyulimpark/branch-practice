for i in range(1, 100+1):
    if i%3==0 or i%5==0:
        print("fizz"*(i%3==0)+"buzz"*(i%5==0))
    else:
        print(i)
#for i in range(1, 101):
#    if 1%10==0:
#       print("fizzbuzz")
#    elif i%3==0:
#        print("fizz")
#    elif i%5==0:
#        print("buzz")
#    else:
#        print(i)
