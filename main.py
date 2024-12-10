music.play_melody("- G - G - G - C5 ", 160)
zeit = 0
basic.show_number(0)

def on_every_interval():
    global zeit
    zeit += 1
    basic.show_number(zeit)
loops.every_interval(1000, on_every_interval)

def on_forever():
    global zeit
    if input.button_is_pressed(Button.A):
        zeit = 0
basic.forever(on_forever)

def on_forever2():
    if input.button_is_pressed(Button.B):
        basic.show_number(0)
basic.forever(on_forever2)
