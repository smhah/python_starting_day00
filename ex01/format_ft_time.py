from datetime import datetime

# Define the Unix Epoch
epoch = datetime(1970, 1, 1)

# Get the current date and time
now = datetime.now()

# Calculate the difference in seconds
difference = (now - epoch).total_seconds()

# Format the time with decimal precision and scientific notation
formatted_time = f"Seconds since January 1, 1970: {difference:,.4f}"
scientific_notation = f"{difference:.2e}"

# Print the results
print(formatted_time, f"or {scientific_notation} in scientific notation")

current_date = now.strftime("%b %d %Y")
print(f"{current_date}")

