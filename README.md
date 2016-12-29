#RASPBERRY Pi Workshop (NTUOSS)
This Workshop is aimed to guide to the basics of raspberry pi and GPIO controls

##Seting up:
HDMI monitor, keyboard, mouse(optional)

8Gb microSD card with [NOOBS](https://www.raspberrypi.org/downloads/noobs/) install

Power supply (charger or power back with microUSB port)

Wifi module for old - generation Raspi


##On startup:

Connect to Wi-fi

    sudo raspi-config:

change name, password (default name = pi, password = pi)

change keyboard to US

turn on SPI, I2C communication

turn on Camera (if needed)

Install some library and dependencies

    sudo apt-get update
    sudo apt-get install wiringpi
    sudo apt-get install python-rpi.gpio

Secure Shell communication from remote

    ifconfig # to get the ip address from wlan0 inet-address ( 192.168.xx.xx for local network)
    ssh pi@[IP address] # to connect via ssh
    scp [file] pi@[IP addess]:/home/pi/[destination] # to copy files to pi

Some basics command

    sudo shutdown now   # to shutdown 
    gpio readall        # to read all GPIO input (only when wiringPi installed)
    ifconfig            # to get network information
    sudo rasp-config    # to config the pi 

##GPIO tutorials:

refer to python files
    
##Very useful websites:

https://pinout.xyz/

https://learn.sparkfun.com/tutorials/raspberry-gpio

http://wiringpi.com/

https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/

http://www.instructables.com/id/Read-and-write-from-serial-port-with-Raspberry-Pi/
