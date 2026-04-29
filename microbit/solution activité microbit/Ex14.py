DEGRES = 0

def on_forever():
    basic.show_number(input.compass_heading())
    basic.pause(1000)
basic.forever(on_forever)

def on_forever2():
    global DEGRES
    DEGRES = input.compass_heading()
    if DEGRES < 45:
        basic.show_string("N")
    elif DEGRES < 135:
        basic.show_string("E")
    elif DEGRES < 225:
        basic.show_string("S")
    elif DEGRES < 315:
        basic.show_string("O")
    else:
        basic.show_string("N")
basic.forever(on_forever2)
