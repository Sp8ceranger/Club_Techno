NOMBRE = 0

def on_gesture_shake():
    global NOMBRE
    NOMBRE = randint(0, 2)
    if NOMBRE == 0:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
    elif NOMBRE == 1:
        basic.show_leds("""
            # # . # #
            # # . # #
            . . # . .
            . # . # .
            # . . . #
            """)
    elif NOMBRE == 2:
        basic.show_leds("""
            . # # # .
            # . . . #
            # . . . #
            # . . . #
            . # # # .
            """)
    basic.pause(500)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
