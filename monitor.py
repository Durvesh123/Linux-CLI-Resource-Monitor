#!/usr/bin/env python3

import psutil
import time
import plotext as plt
from rich.console import Console
from datetime import datetime

console = Console()

cpu_history, memory_history, disk_history = [], [], []
max_history = 20

def log_to_file(cpu, memory, disk):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("system_log.txt", "a") as f:
        f.write(f"{timestamp} | CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%\n")

def monitor():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        cpu_history.append(cpu)
        memory_history.append(memory)
        disk_history.append(disk)

        if len(cpu_history) > max_history:
            cpu_history.pop(0)
            memory_history.pop(0)
            disk_history.pop(0)

        console.clear()
        console.print("[bold cyan]Linux System Monitor (CLI Graphs)[/bold cyan]\n")
        console.print(f"[bold red]CPU[/bold red] | [bold yellow]Memory[/bold yellow] | [bold blue]Disk[/bold blue]\n")

        plt.clt()   # clear terminal
        plt.cld()   # clear data
        plt.plot_size(150, 40)

        plt.plot(cpu_history, label="CPU", color="red")
        plt.plot(memory_history, label="Memory", color="yellow")
        plt.plot(disk_history, label="Disk", color="blue")

        plt.ylim(0, 100)
        plt.title("System Resource Usage (%)")
        plt.canvas_color('default')
        plt.axes_color('default')
        plt.ticks_color('white')
        plt.show()

        log_to_file(cpu, memory, disk)

        time.sleep(5)

if __name__ == "__main__":
    monitor()
