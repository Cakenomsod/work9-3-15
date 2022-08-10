let Yellow = 0
let Green = 0
let Red = 0
function Call_Yellow () {
    while (Yellow > 0) {
        pins.digitalWritePin(DigitalPin.P0, 0)
        pins.digitalWritePin(DigitalPin.P1, 1)
        pins.digitalWritePin(DigitalPin.P2, 0)
        basic.showNumber(Yellow)
        basic.pause(200)
        Yellow += -1
        basic.clearScreen()
    }
}
function Call_Green () {
    while (Green > 0) {
        pins.digitalWritePin(DigitalPin.P0, 0)
        pins.digitalWritePin(DigitalPin.P1, 0)
        pins.digitalWritePin(DigitalPin.P2, 1)
        basic.showNumber(Green)
        basic.pause(200)
        Green += -1
        basic.clearScreen()
    }
}
function Call_red () {
    while (Red > 0) {
        pins.digitalWritePin(DigitalPin.P0, 1)
        pins.digitalWritePin(DigitalPin.P1, 0)
        pins.digitalWritePin(DigitalPin.P2, 0)
        basic.showNumber(Red)
        basic.pause(200)
        Red += -1
        basic.clearScreen()
    }
}
basic.forever(function () {
    Red = 7
    Yellow = 3
    Green = 6
    Call_red()
    basic.pause(500)
    Call_Yellow()
    basic.pause(500)
    Call_Green()
    basic.pause(500)
})
