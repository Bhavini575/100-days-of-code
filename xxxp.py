earth_weight = float(input("Enter your weight on Earth (in kg): "))


planet = int(input("Enter  planet number (1-7): "))

if planet == 1:
    gravity = 0.38      
elif planet == 2:
    gravity = 0.91      
elif planet == 3:
    gravity = 0.38      
elif planet == 4:
    gravity = 2.53      
elif planet == 5:
    gravity = 1.07      
elif planet == 6:
    gravity = 0.89      
elif planet == 7:
    gravity = 1.14      
else:
    gravity = None

if gravity is None:
    print("Invalid planet no")
else:
    destination_weight = earth_weight * gravity
    print("Your weight on the selected planet is:", destination_weight)