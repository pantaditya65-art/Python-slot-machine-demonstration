import random

# ---------------------------
# SLOT MACHINE SETTINGS
# ---------------------------

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# How often each symbol appears
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# How much each symbol pays
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


# ---------------------------
# DEPOSIT MONEY
# ---------------------------

def deposit():
    while True:
        amount = input("Enter amount to deposit: ")

        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")


# 
# CHOOSE NUMBER OF LINES
#

def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines to bet on (1-{MAX_LINES}): ")

        if lines.isdigit():
            lines = int(lines)

            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Invalid number of lines.")
        else:
            print("Please enter a number.")


# ---------------------------
# CHOOSE BET AMOUNT
# ---------------------------

def get_bet():
    while True:
        bet = input(f"Enter bet per line ({MIN_BET}-{MAX_BET}): ")

        if bet.isdigit():
            bet = int(bet)

            if MIN_BET <= bet <= MAX_BET:
                return bet
            else:
                print("Invalid bet amount.")
        else:
            print("Please enter a number.")


# ---------------------------
# CREATE SLOT MACHINE SPIN
# ---------------------------

def get_slot_machine_spin(rows, cols, symbols):

    all_symbols = []

    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []

    for _ in range(cols):

        current_symbols = all_symbols[:]
        column = []

        for _ in range(rows):

            value = random.choice(current_symbols)

            current_symbols.remove(value)

            column.append(value)

        columns.append(column)

    return columns


# ---------------------------
# PRINT SLOT MACHINE
# ---------------------------

def print_slot_machine(columns):

    for row in range(len(columns[0])):

        for i, column in enumerate(columns):

            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


# ---------------------------
# CHECK WINNINGS
# ---------------------------

def check_winnings(columns, lines, bet, values):

    winnings = 0
    winning_lines = []

    for line in range(lines):

        symbol = columns[0][line]

        for column in columns:

            symbol_to_check = column[line]

            if symbol != symbol_to_check:
                break

        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


# ---------------------------
# SPIN FUNCTION
# ---------------------------

def spin(balance):

    lines = get_number_of_lines()

    while True:

        bet = get_bet()

        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"Not enough balance. Your balance is ${balance}"
            )
        else:
            break

    print(f"\nYou are betting ${bet} on {lines} lines.")
    print(f"Total bet = ${total_bet}\n")

    slots = get_slot_machine_spin(
        ROWS,
        COLS,
        symbol_count
    )

    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(
        slots,
        lines,
        bet,
        symbol_value
    )

    print(f"\nYou won ${winnings}")

    if winning_lines:
        print(f"Winning lines: {winning_lines}")
    else:
        print("No winning lines.")

    return winnings - total_bet


# ---------------------------
# MAIN GAME LOOP
# ---------------------------

def main():

    balance = deposit()

    while True:

        print(f"\nCurrent balance: ${balance}")

        answer = input(
            "Press Enter to play (q to quit): "
        )

        if answer.lower() == "q":
            break

        balance += spin(balance)

        if balance <= 0:
            print("You ran out of money!")
            break

    print(f"\nYou left with ${balance}")



# START GAME

main()
