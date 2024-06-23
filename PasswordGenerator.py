from random import randint
from random import choices
from random import shuffle
import string

def passwordGen(n):
    if n < 12:
        n = 12
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    other = ".,;:-_!?$%&/()="
    pwlst = choices(lower, k = n - 6)
    pwlst += [upper[randint(0, len(upper) - 1)]]
    pwlst += [upper[randint(0, len(upper) - 1)]]
    pwlst += [digits[randint(0, len(digits) - 1)]]
    pwlst += [digits[randint(0, len(digits) - 1)]]
    pwlst += [other[randint(0, len(other) - 1)]]
    pwlst += [other[randint(0, len(other) - 1)]]
    shuffle(pwlst)
    return "".join(pwlst)

for _ in range(5):
    print(passwordGen(12))