#!/usr/bin/python3
"""
    ALX Interview: Lockboxes Challenge
"""


def canUnlockAll(boxes):
    """
        a method that determines if all the boxes can be opened
    """
    n = len(boxes)
    opened_boxes = set([0])
    unopened_boxes = set(boxes[0]).difference(set([0]))
    while len(unopened_boxes) > 0:
        boxId = unopened_boxes.pop()
        if not boxId or boxId >= n or boxId < 0:
            continue
        if boxId not in opened_boxes:
            unopened_boxes = unopened_boxes.union(boxes[boxId])
            opened_boxes.add(boxId)
    return n == len(opened_boxes)
