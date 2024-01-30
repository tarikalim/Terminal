import psutil
import tkinter as tk
from tkinter import messagebox
import threading

def show_system_usage():
    root = tk.Tk()
    root.title("Task Manager")
    cpu_label = tk.Label(root, text="CPU Usage:")
    memory_label = tk.Label(root, text="Memory Usage:")
    disk_label = tk.Label(root, text="Storage Usage:")
    battery_label = tk.Label(root, text="Battery Status:")

    cpu_label.pack()
    memory_label.pack()
    disk_label.pack()
    battery_label.pack()
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_usage = psutil.disk_usage('/')
        disk_label.config(text=f"Storage Usage: {disk_usage.used / (1024 ** 3):.2f} GB / {disk_usage.total / (1024 ** 3):.2f} GB")
        battery_status = psutil.sensors_battery()
        if battery_status:
            battery_label.config(text=f"Battery Status: {battery_status.percent}%")
        else:
            battery_label.config(text="Battery Status: N/A")
        cpu_label.config(text=f"CPU Usage: {cpu_percent}%")
        memory_label.config(text=f"Memory Usage: {memory_info.percent:.2f}% ({memory_info.used / (1024 ** 2):.2f} MB / {memory_info.total / (1024 ** 2):.2f} MB)")
        root.update()

try:
    show_system_usage()
except KeyboardInterrupt:
    pass
