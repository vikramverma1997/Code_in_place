"""
File: moon_weight.py
--------------------
This program computes the equivalent weight on moon with respective to weight on earth.
"""

WEIGHT_EARTH2MOON = 16.6


def main():
   weight_earth = float(input("Enter a weight on Earth: "))
   weight_moon = (WEIGHT_EARTH2MOON * weight_earth) / 100
   print("Equivalent weight on the moon: " + str(weight_moon))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
