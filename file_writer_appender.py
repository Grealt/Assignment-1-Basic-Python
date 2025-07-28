# Task 2: Write and append data to output.txt

# Step 1: Write user input to the file
user_input = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Step 2: Append additional data to the same file
additional_input = input("Enter text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(additional_input + "\n")

# Step 3: Read and display final content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
