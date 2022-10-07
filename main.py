def Start():
    global Player2_Active, Player1_Active
    Player2_Active = 0
    Player1_Active = 0
    while not (input.button_is_pressed(Button.A)):
        basic.show_string("P1")
        if input.button_is_pressed(Button.A):
            Player1_Active = 1
    while not (input.button_is_pressed(Button.B)):
        basic.show_string("P2")
        if input.button_is_pressed(Button.B):
            Player2_Active = 1
Player2_choice = 0
Player2_Wait = 0
Player1_choice = 0
Player1_Wait = 0
Player1_Score = 0
Player2_Score = 0
Player1_Active = 0
Player2_Active = 0
Start()

def on_forever():
    global Player2_Score, Player1_Score, Player1_Wait, Player1_choice, Player2_Wait, Player2_choice
    if Player2_Active == 1 and Player1_Active == 1:
        Player2_Score = 0
        Player1_Score = 0
        while not (Player1_Score == 3 or Player2_Score == 3):
            basic.show_string("P1 Choice")
            Player1_Wait = 1
            while Player1_Wait == 1:
                if input.button_is_pressed(Button.A):
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
                    elif Player1_choice > 3:
                        Player1_choice = 1
                    Player1_choice += 1
                if input.button_is_pressed(Button.B):
                    Player1_Wait = 0
            basic.show_string("P2 Choice")
            Player2_Wait = 1
            while Player2_Wait == 1:
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
                        Player2_choice = 1
                    Player2_choice += 1
                if input.button_is_pressed(Button.B):
                    Player2_Wait = 0
basic.forever(on_forever)

# 1 и 1 - ничья
# 1 и 2 - 1
# 1 и 3 - 3
# 2 и 1 - 1
# 2 и 2 - ничья
# 2 и 3 - 2
# 3 и 1 - 3
# 3 и 2 - 2
# 3 и 3 - ничья

def on_forever2():
    global Player1_Score, Player2_Score
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
basic.forever(on_forever2)
