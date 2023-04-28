#!/usr/bin/python3
"""Lockboxes."""


def canUnlockAll(boxes):
    """Check if all boxes can be unlocked."""
    checked: set = set()
    to_check: list = [0]

    while len(to_check) != 0:
        box = to_check.pop(0)
        if box in checked:
            continue
        for key in boxes[box]:
            to_check.append(key)
        checked.add(box)

    return (len(checked) == len(boxes))
