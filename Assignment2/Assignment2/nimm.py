"""
File: nimm.py
-------------------------
This program is a replication of a game called Nimm. In this game, two players participate and remove 1 or 2 stones
at one time from a bag. The player which removes the last stones from the bag loses the game.
"""

# Total stones present in a bag
TOTAL_STONES = 20


# Remove 1 or 2 stones each time from the bag
def remove_stones(total_stones, player_num):
    num_stones = int(input("Player " + str(player_num) + ", would you like to remove 1 or 2 stones?"))
    # Ask the user again for number of stones as number exceeds by 2
    while num_stones > 2:
        num_stones = int(input("Please enter 1 or 2: "))
    remaining_stones = total_stones - num_stones

    return remaining_stones


# Define the number of player e.g. player 1.
def player_number(player_temp):
    player_num = player_temp % 2
    if player_num == 0:
        player_num = 2

    return player_num


def main():
    total_stones = TOTAL_STONES
    player_temp = 1
    # Run program until the bag contains 0 stones.
    while total_stones > 0:
        print("There are " + str(total_stones) + " stones left")
        player_num = player_number(player_temp)
        remaining_stones = remove_stones(total_stones, player_num)
        # Update number of stones after each removal
        total_stones = remaining_stones
        player_temp += 1

    winner_player = player_number(player_temp)
    print("Player " + str(winner_player) + " wins!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
