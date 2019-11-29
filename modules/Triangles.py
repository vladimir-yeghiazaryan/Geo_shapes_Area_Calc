from math import sqrt, sin, radians # sin() uses radians as input

def triangle_perimeter(a, b, c):
    return a + b + c

def triangle_area(a:float, b:float, c:float):
    # checking if triangle exists
    if c < (a + b) and b < (a + c) and a < (b + c):
        perim_half = triangle_perimeter(a, b, c) / 2;
        #  Heron’s formula
        area = round(sqrt(perim_half * (perim_half - a) * (perim_half - b) * (perim_half - c)), 3)  # 3 decimal rounding
        return area
    else:
        return 0  # print("Impossible triangle")

def triangle_area_with_angle(a: float, b: float, alpha: float):
  area = round(((a * b * sin(alpha)) / 2), 3) # sin(alpha) uses radians
  return area

def Triangle_run(version):
  if version == 3:
    side_a = int(input("Please enter the triangle side (a): "))
    side_b = int(input("Please enter the triangle side (b): "))
    side_c = int(input("Please enter the triangle side (c): "))
    return triangle_area(side_a, side_b, side_c)

  elif version == 4:
    side_a = int(input("Please enter the triangle side (a): "))
    side_b = int(input("Please enter the triangle side (b): "))
    angle_c = float(input("Please provide the angle of the triangle (alpha): "))

    return triangle_area_with_angle(side_a, side_b, radians(angle_c)) 

  else:
    return "Unknow error"
    