from datetime import datetime
import requests
import socket
import tkinter as tk
import uuid

now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("格式化后的当前时间:", formatted_time)

def get_ip():
    """ 获取本地IP地址 """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # 连接到Google的公共DNS
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        print(f"Error getting IP: {e}")
        return None


def show_popup(text):
    """ 弹出窗口显示文本 """
    popup = tk.Tk()
    popup.title("四川信息职业技术学院校园网自动登录 made by xxg")
    popup.geometry("400x200")
    label = tk.Label(popup, text=text)
    label.pack(pady=20)
    popup.mainloop()


def main():
    local_ip = get_ip()
    if local_ip:
        url = "http://10.10.11.14/webauth.do"  # 假设这是登录页面的URL
        data = {
            "wlanuserip": local_ip,  # 使用获取到的本地IP
            "mac": "74:4a:a4:14:4a:90",  # 假设的MAC地址
            "wlanacname" : "XF_BRAS",
            # 其他需要的数据...
            "hostIp": "http://127.0.0.1:8080/",
    "auth_type": "0",
    "isBindMac1": "0",
    "pageid": "101",
    "templatetype": "1",
    "listbindmac": "0",
    "recordmac": "0",
    "isRemind": "1",
    "url": "http://edge-http.microsoft.com",
    "notice_pic_loop1": "/portal/uploads/pc/demo3/images/logo.jpg",
    "notice_pic_loop2": "/portal/uploads/pc/demo3/images/rrs_bg.jpg",
    "userId": "校园账号",
    "passwd": "密码",
    "remInfo": "on",
            # ...
        }

        # 发送HTTP POST请求
        try:
            response = requests.post(url, data=data)
            response.raise_for_status()  # 如果响应状态码不是200，将抛出HTTPError
            show_popup(f"登录成功!\n当前IP为:{get_ip()}\n\n\n当前时间为：{formatted_time}")
        except requests.RequestException as e:
            show_popup(f"登录失败: {e}")
    else:
        show_popup("无法获取IP地址。")


if __name__ == "__main__":
    main()