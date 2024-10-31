import random, os

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

arsenal, commands = ("rock", "paper", "scissors", "lizard", "spock"), ('clear', 'exit', 'help')

def sheldonHelp(): print("""
SCISSORS cuts PAPER
PAPER covers ROCK
ROCK crushes LIZARD
LIZARD poisons SPOCK
SPOCK smashes SCISSORS
SCISSORS decapitates LIZARD
LIZARD eats PAPER
PAPER disproves SPOCK
SPOCK vapourizes ROCK
and as it always has
ROCK crushes SCISSORS
""")

def handleCommands(player1, player2):
    if player1 in commands or player2 in commands:
        if player1 == "clear" or player2 == "clear": clear()
        if player1 == "exit" or player2 == "exit": exit()
        if player1 == "help" or player2 == "help": sheldonHelp()


def main(player1, player2, isAlone):
    result = None
    handleCommands(player1, player2)
    if player1 in arsenal and player2 in arsenal:
        input("Press enter to reveal the answer...")
        if player1 == player2: result = "It's a Tie"
        elif    (player1 == "rock" and (player2 == "scissors" or player2 == "lizard")) or \
                (player1 == "paper" and (player2 == "rock" or player2 == "spock")) or \
                (player1 == "scissors" and (player2 == "paper" or player2 == "lizard")) or \
                (player1 == "lizard" and (player2 == "paper" or player2 == "spock")) or \
                (player1 == "spock" and (player2 == "rock" or player2 == "scissors")):
            result = "You Win" if isAlone else "Player 1 Wins!"
        else: result = "You Lose" if isAlone else "Player 2 Wins!"
            
        print(f"I choose '{player2.title()}'. {result}" if isAlone else result)
clear()

while True:
    isAlone = input("Are you playing Alone? (Y/n) ").lower()
    if "y" in isAlone:
        while True: main(input(r".\Computer\RPSLS\Player> ").lower(), random.choice(arsenal), True)
    elif "n" in isAlone:
        while True:
            player1 = input(r".\Humans\RPSLS\Player1> ").lower()
            clear()
            handleCommands(player1, None)
            player2 = input(r".\Humans\RPSLS\Player2> ").lower()
            clear()
            handleCommands(None, player2)
            main(player1, player2, False)
