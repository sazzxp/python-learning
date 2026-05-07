print ("Welcome to Size Converter")
measurements = float(input("Write the measurement that you wish to convert! "))
unit = input("(c)Centimeter or (m)meter ")
if unit ==  "c" :
    result = measurements / 100
    print(f"{measurements} cm = {result} m")
elif unit == "m" :
    result = measurements * 100
    print(f"{measurements} m = {result} cm")
else :
    print("invalid statement")