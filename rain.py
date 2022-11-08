#calculate rain

inches_str = input ("how many inches of rain have fallen: ")

inches_float = float(inches_str)
inches_int = int(inches_float)


volume = (inches_float/12)*43560
volume2 = (inches_int/12)*43560

gallons = volume * 7.48051945
gallons2 = volume2 * 7.48051945

print (inches_int,  "in. rain on 1 acrea is" , gallons, "gallons")
print (inches_float,  "in. rain on 1 acrea is" , gallons2, "gallons")


