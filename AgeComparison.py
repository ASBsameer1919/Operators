'''
It were the days of domination from the traditional metros in the team selections and everytime the team is announced for the Indian Squad, mere disappointment was left with this small town player. 
Dhoni’ill fate continued even during the team selections for the India A squad to tour to Zimbabwe.3 new players from Mumbai were on the list for the Indian team and it was claimed by the selector
that Dhoni was a bit younger than the 3 selected players.
Assume the 3 players are Named X,Y and Z. The ages of the players X and Y are the same and the age of the Z is 10 more than other 2 players. Given the total age of the 3 players, find the age of the 3 players.
Input format:
First line of the input is an integer that corresponds to the total age of the 3 players.
Output format:
Output should display the ages of the three players in 3 lines. The age of the eldest player should be displayed in the last line.
Sample input and output 1:
70
20
20
30
Sample input and output 2:
100
30
30
40
Ans:
'''
def calculate_ages():
    # Input for total age
    total_age = int(input())
    
    # Let the age of players X and Y be 'a'
    # Let the age of player Z be 'a + 10'
    
    # Equation: 2a + (a + 10) = total_age
    # Simplifying gives: 3a + 10 = total_age
    # So: 3a = total_age - 10
    # Thus: a = (total_age - 10) / 3
    
    a = (total_age - 10) // 3
    age_X = age_Y = a
    age_Z = a + 10
    
    # Output the ages
    print(age_X)
    print(age_Y)
    print(age_Z)

# Call the function to execute
calculate_ages()
