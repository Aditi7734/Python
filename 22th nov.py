file_path = 'example.txt'
with open(file_path, 'w') as file:
    file.write('jai mata di')
file_path = 'example.txt'
with open(file_path, 'r') as file:
    # Perform operations on the file
    content = file.read()
    print(content)
file_path = 'example.txt'

# Open the file in read mode ('r')
with open(file_path, 'r') as f1:
    # Read the content of the file
    file_content = f1.read()

    # Print or process the content as needed
    print(file_content)
with open('example.txt', 'r') as file:
    # Read the first 10 characters
    content = file.read(10)
    print(f"Content read: {content}")

    # Get the current position of the file cursor
    position = file.tell()
    print(f"Current position: {position}")
with open('example.txt', 'r') as file:
    # Read the first 10 characters
    content = file.read(10)
    print(f"Content read: {content}")

    # Move the cursor to the beginning of the file
    file.seek(0)

    # Read the next 5 characters from the beginning
    next_content = file.read(5)
    print(f"Next content read: {next_content}")  