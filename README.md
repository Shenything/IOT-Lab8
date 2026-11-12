# IOT-Lab8
This Repository holds all of the files for IOT Lab 8

# Group Members 
- Mihai
- Romeo
- Ben

# File Contents

publisher.py
- The Publisher.
- Pico reads the temperature and sends it to the subscriber pico.

subscriber.py
- The Subscriber.
- Pico receives the temperature, casts it as a float and checks whether the temperature is higher than 30.
- If the temperature is higher than 30, it will turn on the LED.
- Else it will be turned off.

Note : Both PICOs must be connected to the internet.
