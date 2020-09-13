run = True

n = -2

sum = n

N = 1

while (run):
    if (sum > 10000):
        run = False
    print("Sum:",sum,"n:",N,"Number:",n)
    N += 1
    n += 3
    sum += n
    
