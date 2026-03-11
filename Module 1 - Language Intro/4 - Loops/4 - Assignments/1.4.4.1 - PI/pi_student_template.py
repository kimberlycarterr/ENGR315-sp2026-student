import math
def pi_estimate(n):
    """
    Use the Gauss-Legendre Algorithm to estimate Pi. Perform n approximation loops. Once complete, return the approximation.
    :param n: number of iterations
    :return: approximation of pi
    """

    # a variable to hold your returned estimate for PI. When you are done,
    # set your estimated value to this variable. Do not change this variable name
    pi_approx = 0

    """
    Step 1: Declare and initialize all the values for the Gauss-Legendre algorithm
    """

    # modify these lines to correct set the variable values
    a = 1
    b = 1 / math.sqrt(2)
    t = 1 / 4
    p = 1

    # perform n iterations of this loop
    for i in range(n):
        # compute next a and b using temporaries to preserve dependencies
        a_next = (a + b) / 2
        b_next = math.sqrt(a * b)
        t = t - p * ((a_next - a) ** 2)
        p = 2 * p

        # commit the next values
        a = a_next
        b = b_next

    # Step 3: After iterating, calculate the final value for PI
    pi_approx = ((a + b) ** 2) / (4 * t)

    return pi_approx

print("Final estimate for PI: ", pi_estimate(10))
print("Error on estimate: ", abs(pi_estimate(10) - math.pi))
