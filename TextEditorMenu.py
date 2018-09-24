"""
@author: Khor Peak Siew
@since: 12/9/2018
@modified: 12/9/2018
"""

# Menu to initialize the Text Editor class

from TextEditor import TextEditor

# Initialize the TextEditor object
my_text_editor = TextEditor()
quit = False

while not quit:
    # Print the TextEditor commands menu
    print(my_text_editor)
    try:
        command = int(input("Enter your commands: \n"))

        # Insert line of text at given index
        if command == 1:
            # Getting current number of lines of text
            line_count = my_text_editor.get_line_count()

            print("Current line count is: " + str(line_count))
            print(
                "Line number starts from 0, negative line numbers follow list convention.")
            line = input("Enter the line of text: \n")

            try:
                line_num = int(
                    input("Enter line number you would want it to be inserted: \n"))
                if line_num < -line_count or line_num > line_count:
                    raise IndexError(
                        "Valid line number: -(line_count) to (line_count)-1")

                my_text_editor.insert(line_num, line)

            except IndexError as e:
                print("?")
                print(e)

        # Read file
        elif command == 2:
            try:
                file_name = input("Enter file name: ")
                my_text_editor.read_file(file_name)

            except FileNotFoundError:
                print("File not found in current directory.")

        # Write to a file by overwrting its content
        elif command == 3:
            try:
                file_name = input("Enter file name: ")
                my_text_editor.write_file(file_name)

            except FileNotFoundError:
                print("File not found in current directory.")

        # Print lines of text in between given line numbers
        elif command == 4:
            line_count = my_text_editor.get_line_count()

            print("Current line count is: " + str(line_count))
            print(
                "Line number starts from 0, negative line numbers follow list convention.")
            print("Between which line num to print?")

            try:
                num1 = int(input("Line num 1: "))
                num2 = int(input("Line num 2: "))

                # Check for valid line numbers
                if (num2 < num1) or not (-line_count <= num1 < line_count) or not (
                        -line_count <= num1 < line_count):
                    raise IndexError(
                        "Valid line number: -(line_count) to (line_count)-1")

                my_text_editor.print_lines(num1, num2)

            except IndexError as e:
                print("?")
                print(e)

        # Delete line of texts at given line number
        elif command == 5:
            print("Current line count is: " +
                  str(my_text_editor.get_line_count()))
            print(
                "Line number starts from 0, negative line numbers follow list convention.")
            line_count = my_text_editor.get_line_count()

            try:
                line_num = int(input("Enter line number to delete: "))

                # Check for valid line numbers
                if line_num < -line_count or line_num >= line_count:
                    raise IndexError(
                        "Valid line number: -(line_count) to (line_count)-1")

                my_text_editor.delete(line_num)

            except IndexError as e:
                print("?")
                print(e)

        # Search for a word in my_text_editor
        elif command == 6:
            word = input("Enter word to search: ")
            my_text_editor.search_word(word)

        # Quit program
        elif command == 7:
            print("Goodbye!")
            quit = True

        else:
            print("Invalid command number, please try again (0-7)")

    # Catch exception if non-integer input entered as command
    except ValueError as e:
        print(e)
