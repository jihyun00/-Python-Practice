def enough(q, d):
    qpow2 = q**2 
    return abs(qpow2 - d) - 0.0001 < 0

def avg(q, g):
    return (q + g) / 2.0 

def improve(g, x):
    return avg(g, x / g)

def sq(x, g=1):
    if enough(g, x):
        return g
    else:
        return sq(x, improve(g, x))

