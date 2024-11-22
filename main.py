user = 0
Player1_choice = 0
Player2_Score = 0
Player1_Score = 0
Phase = 0
Player2_Block = 0
Player2_choice = 0
def choice():
    global user
    user = 1
    while input.button_is_pressed(Button.AB):
        if input.button_is_pressed(Button.A):
            if user != 0:
                user += 0 - 1
            else:
                user = 3
        if input.button_is_pressed(Button.B):
            if user < 4:
                user += 1
            else:
                user = 1
        if Player1_choice == 1:
            basic.show_leds("""
                . . . . .
                . # # # .
                . # # # .
                . # # # .
                . . . . .
                """)
        elif Player1_choice == 2:
            basic.show_leds("""
                # # . . #
                # # . # .
                . . # . .
                # # . # .
                # # . . #
                """)
        elif Player1_choice == 3:
            basic.show_leds("""
                . . . . .
                . # # # #
                # # # # #
                # # # # .
                . . . . .
                """)
    return user

def on_forever():
    global Player2_Score, Player1_Score, Phase, Player2_choice, Player2_Block
    Player2_Score = 0
    Player1_Score = 0
    while not (Player1_Score == 3 or Player2_Score == 3):
        Phase = 0
        if Phase == 0:
            basic.show_string("P1Choice")
            while not (input.button_is_pressed(Button.B)):
                pass
        if Player2_Block == 0:
            basic.show_string("P2Choice")
            while not (input.button_is_pressed(Button.B)):
                if input.button_is_pressed(Button.A):
                    if Player2_choice == 1:
                        basic.show_leds("""
                            . . . . .
                            . # # # .
                            . # # # .
                            . # # # .
                            . . . . .
                            """)
                    elif Player2_choice == 2:
                        basic.show_leds("""
                            # # . . #
                            # # . # .
                            . . # . .
                            # # . # .
                            # # . . #
                            """)
                    elif Player2_choice == 3:
                        basic.show_leds("""
                            . . . . .
                            . # # # #
                            # # # # #
                            # # # # .
                            . . . . .
                            """)
                    elif Player2_choice > 3:
                        Player2_choice = 0
                    Player2_choice += 1
                if input.button_is_pressed(Button.B):
                    Player2_Block = 1
        if Player2_choice == 1 and Player1_choice == 1:
            basic.show_string("Tie")
        elif Player2_choice == 1 and Player1_choice == 2:
            basic.show_string("P1 Win")
            Player1_Score += 1
        elif Player2_choice == 1 and Player1_choice == 3:
            basic.show_string("P2 Win")
            Player2_Score += 1
        elif Player2_choice == 2 and Player1_choice == 1:
            basic.show_string("P1 Win")
            Player1_Score += 1
        elif Player2_choice == 2 and Player1_choice == 2:
            basic.show_string("Tie")
        elif Player2_choice == 2 and Player1_choice == 3:
            basic.show_string("P2 Win")
            Player2_Score += 1
        elif Player2_choice == 3 and Player1_choice == 1:
            basic.show_string("P1 Win")
            Player1_Score += 1
        elif Player2_choice == 3 and Player1_choice == 2:
            basic.show_string("P2 Win")
            Player2_Score += 1
        elif Player2_choice == 3 and Player1_choice == 3:
            basic.show_string("Tie")
basic.forever(on_forever)
