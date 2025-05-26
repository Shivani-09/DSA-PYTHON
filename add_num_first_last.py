
def fun(n, first):
    for i in [n]:
        first = [i] + first
    return first
fun(7, [12,13,99])

def fun(n, last):
    for i in [n]:
        last = last +[i]
    return last
fun(88, [12,13,45])