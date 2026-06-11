# DimdumOS
*DimdumOS is Os For esp32 written on MicroPython!*
## About
DimdumOS Is A OS for microcontrollers, it was built and tested on **Esp32-CH340C**
## Funcional
ls - list all files in this directory.  
help - all available commands.  
fastfetch - See system info.  
ledon/ledoff - Enable/disable the led.  
cat <Filename> - Display file contents.  
## LED INDICATOR FAQ
Blink 3 times each 0.5 seconds - Startup.  
Blink 10 times each 0.1 second - Error.  
Blink 5 times each 0.2 seconds - Command Successfully executed.
## Install
1. Download **main.py**
2. put **main.py** on your microcontroller (It should be named exacly **main.py**)
3. Connect to the device
4. It should Run automatically, but if not - Press Ctrl+d, it should trigger soft reboot