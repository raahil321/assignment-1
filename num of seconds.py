# Get the number of seconds from the user
seconds = int(input("Enter the number of seconds: "))

# Calculate the number of minutes and seconds
minutes = seconds // 60
remaining_seconds = seconds % 60

# Print out the result
print(seconds, "seconds is", minutes, "minutes and", remaining_seconds, "seconds.")