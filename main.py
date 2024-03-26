# IMPORT SELENIUM
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select as SL
import re
import time
from os import system, environ
import dotenv

dotenv.load_dotenv()

# Khởi tạo biến webdriver
ops = webdriver.ChromeOptions()
ops.add_argument('--ignore-certificate-errors')
ops.add_argument("--disable-proxy-certificate-handler")
ops.add_argument("--disable-content-security-policy")




# Mở trình duyệt và truy cập vào ip router
def portForward():
    try:
        driver = webdriver.Chrome(options=ops)
        driver.get("http://192.168.1.1")
    except Exception as e:
        print(f"Lỗi: {repr(e)}")

    user_lgn = driver.find_element(By.ID, "Frm_Username")
    user_lgn.send_keys(environ.get("USER_LOGIN_NAME"))

    user_lgn_pw = driver.find_element(By.ID, "Frm_Password")
    user_lgn_pw.send_keys(environ.get("USER_LOGIN_PASSWORD"))

    lgn_btn = driver.find_element(By.ID, "LoginId")
    lgn_btn.click()

    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.ID, "Btn_Close")))
    # Vào Setup
    ad_setup_btn = driver.find_element(By.ID, "Btn_Close")
    ad_setup_btn.click()
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.ID, "FWUrl")))
    # Vào mục Security
    Wan_url = driver.find_element(By.ID, "FWUrl")
    Wan_url.click()
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.ID, "pageIntroduce")))
    # ???
    fx12 = driver.find_element(By.ID, "scrollRightBtn")
    fx12.click()
    time.sleep(10)
    # Vào Mục Port Forwarding
    portForwarding_btn = driver.find_element(By.ID, "portForwarding")
    portForwarding_btn.click()
    time.sleep(5)
    # Mở thiết đặt để thay đổi cổng
    portmngr = driver.find_element(By.ID, "instName_PortForwarding:0")
    portmngr.click()
    # Tiến hành thay đổi cổng
    port_mc = driver.find_element(By.ID, "InternalClient:0")
    port_mc.clear()
    port_mc.send_keys(set_v4ip)
    time.sleep(5)
    # Lưu cài đặt
    save_btn = driver.find_element(By.ID, "Btn_apply_PortForwarding:0")
    save_btn.click()

    # Đăng xuất
    LogOffLnk_btn = driver.find_element(By.ID, "LogOffLnk")
    LogOffLnk_btn.click()

    # Đóng driver
    driver.close()

    return {
        "status": "Done"
    }

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

ip = input("Nhập IPV4 của bạn: ")

set_v4ip = f"192.168.1.{ip}"

res = check(set_v4ip)

if res["status"] == "OK":

    print(f"Đang tiến hành đổi cổng: {set_v4ip}")
    result = portForward()
    if result["status"] == "Done":  print(f"Đã đổi cổng chuyển tiếp sang ipv4: {set_v4ip}")

else:
    print(res["msg"])

