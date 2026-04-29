def on_gesture_shake():
    basic.show_number(randint(0, 6))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
