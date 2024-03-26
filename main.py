from os import system
from utils.getipv4 import getipv4
from utils.run import *

def check(v4ip):
    if v4ip == "192.168.1.1":
        return {
            "status": "failed",
            "msg": "Không thể để ip là 1"
        }
    else:
        return {
            "status": "OK",
            "msg": "IP hợp lệ"
        }
    


try: system("cls")
except: system("clear")

select = input("Vui lòng chọn 2 chế độ sau đây: \n [1]: Tự động lấy ip \n [2]: Nhập ip thủ công\n Lựa chọn của bạn: ")

if int(select) ==  1:
    set_v4ip = getipv4()
elif int(select) > 2:
    print("Lựa chon không hợp lệ!")
else:
    try:
        try: system("cls")
        except: system("clear")
        ip = input("Nhập IPV4 của bạn: ")
    except KeyboardInterrupt:
        exit(0)

    set_v4ip = f"192.168.1.{ip}"

res = check(set_v4ip)

if res["status"] == "OK":
    try: system("cls")
    except: system("clear")
    print(f"Đang tiến hành đổi cổng: {set_v4ip}")
    result = portForward(set_v4ip)
    if result["status"] == "Done":  
        system("cls")
        print(f"Đã đổi cổng chuyển tiếp sang ipv4: {set_v4ip}\n")
else:
    print(res["msg"])

