
def squareroot(number,error):
    est = (number+1)/2
    if error < 0:
        error = error * -1
    if error == 0:
        print("Error can't be zero")
        return None
    if number < 0:
        print("Negative numbers do not have real square root")
        return None
    if number == 0:
        return 0
    #Making new estimations (by counting an average of current estimate and number to be square-rooted divided by current estimate) until the result is accurate enough
    iterations = 0
    while number >= 0:
        est_new = (est+(number/est))/2
        if abs(est - est_new) < error:
            print(f"Number of iterations: {iterations} ")
            return est_new
        est = est_new
        iterations = iterations + 1



print(squareroot(10000,0.1))

