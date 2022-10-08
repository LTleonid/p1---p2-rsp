function Start () {
    Player2_Active = 0
    Player1_Active = 0
    while (!(input.buttonIsPressed(Button.A))) {
        basic.showString("P1")
        if (input.buttonIsPressed(Button.A)) {
            Player1_Active = 1
        }
    }
    while (!(input.buttonIsPressed(Button.B))) {
        basic.showString("P2")
        if (input.buttonIsPressed(Button.B)) {
            Player2_Active = 1
        }
    }
}
let Player2_choice = 0
let Player2_Block = 0
let Player1_choice = 0
let Player1_Score = 0
let Player2_Score = 0
let Player1_Active = 0
let Player2_Active = 0
Start()
basic.forever(function () {
    if (Player2_Active == 0 && Player1_Active == 0) {
        Player2_Score = 0
        Player1_Score = 0
        while (!(Player1_Score == 3 || Player2_Score == 3)) {
            let Player1_Block = 0
            if (Player1_Block == 0) {
                basic.showString("P1Choice")
                while (!(input.buttonIsPressed(Button.B))) {
                    if (input.buttonIsPressed(Button.A)) {
                        if (Player1_choice == 1) {
                            basic.showLeds(`
                                . . . . .
                                . # # # .
                                . # # # .
                                . # # # .
                                . . . . .
                                `)
                        } else if (Player1_choice == 2) {
                            basic.showLeds(`
                                # # . . #
                                # # . # .
                                . . # . .
                                # # . # .
                                # # . . #
                                `)
                        } else if (Player1_choice == 3) {
                            basic.showLeds(`
                                . . . . .
                                . # # # #
                                # # # # #
                                # # # # .
                                . . . . .
                                `)
                        } else if (Player1_choice > 3) {
                            Player1_choice = 0
                        }
                        Player1_choice += 1
                    }
                }
            }
            if (Player2_Block == 0) {
                basic.showString("P2Choice")
                while (!(input.buttonIsPressed(Button.B))) {
                    if (input.buttonIsPressed(Button.A)) {
                        if (Player2_choice == 1) {
                            basic.showLeds(`
                                . . . . .
                                . # # # .
                                . # # # .
                                . # # # .
                                . . . . .
                                `)
                        } else if (Player2_choice == 2) {
                            basic.showLeds(`
                                # # . . #
                                # # . # .
                                . . # . .
                                # # . # .
                                # # . . #
                                `)
                        } else if (Player2_choice == 3) {
                            basic.showLeds(`
                                . . . . .
                                . # # # #
                                # # # # #
                                # # # # .
                                . . . . .
                                `)
                        } else if (Player2_choice > 3) {
                            Player2_choice = 0
                        }
                        Player2_choice += 1
                    }
                    if (input.buttonIsPressed(Button.B)) {
                        Player2_Block = 1
                    }
                }
            }
            if (Player2_choice == 1 && Player1_choice == 1) {
                basic.showString("Tie")
            } else if (Player2_choice == 1 && Player1_choice == 2) {
                basic.showString("P1 Win")
                Player1_Score += 1
            } else if (Player2_choice == 1 && Player1_choice == 3) {
                basic.showString("P2 Win")
                Player2_Score += 1
            } else if (Player2_choice == 2 && Player1_choice == 1) {
                basic.showString("P1 Win")
                Player1_Score += 1
            } else if (Player2_choice == 2 && Player1_choice == 2) {
                basic.showString("Tie")
            } else if (Player2_choice == 2 && Player1_choice == 3) {
                basic.showString("P2 Win")
                Player2_Score += 1
            } else if (Player2_choice == 3 && Player1_choice == 1) {
                basic.showString("P1 Win")
                Player1_Score += 1
            } else if (Player2_choice == 3 && Player1_choice == 2) {
                basic.showString("P2 Win")
                Player2_Score += 1
            } else if (Player2_choice == 3 && Player1_choice == 3) {
                basic.showString("Tie")
            }
        }
    }
})
