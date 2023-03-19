def is_zero(x):
    if x == 0:
        print('0')
    else:
        print('not 0')
    
    return x == 0

def is_zero_wrapper(x):
    return is_zero(x)
