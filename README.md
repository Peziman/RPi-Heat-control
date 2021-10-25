# RPi-Heat-control
Python based heat control for my Trotec diesel heater


Setting up the bot

The bot function is part of RNA3210d/RPi-TELEBOT.

- Install telepot library for enabling the Raspberry Pi to communicate with the Telegram bot using the API.

    sudo apt-get install python-pip
    sudo pip install telepot

- Request the BotFather to create a new Bot.
- Paste the HTTP access token here (in the code):
    bot = telepot.Bot('  Enter your Telegram bot API token here  ')
- Run gpiotel20.py as sudo
- Try out the commands given below in the Telegram bot chat (see Usage section below)
- GPIO of led1 and led2 set as 5 and 10 respectively(BCM numbering).

Commands:

- help - get a List of all commands
- cpu - Get CPU info (lscpu) + CPU temperature
- usb - See connected USB devices (lsusb)
- hi - To check if online
- uhrzeit - get time
- datum - get date
- repoupdate - update repositories (sudo apt-get update)
- upgrade - upgrade packages (sudo apt-get upgrade -y)
- shutdown - Shutdown RPi (sudo shutdown -h now)
- reboot - Reboot RPi (sudo reboot)
- heizung aus - Turn off heater
- heizung ein - Turn on heater
- heizung status - get heater status, temperature and fueltank level
- temperatur - get room temperature, humandity and pressure
- stelle temperatur - system ask you for setting temperature
- protokoll - send chat protocol via E-mail
- statistik - send a datalog via E-mail
