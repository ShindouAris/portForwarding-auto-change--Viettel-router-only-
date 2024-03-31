from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select as SL
from os import environ, system
import time
import dotenv
ops = webdriver.ChromeOptions()
ops.add_argument('--ignore-certificate-errors')
ops.add_argument("--disable-proxy-certificate-handler")
ops.add_argument("--disable-content-security-policy")

dotenv.load_dotenv()


# Mở trình duyệt và truy cập vào ip router
def portForward(ipv4):
    time.sleep(3)
    try: system("cls")
    except: system("clear")
    try:
        driver = webdriver.Chrome(options=ops)
        driver.get("http://192.168.1.1")
    except Exception as e:
        print(f"Lỗi: {repr(e)}")
    try:
            user_lgn = driver.find_element(By.ID, "Frm_Username")
            user_lgn.send_keys(environ.get("USER_LOGIN_NAME"))
            print(f"Đã đăng nhập bằng user: {environ.get('USER_LOGIN_NAME')}")

            user_lgn_pw = driver.find_element(By.ID, "Frm_Password")
            user_lgn_pw.send_keys(environ.get("USER_LOGIN_PASSWORD"))
            print(f"Mật khẩu: {environ.get('USER_LOGIN_PASSWORD')}")

            lgn_btn = driver.find_element(By.ID, "LoginId")
            lgn_btn.click()

            WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.ID, "Btn_Close")))
            # Vào Setup
            ad_setup_btn = driver.find_element(By.ID, "Btn_Close")
            ad_setup_btn.click()
            print("Đang vào setup")
            WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.ID, "FWUrl")))
            # Vào mục Security
            Wan_url = driver.find_element(By.ID, "FWUrl")
            Wan_url.click()
            print("Đang vào security")
            WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.ID, "pageIntroduce")))
            # ???
            fx12 = driver.find_element(By.ID, "scrollRightBtn")
            fx12.click()
            time.sleep(2)
            # Vào Mục Port Forwarding
            print("Đang mở mục Port Forwarding")
            portForwarding_btn = driver.find_element(By.ID, "portForwarding")
            portForwarding_btn.click()
            time.sleep(2)
            # Mở thiết đặt để thay đổi cổng
            print("Đang mở thiết đặt")
            portmngr = driver.find_element(By.ID, "instName_PortForwarding:0")
            portmngr.click()
            # Tiến hành thay đổi cổng
            print("Đang thay đổi ipv4")
            port_mc = driver.find_element(By.ID, "InternalClient:0")
            port_mc.clear()
            port_mc.send_keys(ipv4)
            
            time.sleep(2)
            # Lưu cài đặt
            print("Đang lưu cài đặt")
            save_btn = driver.find_element(By.ID, "Btn_apply_PortForwarding:0")
            save_btn.click()

            # Đăng xuất
            print("Đang đăng xuất..")
            LogOffLnk_btn = driver.find_element(By.ID, "LogOffLnk")
            LogOffLnk_btn.click()
            time.sleep(3)

    except Exception as e:
         return {
              "status": "failed",
              "msg": e
         }

    # Đóng driver
    driver.close()

    return {
        "status": "Done"
    }