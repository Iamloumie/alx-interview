#!/usr/bin/python3
"""
a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    a function that checks if all boxes of a list can be unlocked
    thus, the unlocked boxes will be saved in a set for uniqueness
    """
    unlocked = {0}

    """a stack to save keys and visit the boxes it can open"""
    stack = [0]

    while stack:
        """as far as there are numbers in the stack continues"""
        current_box = stack.pop()
        """
        This will pop the item in the stack,
        a new way to append new item will be done.
        """
        for key in boxes[current_box]:
            """the above check the keys that are in the current box"""
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    """ returns true when the keys is equal to the boxes unlocked"""
    return len(unlocked) == len(boxes)
