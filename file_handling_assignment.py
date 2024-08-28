# Define the filename
filename = "my_file.txt"

# File Creation
try:
    with open(filename, 'w') as file:
        # Writing at least three lines of text, including strings and numbers
        file.write("Hello, this is the first line.\n")
        file.write("Here's a line with a number: 42\n")
        file.write("Final line for initial write.\n")
    print("File created and initial content written successfully.")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")
finally:
    print("File creation and initial writing attempt finished.")

# File Reading and Display
try:
    with open(filename, 'r') as file:
        # Reading and displaying the contents
        content = file.read()
        print("\nContents of the file after initial write:")
        print(content)
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")
finally:
    print("File reading attempt finished.")

# File Appending
try:
    with open(filename, 'a') as file:
        # Appending three additional lines of text
        file.write("Appending a new line.\n")
        file.write("Another appended line with a number: 100\n")
        file.write("Final appended line.\n")
    print("Additional content appended successfully.")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")
finally:
    print("File appending attempt finished.")

# File Reading and Display (After Appending)
try:
    with open(filename, 'r') as file:
        # Reading and displaying the updated contents
        content = file.read()
        print("\nContents of the file after appending:")
        print(content)
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")
finally:
    print("File reading attempt after appending finished.")
