    
def fizzbuzz(num):
    a = num%3
    b = num%5

    if a == 0 and b == 0:
        print("fizzbuzz")
    elif a == 0 and b != 0:
        print("fizz")
    elif b == 0 and a != 0:
        print("buzz")
    else:
        print(num)


fizzbuzz(1)
fizzbuzz(2)
fizzbuzz(3)
fizzbuzz(3)
fizzbuzz(5)
fizzbuzz(6)
fizzbuzz(7)
fizzbuzz(8)
fizzbuzz(9)
fizzbuzz(10)
fizzbuzz(11)
fizzbuzz(12)
fizzbuzz(13)
fizzbuzz(14)
fizzbuzz(15)
