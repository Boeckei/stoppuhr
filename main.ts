music.playMelody("- G - G - G - C5 ", 160)
let zeit = 0
basic.showNumber(0)
loops.everyInterval(1000, function () {
    zeit += 1
    basic.showNumber(zeit)
})
basic.forever(function () {
    if (input.buttonIsPressed(Button.B)) {
        zeit = 0
        basic.showNumber(0)
    }
    if (input.buttonIsPressed(Button.A)) {
        zeit = 0
    }
})
