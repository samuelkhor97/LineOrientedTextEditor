class Node:

    def __init__(self, value, link=None):
        self.value = value
        self.next = link

    def __str__(self):
        return "{" + str(self.value) + "}"
