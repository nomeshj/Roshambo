
import numpy as np
select,ai ="",""

def game():

    print("Ready...rock,paper,scissor!!")
    game = ["rock", "paper", "scissor"]
    global select,ai
    select = input("select ")
    print("you selected="+select)
    ai = np.random.choice(game)       #randomly getting selected from rock,paper,scissor with random function
    print("AI oppenent selected="+ai)
    #return select,ai
    game_run()

def game_run():

    if select == "rock":
        if ai == "paper":
            print("you loose :(")
        elif ai == "scissor":
            print("you win :)")
        elif ai == "rock":
            print("you both selected same..lets start again ")
            game()


    elif select == "paper":
        if ai == "scissor":
            print("you loose :(")
        elif ai == "rock":
            print("you win :)")
        elif ai == "paper":
            print("you both selected same..lets start again ")
            game()


    elif select == "scissor":
        if ai == "rock":
            print("you loose :(")
        elif ai == "paper":
            print("you win :)")
        elif ai == "scissor":
            print("you both selected same..lets start again ")
            game()
    else:
        print("wrong input")

    choice = input("Wanna play again(yes/no)?=")
    if choice == "yes":
        print("lets go")
        game()
    elif choice == "no":
        print("thanks for playing :)")
    else:
        print("sorry..couldn't get ur response")

game()  #running game function

