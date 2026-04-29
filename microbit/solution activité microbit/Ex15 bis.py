def on_button_pressed_a():
    global METRES
    METRES += 25
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global PAS
    PAS += 1
    led.stop_animation()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

METRES = 0
PAS = 0

def on_forever():
    basic.show_number(PAS)
basic.forever(on_forever)

def on_forever2():
    basic.show_number(PAS * METRES)
basic.forever(on_forever2)
