a=input("First list of colours:").split(",")
b=input("Second list of colours:").split(",")
print("The colours are:")
for color in a:
    if color not in b:
       print (color)
