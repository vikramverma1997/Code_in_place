"""
File: nimm.py
-------------------------
Add your comments here.
"""


TOTAL_STONES = 20


def remove_stones(total_stones, player_num ):
    num_stones = int(input("Player " + str(player_num) + " would you like to remove 1 or 2 stones?"))
    while num_stones > 2:
        num_stones = int(input("Please enter 1 or 2: "))
    remaining_stones = total_stones - num_stones
    return remaining_stones


def player_number(temp):
    player_num = temp % 2
    if player_num == 0:
        player_num = 2
    return player_num


def main():
    total_stones = TOTAL_STONES
    temp = 1

    while total_stones > 0:
        print("There are " + str(total_stones) + " stones left")
        player_num = player_number(temp)
        remaining_stones = remove_stones(total_stones, player_num)
        total_stones = remaining_stones
        temp += 1

    winner_player = player_number(temp)
    print("Player " + str(winner_player) + " wins!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
