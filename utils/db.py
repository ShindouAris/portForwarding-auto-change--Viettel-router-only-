import sqlite3


def create_table():
    """Tạo bảng.

    Return:
        Ko co j.
        """
    conn = sqlite3.connect("iplist.sqlite")

    cursor = conn.cursor()

    # Tạo câu lệnh SQL
    sql = f"""CREATE TABLE IF NOT EXISTS iplist (
        id INT AUTO_INCREMENT PRIMARY KEY,
        saved_ip STRING
    );"""

    cursor.execute(sql)
    conn.commit()
    conn.close()

def sql_(sql, v):
        """Thực Hiện Truy Vấn SQL"""
        try:
            c = sqlite3.connect("iplist.sqlite")
            m = c.cursor()
            m.execute(sql, v)
            c.commit()
            c.close()
        except Exception as e:
            return {
                "status": "error",
                "msg": e
            }
        
def fetch_sql():
     """Lấy dữ liệu từ bảng

     Return:

     :status: Trạng thái,
     :xd: Vẫn là trạng thái,
     :id: ID đã được cài trước đó,
     :saved_ip: Các ip đã được lưu,
     :msg: Tin nhắn (Nếu nó lỗi).     
     """
     try:
        c = sqlite3.connect("iplist.sqlite")
        m = c.cursor()
        data = m.execute("SELECT * FROM iplist")
        return {
             "status": "fetch_done",
             "xd": "done",
             "id": data[0],
             "saved_ip": data[1],
             "msg": "FETCH DATA"
        }
     except Exception as e:
          return {
               "status": "fetch_error",
               "xd": "error",
               "id": None,
               "saved_ip": None,
               "msg": e
          }
     
