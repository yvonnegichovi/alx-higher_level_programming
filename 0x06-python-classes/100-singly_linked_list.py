#!/usr/bin/python3

"""This module defines a node of a singly linked list"""


class Node:
    """This class defines the attributes and methods of the Node"""

    def __init__(self, data, next_node=None):
        """This method initializes data and next_node of the class Node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This methood retrives private instance data"""
        return self.__data

    @data.setter
    def data(self, value):
        """This setter method changes the value of data
        through making it a private instance"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """This getter method retrieves private instance next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """This setter methid changes the value of next_node
        through msking it a private instance"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """This class defines a singly linked list"""

    def __init__(self):
        """This method initializes the class SinglyLinkedList"""
        self.head = None

    def sorted_insert(self, value):
        """This method inserts a new Node
        into the correct sorted position in the list"""
        new_node = Node(value)
        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """prints or returns the entire list in stdout"""
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
