import requests
val = {"username" : "mohammadj.yusefi99", "password" : "MJYoosefi6900"}
r = requests.post("https://net2.sharif.edu/login", params=val)
print(r.status_code)

