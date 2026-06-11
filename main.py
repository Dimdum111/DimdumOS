# Imports
from machine import Pin
import machine
import time
import esp32
import os
import _thread
import gc
# Variables
temp = (esp32.raw_temperature() - 32)/1.8
uptime = uptime_ms = time.ticks_ms() // 1000
led_pin = Pin(2, Pin.OUT)
Boot = Pin(0, Pin.IN, Pin.PULL_UP)
DimdumOsVer = "DimdumOs 1.2"
HelpList = """--=[AVAILABLE COMMANDS]=--
ls - list all files in this directory.
help - all available commands.
fastfetch - See system info.
ledon/ledoff - Enable/disable the led.
cat <Filename> - Display file contents.

-=LED INDICATOR FAQ=-
Blink 3 times each 0.5 seconds - Startup.
Blink 10 times each 0.1 second - Error.
Blink 5 times each 0.2 seconds - Command Successfully executed.
"""

# Code
for i in range(3): # Startup Led Flash
    led_pin.value(1)
    time.sleep(0.5)
    led_pin.value(0)
    time.sleep(0.5)
def LedCommandIndicator(delay,times):
    for i in range(times):
        led_pin.value(1)
        time.sleep(delay)
        led_pin.value(0)
        time.sleep(delay)

print("--=DimdumOS Booted!=--") # Boot info
print("--=[SYSINFO]--")
print(f"Temp: {temp}\nUptime: {uptime}S\nRam: {gc.mem_free()}/{gc.mem_alloc() + gc.mem_free()}\nCpu Freq: {machine.freq() / 1000000} MHz")
print("\nWelcome to DimdumOS. A OS for ESP32.\nhelp for all avalible commands.")
while True:
    Username = input("Enter your Username: ").strip()
    if Username == "":
        _thread.start_new_thread(LedCommandIndicator, (0.1, 10))
        print("Username cannot be empty.")
        continue
    break

while True: # Start Console Loop
    CmdUnsplited = input(f"{Username}@DimdumOS:~$ ").strip() # Command line
    parts = CmdUnsplited.split(None, 1)
    if not parts:
        continue
    Cmd = parts[0]
    if Cmd == "ls": # Ls Command
        _thread.start_new_thread(LedCommandIndicator, (0.2, 5))
        files = os.listdir()
        print("\n".join(files)) # List all avalible files
    elif Cmd == "cat": # Cat command
        if len(parts) < 2:
            _thread.start_new_thread(LedCommandIndicator, (0.1, 10))
            print("Not enough arguments. Usage: cat <Filename>")
            continue
        filename = parts[1]
        try:
            with open(filename,"r") as file:
                filecontents = file.read()
            _thread.start_new_thread(LedCommandIndicator, (0.2, 5))
            print("File Readed.\n-----FILEBEGIN-----")
            print(filecontents)
            print("-----FILEEND-----")
        except OSError:
            _thread.start_new_thread(LedCommandIndicator, (0.1, 10))
            print("File does not exist.")
    elif Cmd == "fastfetch": # Fastfetch command
        _thread.start_new_thread(LedCommandIndicator, (0.2, 5))
        temp = (esp32.raw_temperature() - 32)/1.8
        uptime = uptime_ms = time.ticks_ms() // 1000
        sys_info = os.uname()
        MicroController_Str = f"{sys_info.sysname}"
        MicroPythonVer_Str = f"{sys_info.release}"
        ram_str = f"{gc.mem_free()}/{gc.mem_alloc() + gc.mem_free()}"
        cpu_str = f"{machine.freq() / 1000000} MHz"
        
        # Diplay the Art and Info
        print(f"""
░░░░░░░███░░
░░░░░░░█▓▓███░░
░░░░░░░█▓▓▓▓███░░
░░░░░░░█▓▒▒▓▓▓███░░
░░░░░░░█▓▒▒▒▒▓▓▓██░░░░░░░░░░░▓▓▓▓▓▓░░ {Username}@DimdumOs
░░░░░░░█▓▒▒▒▒▒▒▓▓████████░░░▓▓████▓░░ -------------------
░░░░░░░█▓▒▒▒▒▒▒▒▓▓▓█▓▓▓▓███░▓██▓▓▓▓░░ OS: {DimdumOsVer}
░░░░░░██▓▒▒▒▒▒▒▒▒▒▓██▓▒▓▓▓▓███▓▓░░    Username: {Username}
░░░░░░█▓▓▒▒▒▒▒▒▒▒▒▓▓██▓▓▒▒▓▓██▓▓░░    Uptime: {uptime}S
░░░░░░█▓▒▒▒▒▒▒▒▒▒▒▒▓▓██▓▒▒▒▓█▓█▓▓░░   Ram: {ram_str}
░░░░░░█▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓█▓▓▒▒▓██▓█▓░░   Cpu Freq: {cpu_str}
░░░░░░█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓██▓▒▒▓▓███▓░░   Locale: en_US
░░░░░░█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓█▓▒▒▒▓▓██▓▓░░  Temp: {temp}°C
░░░░░░█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▓▒▒▒▓▓███▓▓▓░░Microcontroller: {MicroController_Str}
░░░░░░█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▓▒▒▒▓██▓▓██▓░░MicroPython Ver: {MicroPythonVer_Str}
░░░░░░█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▓▒▒▓▓█▒▒▓▓█▓░░
░░░░░░█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓█▓▒▓▓█▒▒▓▓██▓
░░░░░░█▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓██▓▓▓██▒▓▓█▓▓▓
░░░░░░░█▓▒▒▒▒▒▒▒▒▒▒▒▒▓█▓▓███▓▓▓██▓
░░░░░░░█▓▒▒▒▒▒▒▒▒▒▒▓▓▓████▓▓███▓▓▓
░░░░░░░█▓▒▒▒▒▒▒▒▒▒▒▓████░░▓██▓▓▓
░░░░░░░█▓▒▒▒▒▒▒▒▒▒▒▓██░░░▓▓▓▓▓
░░░░░░░█▓▒▒▒▒▒▒▒▒▒▓▓█░░
░░░░░░██▓▒▒▒▒▒▒▒▒▓███░░
░░░░░░█▓▓▒▒▒▒▒▓▓▓██░░
░░░░░██▓▒▒▒▒▓▓███░░
░░░░░█▓▓▓▓▓▓███░░
░░░░░█▓▓████░░
░░░░░███░░""")
    elif Cmd == "help": # help command
        _thread.start_new_thread(LedCommandIndicator, (0.2, 5))
        print(HelpList) # display all commands
    elif Cmd == "ledon": # LedOn and LedOff (Enable or disable Led)
        led_pin.value(1)
    elif Cmd == "ledoff":
        led_pin.value(0)
    else:
        _thread.start_new_thread(LedCommandIndicator, (0.1, 10))
        print("Command Not reconized. 'help' For Command list.")