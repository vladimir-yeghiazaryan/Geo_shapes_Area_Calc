from math import pi

def Circle_run():
  radius = int(input("Please provide the radius of the circle (r): "))
  return round(radius * radius * pi, 3)
  