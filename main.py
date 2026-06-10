# Imports
from machine import Pin
import machine
import time
import esp32
import os
import _thread
# Variables
temp = (esp32.raw_temperature() - 32)/1.8
uptime = uptime_ms = time.ticks_ms() // 1000
led_pin = Pin(2, Pin.OUT)
Boot = Pin(0, Pin.IN, Pin.PULL_UP)
HelpList = """--=[AVALIBLE COMMANDS]=--
ls - list all files in this directory.
help - all avalible commands.
fastfetch - See system info.
ledon/ledoff - Enable/disable the led."""

# Code
for i in range(5): # Startup Led Flash
    led_pin.value(1)
    time.sleep(0.3)
    led_pin.value(0)
    time.sleep(0.3)
    def LedCommandIndicator(delay,times):
        for i in range(times):
            led_pin.value(1)
            time.sleep(delay)
            led_pin.value(0)
            time.sleep(delay)

print("--=DimdumOS Booted!=--") # Boot info
print("--=[SYSINFO]--")
print(f"Temp: {temp}\nUptime: {uptime // 1000}S\nRam: {gc.mem_free()}/{gc.mem_alloc() + gc.mem_free()}\nCpu Freq: {machine.freq() / 1000000} MHz")
Username = input("\nWelcome to DimdumOS. A OS for ESP32.\nhelp for all avalible commands\nEnter your Username: ")

while True: # Start Console Loop
    Cmd = input(f"{Username}@DimdumOS:~$ ") # Command line
    if Cmd == "ls": # Ls Command
        _thread.start_new_thread(LedCommandIndicator, (0.5, 2))
        files = os.listdir()
        print("\n".join(files)) # List all avalible files
    elif Cmd == "fastfetch": # Fastfetch command
        _thread.start_new_thread(LedCommandIndicator, (0.2, 5))
        temp = (esp32.raw_temperature() - 32)/1.8
        uptime = uptime_ms = time.ticks_ms() // 1000
        sys_info = os.uname()
        os_str = f"{sys_info.sysname} {sys_info.release}"
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
░░░░░░░█▓▒▒▒▒▒▒▒▓▓▓█▓▓▓▓███░▓██▓▓▓▓░░ OS: {os_str}
░░░░░░██▓▒▒▒▒▒▒▒▒▒▓██▓▒▓▓▓▓███▓▓░░    Username: {Username}
░░░░░░█▓▓▒▒▒▒▒▒▒▒▒▓▓██▓▓▒▒▓▓██▓▓░░    Uptime: {uptime}S
░░░░░░█▓▒▒▒▒▒▒▒▒▒▒▒▓▓██▓▒▒▒▓█▓█▓▓░░   Ram: {ram_str}
░░░░░░█▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓█▓▓▒▒▓██▓█▓░░   Cpu Freq: {cpu_str}
░░░░░░█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓██▓▒▒▓▓███▓░░   Locale: en_US
░░░░░░█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓█▓▒▒▒▓▓██▓▓░░  Temp: {temp}°C
░░░░░░█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▓▒▒▒▓▓███▓▓▓░░
░░░░░░█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▓▒▒▒▓██▓▓██▓░░
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
        _thread.start_new_thread(LedCommandIndicator, (0.1, 6))
        print(HelpList) # display all commands
    elif Cmd == "ledon": # LedOn and LedOff (Enable or disable Led)
        led_pin.value(1)
    elif Cmd == "ledoff":
        led_pin.value(0)
    else:
        print("Command Not reconized. 'help' For Command list.")