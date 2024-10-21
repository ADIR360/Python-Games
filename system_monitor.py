import psutil
import tkinter as tk
from tkinter import ttk
import time

# Function to update system stats
def update_stats():
    cpu_percent = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    net = psutil.net_io_counters()
    
    # Update labels with system stats
    cpu_label.config(text=f"CPU Usage: {cpu_percent}%")
    mem_label.config(text=f"Memory Usage: {mem.percent}%")
    disk_label.config(text=f"Disk Usage: {disk.percent}%")
    net_label.config(text=f"Network Sent: {net.bytes_sent/1024/1024:.2f} MB | Received: {net.bytes_recv/1024/1024:.2f} MB")
    
    # Refresh stats every second
    root.after(1000, update_stats)

# Set up GUI
root = tk.Tk()
root.title("System Performance Analyzer")

# CPU usage label
cpu_label = ttk.Label(root, text="CPU Usage: ")
cpu_label.pack()

# Memory usage label
mem_label = ttk.Label(root, text="Memory Usage: ")
mem_label.pack()

# Disk usage label
disk_label = ttk.Label(root, text="Disk Usage: ")
disk_label.pack()

# Network stats label
net_label = ttk.Label(root, text="Network Sent/Received: ")
net_label.pack()

# Call update_stats() to start the monitoring process
update_stats()

# Run the Tkinter loop
root.mainloop()
