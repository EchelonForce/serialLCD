serialLCD
=========

Writes IP addresses to Sparkfun Serial LCD on a Raspberry Pi


Install rpi-serial-console and use it to disable the default serial console.
https://github.com/lurch/rpi-serial-console

sudo rpi-serial-console disable

Install python-serial
sudo apt-get install python-serial

Setup a cron job for the script
sudo crontab -e
add a line: @reboot python /home/pi/serialLCD/serialLCD.py &

Reboot.