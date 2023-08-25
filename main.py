import math
import pdb
import iss_position


latitude, longitude, day, month, year, hour, minutes =\
        iss_position.iss_position()
print(round(float(latitude)))
if 40 <= round(float(latitude)) <= 60 and 25 <= round(float(longitude)) <= 40:
    print("you can see")
else:
    print("ridi")
