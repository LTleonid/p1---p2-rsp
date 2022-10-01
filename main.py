Player2_Active = 0
Player1_Active = 0
Player2_Score = 0
Player1_Score = 0
while not (input.button_is_pressed(Button.A)):
    basic.show_string("P1")
    if input.button_is_pressed(Button.A):
        Player1_Active = 1
while not (input.button_is_pressed(Button.B)):
    basic.show_string("P2")
    if input.button_is_pressed(Button.B):
        Player2_Active = 1

def on_forever():
    if Player2_Active == 1 and Player1_Active == 1:
        while Player1_Score == 3 or Player2_Score == 3:
            pass
basic.forever(on_forever)
