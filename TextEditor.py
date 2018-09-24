"""
@author: Khor Peak Siew
@since: 12/9/2018
@modified: 12/9/2018
"""

from linked_list import linkedList
import re


class TextEditor:

    def __init__(self):
        """@:self.the_list: (List) An array based list"""
        self.the_list = linkedList()

    def __str__(self):
        """Return a menu of commands"""
        retval = ""
        retval += "1. Insert a line of text before given index\n"
        retval += "2. Read a file\n"
        retval += "3. Write to a file\n"
        retval += "4. Print line(s) of text between given line num\n"
        retval += "5. Delete line of text at given line num\n"
        retval += "6. Search word\n"
        retval += "7. Quit\n"

        return retval

    def get_line_count(self):
        """Return the current list's length"""
        return len(self.the_list)

    def insert(self, num, line):
        """Insert the 'line' item into self.the_list at index 'num'"""
        self.the_list.insert(num, line)

    def read_file(self, filename):
        """
        Open 'filename' in read mode and append each and every line as an
        item into self.the_list
        @:filename: (String) The file name for the file to be read
        """
        with open(filename, 'r') as f:
            for line in f:
                self.the_list.append(line)

    def write_file(self, filename):
        """
        Open 'filename' in write mode and overwrite content in the file with
        items in self.the_list as lines in file
        @:filename: (String) The file name for the file to be written
        """
        with open(filename, 'w') as f:
            f.seek(0)
            f.truncate()
            for line in self.the_list:
                f.write(line.value)

    def print_lines(self, num1, num2):
        """
        Print the items in self.the_list from index 'num1' till 'num2'
        as new line for each loop
        """
        for i in range(num1, num2 + 1):
            print(str(self.the_list[i]))

    def delete(self, num=None):
        """
        Delete the item in self.the_list at index 'num', if 'num' is not
        specified, will clear the whole list instead
        """
        if num != None:
            self.the_list.delete(num)
        else:
            self.the_list.__init__()

    def search_word(self, word):
        """
        Look for the word in the list and print its line number it is found
        Search is case insensitive and ignores all punctuation. eg Autho,r@! == author
        @: word: (string) Substring to be looked up in the list
        @:return flag: (boolean) True if 'word' is found, False otherwise
        """

        # Strip all non-word characters from the 'word'
        regex = re.compile('[^a-zA-Z]')
        word_only = regex.sub("", word)
        # Make it lowercase
        lower_case_word = word_only.lower()
        # False if 'word' not found, True otherwise
        flag = False

        # Traverse through self.the_list and look for lower_case_word version
        # of 'word'
        for line_number in range(len(self.the_list)):
            found = self.the_list[
                line_number].value.lower().find(lower_case_word)
            if found != -1:
                print(word_only + " is found at line number " +
                      str(line_number + 1))
                flag = True

        if not flag:
            print(word + " is not found")

        return flag
