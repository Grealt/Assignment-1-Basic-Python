# Task 1: Read from sample.txt and print line by line
try:
    with open("sample.txt", "r") as file:
        print("Content of sample.txt:")
        for line in file:
            print(line.strip())  # strip removes newline characters
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
