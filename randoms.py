import random

num = random.randint(1, 100)

get = int(input('guess the number? :'))

if num != get:
    while num != get:
        if num > get:
            print("the number is bigger")
            get = int(input('Guess Again: '))
        else:
            print("the number is smaller")
            get = int(input('Guess Again: '))

    print("You got it")
