"""
@author: Khor Peak Siew
@since: 9/9/2018
@modified: 9/9/2018
"""

from node import Node


class linkedList:

    def __init__(self):
        """
        @:self.head: (Node) None when initialized, will be Node object
        @: self.count: (int) Actual number of elements in list
        """
        self.head = None
        self.count = 0

    def __len__(self):
        return self.count

    def __str__(self):
        string = "Linked List: "
        current = self.head
        # Traverse through the list until there is no Node left
        while not (current is None):
            if current != self.head:
                string += " -> " + str(current)
                # Go to next Node
                current = current.next
            else:
                string += str(current)
                current = current.next

        return string

    def __contains__(self, item):
        current = self.head
        # Traverse through the list until there is no Node left
        while not (current is None):
            if current.value == item:
                return True
            current = current.next
        return False

    def __getitem__(self, index):
        try:
            if index < -len(self) or index >= len(self):
                raise StopIteration("Node doesn't exist at this index")
            currentPos = 0
            current = self.head
            if index < 0:
                index = index + len(self)

            # Stop when specified 'index' is reached
            while not (current is None) and currentPos < index:
                current = current.next
                currentPos += 1
            return current

        except StopIteration as e:
            print(e)

    def __setitem__(self, index, item):
        try:
            if index < -len(self) or index >= len(self):
                raise StopIteration("Node doesn't exist at this index")
            currentPos = 0
            current = self.head
            # Index '-1' for last item, '-len(self)' for first item
            if index < 0:
                index = index + len(self)

            while not (current is None) and currentPos < index:
                current = current.next
                currentPos += 1

            current.value = item

        except StopIteration as e:
            print(e)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        else:
            current_self = self.head
            current_other = other.head

            # Two lists are equal if both lists are of the same length
            # and every item is of same value at the same indexes
            while not (current_self is None):
                if current_self.value != current_other.value:
                    return False
                current_self = current_self.next
                current_other = current_other.next

            return True

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def is_empty(self):
        """return True if array is empty, False if otherwise"""
        return self.count == 0

    def reset(self):
        """Reinitialize the list to default state"""
        self.__init__()

    def append(self, item):
        """
        Insert the argument 'item' passed in to end of array
        @:item: (int) Item to be appended
        """
        if self.is_empty():
            self.head = Node(item, None)
        else:
            current = self.head
            for i in range(len(self) - 1):
                current = current.next

            # Append the item as a Node at the end of array
            current.next = Node(item, None)

        self.count += 1

    def insert(self, index, item):
        """
        Insert the argument 'item' passed in to the 'index' passed in
        @:index: (int) Index for the item to be inserted 
        @:item: (int) Item to be inserted
        @:return: (Boolean) Return True if inserted successfully, False otherwise
        """
        try:
            # Check if -len(self) <= index <= len(self)
            if index < -len(self) or index > len(self):
                raise IndexError(
                    "Index must be in between -len(self) to len(self).")

            # Index '-1' for last item, '-len(self)' for first item
            if index < 0:
                index = index + len(self)

            if index == 0:
                self.head = Node(item, self.head)

            else:
                # Insert the 'item' at 'index'
                node = self[index - 1]
                node.next = Node(item, node.next)
            self.count += 1

            return True

        except IndexError as e:
            print(e)
            return False

    def delete(self, index):
        """
        Delete the item from the list at the specified 'index'
        @:index: (int) Index of item to be removed from the list
        @:return valid_index: (Boolean) Return True if item deleted successfully, False otherwise
        @complexity: Worst-Case: O(n) where n is len(self)
        @complexity: Best-Case: O(1) 
        @precondition: There is item at 'index'
        """
        try:
            if self.is_empty():
                raise IndexError("The list is empty.")
            if index < -len(self) or index >= len(self):
                raise IndexError(
                    "Index must be in between -len(self) to len(self).")
            if index < 0:
                index = index + len(self)

            if index == 0:
                self.head = self.head.next
            else:
                node = self[index - 1]
                node.next = node.next.next
            self.count -= 1

            return True

        except IndexError as e:
            print(e)
            return False

    def remove(self, item):
        """
        Remove the argument 'item' passed in from the list if found
        @:item: (int) Item to be removed from the array
        @:return item_found: (Boolean) Return True if item found and removed successfully, False otherwise
        @complexity: Worst-Case: O(n) where n is len(self)
        @complexity: Best-Case: O(1) 
        """
        item_found = False

        try:
            current = self.head
            index = 0

            # Traverse through the list to look for the 'item'
            while not (current is None):
                if current.value == item:
                    # Delete the 'item' from list if found
                    item_found = self.delete(index)
                    break

                index += 1
                current = current.next

            if not item_found:
                raise ValueError

        except ValueError:
            print("Item not found in list.")

        return item_found

    def sort(self, reverse):
        """
        This function will sort elements' values in self, ascendingly or descendingly
        depending on the argument value of 'reverse'
        @:reverse: (Boolean) If True, sort self.the_array in descending order, False if the otherwise
        @:return: Does not return anything
        @complexity: Worst-Case: O(n^2) where n is len(self)
        @complexity: Best-Case: O(n) where n is len(self)
        @post-condition: self.the_array is sorted ascendingly/descendingly
        """
        if not reverse:
            # Traverse through all elements
            for i in range(len(self)):

                # Last i elements are already in place
                for j in range(0, len(self) - i - 1):

                    # traverse the linked list from 0 to n-i-1
                    # Swap values if the element found is greater
                    # than the next element
                    if self[j].value > self[j + 1].value:
                        temp = self[j].value
                        self[j].value = self[j + 1].value
                        self[j + 1].value = temp
        else:
            # Traverse through all elements
            for i in range(len(self)):

                # Last i elements are already in place
                for j in range(0, len(self) - i - 1):

                    # traverse the array from 0 to n-i-1
                    # Swap if the element found is less
                    # than the next element
                    if self[j].value < self[j + 1].value:
                        temp = self[j].value
                        self[j].value = self[j + 1].value
                        self[j + 1].value = temp
