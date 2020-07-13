
def compute_bounds(forcasts):
    z = 2.58 
    mean = sum(forcasts) / len(forcasts)   # mean
    var  = sum(pow(x-mean,2) for x in forcasts) / len(forcasts)  # variance
    std  = math.sqrt(var)  

    lb = mean - z * std
    ub = mean + z * std

    return lb, ub