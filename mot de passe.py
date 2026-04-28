# Generate code using makcode : https://makecode.microbit.org
# Created by Sp8ceranger (https://github.com/Sp8ceranger) using makcode (https://makecode.microbit.org)
# mot de passe.hex is available here: https://github.com/Sp8ceranger/Spaceranger/edit/main/mot%20de%20passe.hex

def on_button_pressed_a():
    global ENTREE
    ENTREE = "" + ENTREE + "A"
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global ACCEPTED, ENTREE
    if ENTREE == MOT_DE_PASSE:
        basic.show_icon(IconNames.YES)
        ACCEPTED = True
        music.play(music.tone_playable(880, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(330, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(523, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(330, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(831, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
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
ACCEPTED = False
MOT_DE_PASSE = ""
MOT_DE_PASSE = "AABL" # password : buton A (A) + buton B (B) + Logo (L)
ACCEPTED = False
music.set_volume(127)

def on_forever():
    if ACCEPTED == True:
        # when the password is valid
        pass
basic.forever(on_forever)
