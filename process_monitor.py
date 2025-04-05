#!/usr/bin/env python3

import psutil
from rich.console import Console
from rich.table import Table
import time

console = Console()

def list_processes():
    while True:
        table = Table(title="Running Processes")  # Title must be a string

        table.add_column("PID", style="bold cyan")
        table.add_column("Process Name", style="bold magenta")
        table.add_column("CPU %", style="bold yellow")

        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            try:
                table.add_row(
                    str(proc.info['pid']),
                    str(proc.info['name']),
                    str(proc.info['cpu_percent'])
                )
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        console.clear()
        console.print(table)
        time.sleep(5)

if __name__ == "__main__":
    list_processes()
