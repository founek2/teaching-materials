# Write a Python function that takes a number as a parameter and check the number is prime or not.

def prime(number):
    if number <= 1:
        return False

    for num in range(2, number):  # <2, number-1>
        if number % num == 0:
            # Není to prvočíslo
            return False

        # Ekvivalentní zápis
        # if number % num != 0:
        #    # je to prvočíslo
        #    pass
        # else:
        #    return False

    return True


assert prime(10) == False
assert prime(2) == True
assert prime(7) == True
assert prime(1) == False
assert prime(-111) == False
