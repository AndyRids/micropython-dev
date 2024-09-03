from machine import ADC, Pin
from micropython import const
from time import sleep


led_pico = Pin("LED", Pin.OUT)

# SoilWatch 3V - usual maxADC value will be around 600
# GP26 -> ADC0 SoilWatch 10
# GP27 -> VCC SoilWatch 10
sensor_vcc = Pin(27, Pin.OUT)
sensor_moisture = ADC(Pin(26, Pin.IN))

CONVERSION_FACTOR = 3.3 / 65535
MIN_ADC = const(1488)
MAX_ADC = const(49212)

# GP6 -> VCC U.S. SOLID Valve
valve_vcc = Pin(6, Pin.OUT)

led_pin = Pin("LED", Pin.OUT)

print("Device running...")
sensor_vcc.on()
sleep(2)

readings = []
while True:
    try:
        led_pico.toggle()
        valve_vcc.toggle()
        sleep(10)
    except KeyboardInterrupt:
        break

led_pin.off()
valve_vcc.off()
sensor_vcc.off()

# print(f"min: {min(readings)}")
# print(f"max: {max(readings)}")

print("Exit")