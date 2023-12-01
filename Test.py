input_file_path = "output.txt"
output_file_path = "output2.txt"

# Open the input file with UTF-8 encoding
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    content = input_file.read()

# Replace all occurrences of '█' with a space
content = content.replace('█', ' ')

# Write the modified content to the output file with UTF-8 encoding
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(content)

print("Replacement completed.")