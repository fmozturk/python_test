def minimumIndexValue(initialValue, incrementalValue, totalLimit):
    sum   = 0
    index = 1

    for i in range(initialValue, totalLimit, incrementalValue):
        sum += i
        print("U%03d=%3d, Sum=%5d" %(index, i, sum))
        if (sum > totalLimit):
            break
        index += 1

    return index
    
print("Minimum Index Value: %d" %(minimumIndexValue(-2, 3, 10000)))
