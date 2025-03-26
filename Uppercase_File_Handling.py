def process_file(filename):
    try:
        with open(filename, 'r') as file:  
            content = file.read()
            word_count = len(content.split())
            print(f"Number of words: {word_count}")
            print("File content in uppercase:")
            print(content.upper())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")



process_file("one.txt")


"""in one.txt file we provided the text=
This is a sample file.
It has multiple lines."""