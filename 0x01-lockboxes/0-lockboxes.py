#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Parameters:
    boxes (list of lists): A list where each element is a list of keys contained in that box.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)  # Total number of boxes
    opened = [False] * n  # List to keep track of opened boxes
    opened[0] = True  # The first box is initially opened
    keys = [0]  # Start with the key to the first box

    while keys:
        current_key = keys.pop()  # Get the current key to open a box
        for key in boxes[current_key]:  # Iterate through all keys in the current box
            if key < n and not opened[key]:  # Check if the key opens a box that hasn't been opened yet
                opened[key] = True  # Mark the box as opened
                keys.append(key)  # Add the key to the list of keys to be processed

    return all(opened)  # Return True if all boxes have been opened, otherwise False

