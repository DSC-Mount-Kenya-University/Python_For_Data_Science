# TODO: Define compute_age_in_future below
def compute_age_in_future(current_year, future_year, current_age):
    if future_year > current_year:
        x = future_year - current_year
        new_age = current_age + x
        return new_age
    elif future_year < current_year:
        x = current_year - future_year
        new_age = current_age - x
        return new_age

# TODO: Define weird_add below


def weird_add(x, y):
    weird_sum = int(str(x)+str(y))
    return weird_sum

# TODO: Define is_prime below


def is_prime(n):
    if (n == 2):
        return True
    else:
        for x in range(2, n):
            if(n % x == 0):
                return False
        return True


# These lines are for your benefit to see what your function
# does on these calls. Feel free to add more here to test
# different inputs.
# Unlike the previous test cases, we won't be checking the
# direct output. We'll call your functions directly many times
# and see that they return the correct value or behave as expected.
print(compute_age_in_future(2020, 2050, 13))
print(weird_add(13, 235))
print(type(weird_add(13, 235)))  # this should be an int
print(is_prime(8))
