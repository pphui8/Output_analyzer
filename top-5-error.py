import re
import matplotlib.pyplot as plt

# Open the log file and read its content
with open('output.txt', 'r') as file:
    lines = file.readlines()

# Initialize lists to store extracted information
top5_errors = []

# Regular expression pattern to match lines starting with "Current" and extracting top-5 error
pattern = re.compile(r'Current best accuracy \(top-1 and 5 error\): \d+\.\d+ (\d+\.\d+)')

# Iterate through the lines in the log file
for line in lines:
    match = pattern.match(line)
    if match:
        # Extract top-5 error from the matched line
        top5_error = float(match.group(1))
        top5_errors.append(top5_error)

# Create a figure and plot the extracted top-5 errors
plt.plot(top5_errors, marker='o', linestyle='-', color='r', label='Top-5 Error')
plt.title('Top-5 Error Over Time')
plt.xlabel('Iteration')
plt.ylabel('Top-5 Error')
plt.legend()
plt.grid(True)
plt.show()
