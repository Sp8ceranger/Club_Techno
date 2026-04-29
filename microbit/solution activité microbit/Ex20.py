for index in range(4):
    pins.servo_write_pin(AnalogPin.P0, 0)
    basic.pause(500)
    pins.servo_write_pin(AnalogPin.P0, 180)
    basic.pause(500)
