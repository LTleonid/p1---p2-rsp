let Player2_Active = 0
let Player1_Active = 0
let Player1_Score = 0
let Player2_Score = 0
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
basic.forever(function () {
    if (Player2_Active == 1 && Player1_Active == 1) {
        while (!(Player1_Score == 3 || Player2_Score == 3)) {
        	
        }
    }
})
