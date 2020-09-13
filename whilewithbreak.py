def minimumIndexValue(initialValue, incrementalValue, totalLimit):
    number = initialValue
    sum    = 0
    index  = 1

    while (True):
        sum += n
        print("U%03d=%3d, Sum=%5d" %(index, number, sum))
        if (sum > totalLimit):
            break
        index += 1
        number += incrementalValue

    return index

print("Minimum Index Value: %d" %(minimumIndexValue(-2, 3, 10000)))
