def on_forever():
    basic.show_number(input.temperature())
    basic.pause(1000)
basic.forever(on_forever)
