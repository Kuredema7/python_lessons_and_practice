# Make a program where you set a length given in meters and then compute and write
# out the corresponding length measured in inches, in feet, in yards, and in miles.

# Given:-
#   1 inch = 2.54cm
#   1 foot = 12 inches
#   1 yard = 3 feet
#   1 mile = 1760 yards
#   N meter = ???

# First we need to convert '2.5cm' to meter
# 2.54 / 100 = 0.0254 meter
# So we know that 1 inch equals 0.0254 meter


m = 640
inc = m / 0.0254  # Formula of meter to inch
f = inc / 12          # Formula of inch to foot
y = f / 3               # Formula of foot to yard
mi = y / 1760      # Formula of yard to mile

print (m)
print (inc)
print (f)
print (y)
print (mi)
