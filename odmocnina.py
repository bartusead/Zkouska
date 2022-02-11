
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
    while number >= 0:
        est_new = (est+(number/est))/2
        if est - est_new < error:
            return est_new
        est = est_new




print(squareroot(16526384834346486.15435484,0.0000000000001))

