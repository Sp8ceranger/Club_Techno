def on_button_pressed_a():
    basic.show_number(input.light_level())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    led.plot_bar_graph(input.light_level(), 255)
input.on_button_pressed(Button.B, on_button_pressed_b)
