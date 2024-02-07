#fizz buzz game
print("hey welcome to the fizz buzz game")
a=int(input("enter a number: "))
for i in range(1,a):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%5==0:
        print("buzz")
    elif i%3==0 :
        print("fizz ")
    else:
        print(i)