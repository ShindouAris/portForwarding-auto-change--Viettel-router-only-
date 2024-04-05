from os import system
from utils.getipv4 import getipv4
from utils.run import *
import asyncio
from inputimeout import inputimeout
from utils.db import Database
from timeit import default_timer

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
timeout = 5

def timer(func):
    def wrapper(*args, **kwargs):
        start = default_timer()
        res = func(*args, **kwargs)
        end = default_timer()
        print(f"Thời gian chạy: {round((end - start), 2)}s")
        return res
    return wrapper
    


try: system("cls")
except: system("clear")


async def main():
        global select, set_v4ip
        try:
            select = inputimeout(f"Vui lòng chọn 2 chế độ sau đây: \n [1]: Tự động lấy ip \n [2]: Nhập ip thủ công\n Lưu ý: Sẽ tự động chọn ip nếu người dùng không tương tác sau {timeout} giây \nLựa chọn của bạn: ", timeout=timeout)
        except Exception:
            set_v4ip = getipv4()
        try:
            if int(select) ==  1:
                set_v4ip = getipv4()
            elif int(select) > 2:
                print("Lựa chon không hợp lệ!")
                system("shutdown -r -t 10")
                set_v4ip = "192.168.1.1"
            else:
                try:
                    try: system("cls")
                    except: system("clear")
                    ip = input("Nhập IPV4 của bạn: ")
                except KeyboardInterrupt:
                    exit(0)

            set_v4ip = f"192.168.1.{ip}"
        except NameError:
            pass
        
        Database.sql_("""INSERT TO """)
        res = check(set_v4ip)

        if res["status"] == "OK":
            try: system("cls")
            except: system("clear")
            print(f"Đang tiến hành đổi cổng: {set_v4ip}")
            program = portForward(set_v4ip)
            if program["status"] == "Done":  
                system("cls")
                print(f"Đã đổi cổng chuyển tiếp sang ipv4: {set_v4ip}\n")
                time.sleep(10)
            elif program["status"] == "failed":
                print(f"Đã xảy ra lỗi: {repr(program['msg'])}")
        else:
            print(res["msg"])
            system("pause")

if __name__ == "__main__":
    asyncio.run(main())

