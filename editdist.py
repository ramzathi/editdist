"""Levenshtein distance for short strings."""
from __future__ import annotations


def distance(left: str, right: str) -> int:
    if left == right:
        return 0
    if not left:
        return len(right)
    if not right:
        return len(left)
    prev = list(range(len(right) + 1))
    for i, left_char in enumerate(left, 1):
        curr = [i]
        for j, right_char in enumerate(right, 1):
            insert = curr[j - 1] + 1
            delete = prev[j] + 1
            replace = prev[j - 1] + (left_char != right_char)
            curr.append(min(insert, delete, replace))
        prev = curr
    return prev[-1]
