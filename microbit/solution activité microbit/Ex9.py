def on_forever():
    basic.clear_screen()
    if input.sound_level() < 64:
        basic.show_icon(IconNames.HAPPY)
        basic.pause(500)
    else:
        basic.show_icon(IconNames.SAD)
        basic.pause(500)
basic.forever(on_forever)
