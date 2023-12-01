import re
import matplotlib.pyplot as plt

# Open the log file and read its content
with open('output.txt', 'r') as file:
    lines = file.readlines()

# Initialize lists to store extracted information
top1_errors = []

# Regular expression pattern to match lines starting with "Current" and extracting top-1 error
pattern = re.compile(r'Current best accuracy \(top-1 and 5 error\): (\d+\.\d+) \d+\.\d+')

# Iterate through the lines in the log file
for line in lines:
    match = pattern.match(line)
    if match:
        # Extract top-1 error from the matched line
        top1_error = float(match.group(1))
        top1_errors.append(top1_error)

# Create a figure and plot the extracted top-1 errors
plt.plot(top1_errors, marker='o', linestyle='-', color='b', label='Top-1 Error')
plt.title('Top-1 Error Over Time')
plt.xlabel('Iteration')
plt.ylabel('Top-1 Error')
plt.legend()
plt.grid(True)
plt.show()
