import sys
import time

# Function to format the duration in hours and minutes
def format_duration(duration):
    return time.strftime("%H Hours, %M Minutes", time.gmtime(duration * 60))

# Function to process cat data from the log file
def process_cat_data(filename):
    cat_visits_count = 0
    other_cats_count = 0
    total_time_in_house = 0
    min_visit_duration = float('inf')
    max_visit_duration = 0
    total_visit_duration = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.strip() == "END":
                    break

                # Extract cat name, entry time, and exit time from the line
                cat_name, entry_time, exit_time = map(str.strip, line.split(','))

                entry_time = int(entry_time)
                exit_time = int(exit_time)

                visit_duration = exit_time - entry_time

                # Update statistics based on cat name
                if cat_name == "OURS":
                    cat_visits_count += 1
                    total_time_in_house += visit_duration
                    total_visit_duration += visit_duration

                    # Update max and min visit durations
                    if visit_duration > max_visit_duration:
                        max_visit_duration = visit_duration

                    if visit_duration < min_visit_duration:
                        min_visit_duration = visit_duration
                else:
                    other_cats_count += 1

        # Print the log file analysis
        print("Log File Analysis")
        print("==================")
        print(f"Cat Visits: {cat_visits_count}")
        print(f"Other Cats: {other_cats_count}")
        print(f"\nTotal Time in House: {format_duration(total_time_in_house)}")
        print(f"\nAverage Visit Length: {format_duration(total_visit_duration // cat_visits_count)}")
        print(f"Longest Visit:        {format_duration(max_visit_duration)}")
        print(f"Shortest Visit:       {format_duration(min_visit_duration)}")

    except FileNotFoundError:
        print(f'Error: The file "{filename}" does not exist!')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Error: Missing command line argument!")
    else:
        # Process the cat data from the log file
        process_cat_data(sys.argv[1])
