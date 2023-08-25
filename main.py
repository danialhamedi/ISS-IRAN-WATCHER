import requests
import iss_position


latitude, longitude, day, month, year, hour, minutes =\
        iss_position.iss_position()
print(round(float(latitude)))
if 40 <= round(float(latitude)) <= 60 and 25 <= round(float(longitude)) <= 40:
    print("you can see")
    data = {"result": "you can see"}
    requests.post("https://hooks.zapier.com/hooks/catch/16304266/3516k6i/",
                  data=data,
                  timeout=10)
else:
    print("you cant see")
    data = {"result": "you can not see"}
    requests.post("https://hooks.zapier.com/hooks/catch/16304266/3516k6i/",
                  data=data,
                  timeout=10)
