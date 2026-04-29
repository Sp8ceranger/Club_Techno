def on_gesture_shake():
    global PAS
    PAS += 1
    led.stop_animation()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

PAS = 0

def on_forever():
    basic.show_number(PAS)
basic.forever(on_forever)
