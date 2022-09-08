def wrap(value,minValue,maxValue):
    if value < minValue:
        return maxValue
    elif (value > maxValue):
        return minValue
    return value

while True:
    value = input("value")
    minValue = input("minValue")
    maxValue = input("maxValue")

    print(wrap(value,minValue,maxValue))