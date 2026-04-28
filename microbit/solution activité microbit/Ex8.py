def on_logo_long_pressed():
    music.play(music.builtin_playable_sound_effect(soundExpression.spring),
        music.PlaybackMode.UNTIL_DONE)
    basic.pause(500)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_logo_pressed():
    music.play(music.builtin_playable_sound_effect(soundExpression.happy),
        music.PlaybackMode.UNTIL_DONE)
    basic.pause(500)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)
