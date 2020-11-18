name = 'sciiif'
age = 32.0
height = 70.0 # inches
weight = 230.0 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

centimeters = 2.54
combined = centimeters * height
print(f"He is {height} inches tall which is {combined} centimeters tall")
