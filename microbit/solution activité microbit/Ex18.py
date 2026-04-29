def on_received_number(receivedNumber):
    if receivedNumber == 1:
        basic.show_icon(IconNames.SAD)
        basic.pause(1000)
        basic.clear_screen()
    if receivedNumber == 0:
        basic.show_icon(IconNames.HAPPY)
        basic.pause(1000)
        basic.clear_screen()
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_number(0)
    basic.show_icon(IconNames.HAPPY)
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(1)
    basic.show_icon(IconNames.SAD)
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)
