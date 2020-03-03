##################
# Emmy Daro and Cynthia Jelke
# This Program collects pendulum measurements of acceleration and time and
# sends them to a reciever
# Time to Complete:
#################

import microbit as mb
import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=7, length=100)

print('Program Started')
mb.display.show(mb.Image.HAPPY)

while not mb.button_a.is_pressed():  # wait for button A to be pressed to begin logging
    mb.sleep(10)

radio.send('start') # Send the word 'start' to start the receiver
mb.sleep(1000)
mb.display.show(mb.Image.HEART)  # Display Heart while logging


# Read and send accelerometer data repeatedly until button A is pressed again
while not mb.button_a.is_pressed():
    ######################################################
    # FILL In HERE
    # Need to collect accelerometer and time measurements
    # Need to format into a single string
    # Send the string over the radio
    x_ac=mb.accelerometer.get_x()

    y_ac=mb.accelerometer.get_y()

    z_ac=mb.accelerometer.get_z()

    time=mb.runningtime()

    message= str(time) + ',' + str(x_ac) + ',' + str(y_ac) + ',' + str(z_ac)
    ######################################################

    radio.send(message)
    mb.sleep(10)



mb.display.show(mb.Image.SQUARE)  # Display Square when program ends