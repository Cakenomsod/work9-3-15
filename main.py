Yellow = 0
Green = 0
Red = 0
def Call_Yellow():
    global Yellow
    while Yellow > 0:
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P12, 1)
        pins.digital_write_pin(DigitalPin.P16, 0)
        basic.show_number(Yellow)
        basic.pause(200)
        Yellow += -1
        basic.clear_screen()
def Call_Green():
    global Green
    while Green > 0:
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P12, 0)
        pins.digital_write_pin(DigitalPin.P16, 1)
        basic.show_number(Green)
        basic.pause(200)
        Green += -1
        basic.clear_screen()
def Call_red():
    global Red
    while Red > 0:
        pins.digital_write_pin(DigitalPin.P8, 1)
        pins.digital_write_pin(DigitalPin.P12, 0)
        pins.digital_write_pin(DigitalPin.P16, 0)
        basic.show_number(Red)
        basic.pause(200)
        Red += -1
        basic.clear_screen()

def on_forever():
    global Red, Yellow, Green
    Red = 7
    Yellow = 3
    Green = 6
    Call_red()
    basic.pause(500)
    Call_Yellow()
    basic.pause(500)
    Call_Green()
    basic.pause(500)
basic.forever(on_forever)
