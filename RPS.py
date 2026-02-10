import random

while True: 
    print("="*30)
    print("ROCK PAPER SCISSORS")
    print("="*30)
    print("1. Play Game")
    print("2. Exit")
    print("="*30)
    
    menu_choice = input("Select option (1-2): ").strip()
    
    if menu_choice == "2":
        print("Goodbye!")
        break 
    
    elif menu_choice == "1":
        while True:
            print("\n" + "-"*20)
            print("""Choose between rock, paper, and scissors.
1- Rock
2- Paper
3- Scissors
0- Back to Menu""")
            
            system_selection = random.randint(1, 3)
            user_input = input("Enter your choice (0-3): ").strip()
            
            if user_input == "0":
                print("Returning to menu...")
                break  
            
            if not user_input.isdigit():
                print("Error: Please enter a number!")
                continue
            
            user_choice = int(user_input)
            
            if user_choice < 1 or user_choice > 3:
                print("Error: Please enter a number between 1 and 3!")
                continue
            
            choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
            print("\nYou chose: " + choices[user_choice])
            print("System chose: " + choices[system_selection])
            
            if user_choice == system_selection:
                print("It's a tie!")
            elif (user_choice == 1 and system_selection == 3) or \
                (user_choice == 2 and system_selection == 1) or \
                (user_choice == 3 and system_selection == 2):
                print("You win!")
            else:
                print("System wins!")
            
            play_again = input("\nPlay again? (y/n): ").strip().lower()
            if play_again != 'y':
                break  
    
    else:
        print("Invalid option! Please enter 1 or 2.")