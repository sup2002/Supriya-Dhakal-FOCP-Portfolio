#Q)4)In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014 times, was not out 162 times, and scored 48426 runs. Write a program to calculate and display Boycott's batting average.
#Note: A batting average is the number of runs scored divided by the number of completed innings (i.e. the total times batted minus the times not out).
# Program to calculate batting average

# Given statistics for Geoffrey Boycott
matches_played = 609
times_batted = 1014
not_out = 162
runs_scored = 48426

# Calculating completed innings
completed_innings = times_batted - not_out

# Calculating batting average
batting_average = runs_scored / completed_innings

print(f"Geoffrey Boycott's Batting Average: {batting_average:.2f}")
