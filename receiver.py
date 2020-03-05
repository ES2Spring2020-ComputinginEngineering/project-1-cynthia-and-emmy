

##################

# Emmy Daro and Cynthia Jelke

# This Program converts the data received in logger.py into data that can be

# plotted and visualized

# Time to Complete:

#################



import microbit as mb

import radio  # Needs to be imported separately



# Change the channel if other microbits are interfering. (Default=7)

radio.on()  # Turn on radio

radio.config(channel=7, length =100)



print('Program Started')

mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)





# Wait for start message before beginning printing

incoming = ''

while not incoming == 'start':

    incoming = radio.receive()

print('start')





while True:

    incoming = radio.receive() # Read from radio

    mb.sleep(5)
    #print("This is incoming")
    #print(incoming)

    if incoming is not None: # message was received

        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False)



        #############################################################

        # FILL IN HERE

        # Incoming is string sent from logger

        # Need to parse it and reformat as a tuple for the MU plotter

        #############################################################


        value = eval(incoming)#

        #makes it so that you can see the values on the REPL and Plotter
        print(value)
        mb.sleep(100)