def divisible(m, n):
    if m % n == 0:
        print("True")
        return True
    else:
        print("False")
        return False


def fb(n):
    if n % 3 == 0 and n % 5 != 0:
        print("fiz")
    if n % 3  != 0 and n % 5 == 0:
        print("buzz")
    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")
    if n % 3 != 0 and n % 5 != 0:
        print("shucks")

def sleep_in(weekday,vacation):
    if not weekday or vacation:
        return True
    else:
        return False

def monkey_trouble(a_smile,b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False

def sum_double(a,b):
    if a == b:
        return ((a + b) *2)
    return a + b

def diff21(n):
    if n > 21:
        return((n - 21) *2)
    else:
        return 21 - n

def parrot_trouble(talking, hour):
    if (hour < 7 or hour > 20) and talking:
        return True
    else:
        return False
print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))
print(parrot_trouble(False, 6))
print(parrot_trouble(True, 22))
