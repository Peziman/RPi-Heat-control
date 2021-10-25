# Coder  :- Naveen A. B.
# Reddit :- u/RNA3210d

# Telegram bot to monitor and control your RPi
# The teleport library enables the Raspberry Pi to communicate with the Telegram bot using the API.
# Use "sudo pip install telepot" to install telepot library
import datetime 
import telepot  
import subprocess
from telepot.loop import MessageLoop
from time import sleep      
from gpiozero import CPUTemperature
     



now = datetime.datetime.now()
wait_for_temp = False

#temp variablen für Tests (kommen dann aus dem Hauptprogramm)
hz_error = False
hz_auto = False
hz_ein = False
soll_temp = 15
room_temp = 20
room_hum = 50
room_pres = 995
tank_level = 62


def handle(msg):
    chat_id = msg['chat']['id'] # Receiving the message from telegram
    command = msg['text']   # Getting text from the message
    print ('Incoming...')
    print(command)
    cpu = CPUTemperature()
    temp = cpu.temperature
    # Comparing the incoming message to send a reply according to it
    if wait_for_temp == True:
        if command == '/abort':
            bot.sendMessage(chat_id, str("Ok ich lasse es!"))
        else:
            try:
                command = int(soll_temp)
                bot.sendMessage(chat_id, str("Soll-Temperatur auf ") + str(soll_temp) + str("C° eingestellt"))
            except:
                bot.sendMessage(chat_id, str("Hallo? Ich brauch ne ganze Zahl! Ich breche die Temperatur Einstellung ab!"))
                wait_for_temp = False
    else:
        
        if command == '/help':
            bot.sendMessage (chat_id, str("ledon1 - Switch on LED 1\nledoff1 - Switch off LED 1\nledon2 - Switch on LED 2\nledoff2 - Switch off LED 2\ncpu - Get CPU info\nusb - See connected USB devices\nhi - To check if online\ntime - Returns time\ndate - Returns date\ntemp - CPU Temperature\nrepoupdate - update repositories \nupgrade - upgrade packages\nshutdown - Shutdown RPi\nreboot - Reboot RPi"))
    
        elif command == '/hi':
            bot.sendMessage (chat_id, str("BLEEP..BLOP.., Hallo ike bins... die Werkstatt Heizung!"))
    
        elif command == '/time':
            bot.sendMessage(chat_id, str("Time: ") + str(now.hour) + str(":") + str(now.minute) + str(":") + str(now.second))
    
        elif command == '/date':
            bot.sendMessage(chat_id, str("Date: ") + str(now.day) + str("/") + str(now.month) + str("/") + str(now.year))
    
        elif command == '/Heizung Ein':
            bot.sendMessage(chat_id, str("Heizung wird Automaik Betrieb geschaltet!"))
            hz_auto = True
        
        elif command == '/Heizung Aus':
            bot.sendMessage(chat_id, str("Heizung wird abgeschaltet"))
            hz_auto = False
        
        elif command == '/Heizung Status':
            if hz_error == True:
                bot.sendMessage(chat_id, str("Bei der Heizung ist eine Störung aufgetreten!"))
            else:
                if hz_auto == True and hz_ein == True:
                    bot.sendMessage(chat_id, str("Heizung ist auf Automatik und läuft im Mmoment."))
                elif hz_auto == True and hz_ein == False:
                    bot.sendMessage(chat_id, str("Heizung ist auf Automatik und ist Momentan aus."))
                elif hz_auto == False and hz_ein == False:
                    bot.sendMessage(chat_id, str("Heizung ist aus."))
                else:
                    bot.sendMessage(chat_id, str("Es besteht ein Logikfehler an der Heizung."))
            bot.sendMessage(chat_id, str("Die Temperatur ist auf ") + str(soll_temp) + str("C° eingestellt."))
            bot.sendMessage(chat_id, str("Im Tank befinden sich ") + str(tank_level) + str("l Diesel."))
         
        elif command == '/Temperatur':
            bot.sendMessage(chat_id, str("In der Werkstatt hat es momentan ") + str(room_temp) + str("C°") + str("bei einer Luftfeuchte von ") + str(room_hum) + str("%. ") + str("Der Luftdruck liegt bei ") + str(room_pres) + str("mBar."))
        
        elif command == '/stelle Temperatur':
            if wait_for_temp == False:
                bot.sendMessage(chat_id, str("Die Temperatur ist auf ") + str(soll_temp) + str("C° eingestellt."))
                bot.sendMessage(chat_id, str("Auf welche Soll-Temperatur soll eingestellt werden?"))
                bot.sendMessage(chat_id, str("Geben sie die gewünschte Temperatur als ganze Zahl ein, ohne C°!"))
                bot.sendMessage(chat_id, str("Abbruch mit Kommando /abort"))
                wait_for_temp = True
        
        elif command == '/repoupdate':
            bot.sendMessage(chat_id, str("Updating repos..."))
            p = subprocess.Popen("apt-get update", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
            bot.sendMessage(chat_id, str(p))
            bot.sendMessage(chat_id, str("Update complete"))
    
        elif command == '/upgrade':
            bot.sendMessage(chat_id, str("Upgrading all packages..."))
            p = subprocess.Popen("apt-get upgrade -y", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
            bot.sendMessage(chat_id, str(p))
            bot.sendMessage(chat_id, str("Upgrade complete"))
    
        elif command == '/shutdown':
            bot.sendMessage(chat_id, str("Shutdown command sent.."))
            bot.sendMessage(chat_id, str("Gute Nacht!"))
            subprocess.call('sudo shutdown -h now', shell=True)
    
        elif command == '/reboot':
            bot.sendMessage(chat_id, str("Reboot command sent.."))
            bot.sendMessage(chat_id, str("Bis gleich!"))
            subprocess.call('sudo reboot', shell=True)
    
        elif command == '/cpu':
            p = subprocess.Popen("lscpu", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0])
            bot.sendMessage(chat_id, str(p))
            bot.sendMessage(chat_id, str("CPU temp. : ") + str(temp))
    
        elif command == '/usb':
            p = subprocess.Popen("lsusb", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0])
            bot.sendMessage(chat_id, str(p))
            
        elif command == '/protokoll':
            bot.sendMessage(chat_id, str("Ich sende das Chatprotokoll per E-mail."))
    

        
        
# Enter your telegram token below
bot = telepot.Bot('Enter your Telegram bot API token here')
print (bot.getMe())

# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('GPIOTEL 2.00 at your service...')

while 1:
    sleep(10)
