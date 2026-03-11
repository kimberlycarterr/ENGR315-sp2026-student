import math

def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """
    a = 1
    b = 1 / math.sqrt(2)
    t = 1 / 4
    p = 1
    my_pi = 0
    ### YOUR CODE HERE ###
    # Target Error = actual value - nominal value
    while abs(math.pi - my_pi) > abs(target_error):
        a_next = (a+b)/2
        b_next = math.sqrt(a*b)
        t_next = t - p * ((a_next - a) ** 2)
        p_next = 2 * p

        a = a_next
        b = b_next
        t = t_next
        p = p_next

        my_pi = (a_next + b_next) ** 2 / (4 * t_next)

        if abs(math.pi - my_pi) <= abs(target_error):
            return my_pi
        
    # change this so an actual value is returned

desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
