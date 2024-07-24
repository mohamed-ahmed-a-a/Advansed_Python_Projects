import os 

def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")


class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True :
            name = input("Enter Your Name : ").strip().capitalize()
            if name.isalpha():
                self.name = name 
                break
            print("Invalid name. Please use letters only.")    

    def choose_symbol(self ,taken_symbols):
        while True:
            symbol = input("{}, Choose Your Symbol (a single letters): ".format(self.name)).strip()
            if symbol.isalpha() and len(symbol) == 1 and  symbol  not in taken_symbols:
                self.symbol = symbol
                break
            print("Invalid symbol. Please choose a single letter.")    

class Menu:
    def display_main_menu(self):
        print("\n\t   Welcome to Tic Tac Toe Game :)\n")
        print("1- Start Game")
        print("2- Quit Game")

        while True:
            choice = input("\tEnter Your Choice (1 or 2): ").strip()
            clean_screen()
            if choice.isdigit() and (choice == "1" or choice == "2"):
                break
            print("Invalid Input. Please choose (1 or 2): ")        
        return choice
    

    def display_endgame_menu(self):
        endtext = """
            GAME OVER !

1- Restart Game
2- Quit Game
Enter Your Choice (1 or 2): """
        while True:
            choice = input(endtext).strip()
            if choice.isdigit() and (choice == "1" or choice == "2"):
                break
            print("Invalid Input. Please choose (1 or 2): ")
        clean_screen()
        return choice
    

class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1,10)]

    def display_board(self):
        for i in range (0, 9, 3):
            print("\t"," | ".join(self.board[i:i+3]))
            if i <6:
                print("\t","-"*10)
    def update_board(self, choice , symbol):
        if self.is_valid_move(choice):
            self.board[choice-1] = symbol
            return True
        else:
            return False    

    def is_valid_move(self, choice):
        return self.board[choice-1].isdigit()
    
    def reset_board(self):
        self.board = [str(i) for i in range(1,10)]


class Game:
    def __init__(self) :
        self.players = [Player() , Player()]
        self.menu = Menu()
        self.board = Board()
        self.current_player_index = 0
        
    def start_game(self):
        choice = self.menu.display_main_menu()
        
        if choice == "1":
            self.setup_players()
            self.play_game()
        elif choice == "2":
            self.quit_game()
        else:
            print("Please Enter A Valid Choice -_^")

    def setup_players(self):
        taken_symbols = []
        for number, player in  enumerate(self.players ,start=1):
            print(f"Player {number}, Enter Your Details: ")
            player.choose_name()
            player.choose_symbol(taken_symbols)
            taken_symbols.append(player.symbol)
            clean_screen()

    def play_game(self):
        while True:
            self.play_turn()
            winner_symbol = self.check_win()
            if winner_symbol:
                winner = next(player for player in self.players  if player.symbol == winner_symbol)
                print(f"Congratulations {winner.name}! You are the winner with symbol {winner.symbol}!")
                choice = self.menu.display_endgame_menu()

                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break


            elif self.check_draw():  
                print("\t It's Draw -_^")
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()


    def check_win(self):
        win_combinations = [
            [0,1,2],[3,4,5],[6,7,8], #rows
            [0,3,6],[1,4,7],[2,5,8], #rows
            [0,4,8],[2,4,6] #diagonal
        ]

        for combo in win_combinations:
            if(self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]):
                return self.board.board[combo[0]]
        return None
        

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)


    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"\n{player.name}'s turn ({player.symbol})")

        while True:
            
            try:
                cell_choice = int(input ("\tChoose a Cell (1-9): "))
                clean_screen()

                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice , player.symbol):
                    break
                else:
                    print("Invalid move , try again")
            except ValueError:
                print("Please Enter a number between 1 and 9.")

        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index     

    def quit_game(self):
        print("\n\tThank You For Playing ^_^\n")     

if __name__ == "__main__":
    game = Game()
    game.start_game()