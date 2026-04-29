def sons():
    if v1 == 0:
        music.play(music.builtin_playable_sound_effect(soundExpression.happy),
            music.PlaybackMode.IN_BACKGROUND)

def on_button_pressed_ab():
    basic.clear_screen()
    basic.show_number(block_casses)
    basic.pause(2000)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_three_g():
    global _3g
    _3g += 1
input.on_gesture(Gesture.THREE_G, on_gesture_three_g)

block_casses = 0
v1 = 0
_3g = 0
v1 = 0
v2 = 0
v3 = 0
block_casses = 0

def on_forever():
    global block_casses, _3g
    if _3g == 0:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
    elif _3g == 1:
        basic.show_leds("""
            . # # # .
            # # # # #
            # # . # #
            # # # # #
            . # # # .
            """)
    elif _3g == 2:
        basic.show_leds("""
            . # # # .
            # . # . #
            # # . # #
            # . # . #
            . # # # .
            """)
    elif _3g == 3:
        basic.show_leds("""
            . # . # .
            # . # . #
            . # . # .
            # . # . #
            . # . # .
            """)
    elif _3g == 4:
        block_casses += 1
        sons()
        basic.show_leds("""
            . # . # .
            # . # . #
            . # . # .
            # . # . #
            . # . # .
            """)
        control.wait_micros(2)
        basic.show_leds("""
            . # # # .
            # . # . #
            # # . # #
            # . # . #
            . # # # .
            """)
        control.wait_micros(2)
        basic.show_leds("""
            . # # # .
            # # # # #
            # # . # #
            # # # # #
            . # # # .
            """)
        control.wait_micros(2)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        _3g = 0
basic.forever(on_forever)
