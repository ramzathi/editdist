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


def within(left: str, right: str, limit: int) -> bool:
    if limit < 0:
        raise ValueError("上限不能为负")
    return distance(left, right) <= limit


def farthest(needle: str, options: list[str]) -> str:
    if not options:
        raise ValueError("没有候选")
    return max(options, key=lambda item: (distance(needle, item), item))


def by_distance(needle: str, options: list[str]) -> list[str]:
    return sorted(options, key=lambda item: (distance(needle, item), item))


def within_any(needle: str, options: list[str], limit: int) -> bool:
    if limit < 0:
        raise ValueError("上限不能为负")
    return any(within(needle, item, limit) for item in options)


def beyond(needle: str, options: list[str], limit: int) -> list[str]:
    if limit < 0:
        raise ValueError("上限不能为负")
    return [item for item in options if not within(needle, item, limit)]


def nearest_distance(needle: str, options: list[str]) -> int:
    if not options:
        raise ValueError("没有候选")
    return distance(needle, closest(needle, options))


def tied(needle: str, options: list[str]) -> list[str]:
    if not options:
        raise ValueError("没有候选")
    limit = nearest_distance(needle, options)
    return [item for item in options if distance(needle, item) == limit]


def only_closest(needle: str, options: list[str]) -> bool:
    return len(tied(needle, options)) == 1


def spread_of(needle: str, options: list[str]) -> int:
    if not options:
        raise ValueError("没有候选")
    dists = [distance(needle, item) for item in options]
    return max(dists) - min(dists)


def nearest_count(needle: str, options: list[str]) -> int:
    return len(tied(needle, options))


def closest(needle: str, options: list[str]) -> str:
    if not options:
        raise ValueError("没有候选")
    return min(options, key=lambda item: (distance(needle, item), item))

def far_count(needle: str, options: list[str]) -> int:
    return len(options) - nearest_count(needle, options)
