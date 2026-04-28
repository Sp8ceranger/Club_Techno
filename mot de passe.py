def on_button_pressed_a():
    global ENTREE
    ENTREE = "" + ENTREE + "A"
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global ENTREE
    if ENTREE == MOT_DE_PASSE:
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
    basic.pause(500)
    basic.clear_screen()
    ENTREE = ""
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global ENTREE
    ENTREE = "" + ENTREE + "B"
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global ENTREE
    ENTREE = "" + ENTREE + "L"
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

ENTREE = ""
MOT_DE_PASSE = "AABL"

def on_forever():
    pass
basic.forever(on_forever)
