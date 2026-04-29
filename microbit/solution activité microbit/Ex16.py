TEMPS = 0

def on_button_pressed_a():
    global TEMPS
    while not (input.button_is_pressed(Button.B)):
        basic.pause(1000)
        TEMPS += 1
        basic.show_number(TEMPS)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global TEMPS
    TEMPS = 0
    basic.show_number(TEMPS)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_number(TEMPS)
    basic.pause(2000)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)
