#!/usr/bin/python3
"""
method to determine is all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    function to determine if all the boxes can be opened
    """

    if boxes is None or boxes == []:
        return False
    if not isinstance(boxes, list):
        return False
    if boxes == [[]]:
        return True
    if boxes[0] == [] and len(boxes) > 1:
        return False

    for box in boxes:
        if not isinstance(box, list):
            return False
        else:
            for item in box:
                if not isinstance(item, int):
                    return False

    Unlocked = [False for box in boxes]
    Unlocked[0] = True
    Open = [False for box in boxes]

    while [True for box in range(len(boxes))
           if Open[box] is False and Unlocked[box] is True]:
        for k in range(len(boxes)):
            if Unlocked[k] is True:
                Open[k] = True
                for box in boxes[k]:
                    try:
                        Unlocked[box] = True
                    except Exception:
                        pass
    return False not in Unlocked
