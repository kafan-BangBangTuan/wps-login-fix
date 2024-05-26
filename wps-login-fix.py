import ctypes
import os
import sys
import winreg
import tkinter as tk
from tkinter import messagebox

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def create_registry_key():
    try:
        key_path = r'Software\kingsoft\Office\6.0\plugins\officespace\flogin'
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path) as key:
            winreg.SetValueEx(key, 'enableforceloginforfirstinstalldevice', 0, winreg.REG_SZ, 'false')
        messagebox.showinfo("WPS强制登录解决工具", "操作成功")
    except Exception as e:
        messagebox.showerror("WPS强制登录解决工具", f"修改注册表时出错: {e}")

def main():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    if messagebox.askyesno("WPS强制登录解决工具", "本程序将会修改注册表，所涉及的风险自行承担。请确认是否继续："):
        create_registry_key()
    else:
        messagebox.showinfo("WPS强制登录解决工具", "用户取消")

if __name__ == "__main__":
    if is_admin():
        main()
    else:
        # 重新以管理员身份运行
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
