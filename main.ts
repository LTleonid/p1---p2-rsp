let user = 0
let Phase = 0
let Player1_choice = 0
let Player2_choice = 0
function choice () {
    user = 1
    while (!(input.buttonIsPressed(Button.AB))) {
        if (input.buttonIsPressed(Button.A)) {
            if (user != 0) {
                user += 0 - 1
            } else {
                user = 3
            }
        }
        if (input.buttonIsPressed(Button.B)) {
            if (user < 4) {
                user += 1
            } else {
                user = 1
            }
        }
        if (user == 1) {
            basic.showLeds(`
                . . . . .
                . # # # .
                . # # # .
                . # # # .
                . . . . .
                `)
        } else if (user == 2) {
            basic.showLeds(`
                # # . . #
                # # . # .
                . . # . .
                # # . # .
                # # . . #
                `)
        } else if (user == 3) {
            basic.showLeds(`
                . . . . .
                . # # # #
                # # # # #
                # # # # .
                . . . . .
                `)
        }
    }
    return user
}
function Compare (num: number, num2: number) {
    if (num == 1 && num2 == 1) {
        basic.showString("Tie")
    } else if (num == 1 && num2 == 2) {
        basic.showString("P1 Win")
    } else if (num == 1 && num2 == 3) {
        basic.showString("P2 Win")
    } else if (num == 2 && num2 == 1) {
        basic.showString("P1 Win")
    } else if (num == 2 && num2 == 2) {
        basic.showString("Tie")
    } else if (num == 2 && num2 == 3) {
        basic.showString("P2 Win")
    } else if (num == 3 && num2 == 1) {
        basic.showString("P1 Win")
    } else if (num == 3 && num2 == 2) {
        basic.showString("P2 Win")
    } else if (num == 3 && num2 == 3) {
        basic.showString("Tie")
    }
}
basic.forever(function () {
    Phase = 0
    if (Phase == 0) {
        basic.showString("P1")
        Player1_choice = choice()
        Phase += 1
    }
    if (Phase == 1) {
        basic.showString("P2")
        Player2_choice = choice()
        Phase += 1
    }
    if (Phase == 2) {
        Compare(Player2_choice, Player1_choice)
        Phase = 0
    }
})
