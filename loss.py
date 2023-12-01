import re
import matplotlib.pyplot as plt

# Open the log file and read its content
with open('output.txt', 'r') as file:
    lines = file.readlines()

# Initialize lists to store extracted information
test_losses = []

# Flag to indicate whether to start extracting information
extract_info = False

# Regular expression patterns to match lines starting with "Current" and extracting test loss
current_pattern = re.compile(r'Current best accuracy \(top-1 and 5 error\): (\d+\.\d+) (\d+\.\d+)')
loss_pattern = re.compile(r'\* Epoch: \[\d+/\d+\]\s+Top 1-err (\d+\.\d+)\s+Top 5-err (\d+\.\d+)\s+Test Loss (\d+\.\d+)')

# Iterate through the lines in the log file
for line in lines:
    current_match = current_pattern.match(line)
    loss_match = loss_pattern.match(line)

    if current_match:
        # If a line starts with "Current", set the flag to start extracting information
        extract_info = True
        # Extract top-1 and top-5 errors if needed
        top1_error = float(current_match.group(1))
        top5_error = float(current_match.group(2))
    elif extract_info and loss_match:
        # If the flag is set and the line matches the pattern, extract test loss
        test_loss = float(loss_match.group(3))
        
        # Check if the test loss is within an acceptable range (less than or equal to 0.7)
        if test_loss <= 0.7:
            test_losses.append(test_loss)

        # Reset the flag after extracting the information
        extract_info = False

# Create a figure and plot the extracted test losses
plt.plot(test_losses, marker='o', linestyle='-', color='g', label='Test Loss')
plt.title('Test Loss Over Time')
plt.xlabel('Iteration')
plt.ylabel('Test Loss')
plt.legend()
plt.grid(True)
plt.show()
