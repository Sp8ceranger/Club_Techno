NOMBRE_1 = 0
NOMBRE_2 = 0

def on_button_pressed_a():
    global NOMBRE_1
    NOMBRE_1 += 1
    basic.show_number(NOMBRE_1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global NOMBRE_2, NOMBRE_1
    basic.show_leds("""
        . . . . .
        . # # # .
        . . . . .
        . # # # .
        . . . . .
        """)
    basic.show_number(NOMBRE_1 + NOMBRE_2)
    NOMBRE_2 = 0
    NOMBRE_1 = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global NOMBRE_2
    basic.show_leds("""
        . . # . .
        . . # . .
        # # # # #
        . . # . .
        . . # . .
        """)
    NOMBRE_2 += 1
    basic.show_number(NOMBRE_2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
