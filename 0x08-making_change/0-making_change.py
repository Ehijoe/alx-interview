#!/usr/bin/python3
"""Change comes from within ;)."""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet total."""
    def min_if_exists(a, b):
        """Get the minimum of two values if they exist."""
        if a is None:
            return b
        if b is None:
            return a
        return min(a, b)

    def makeChangeHelper(coins, total, count):
        """Continue counting coins."""
        if total == 0:
            return count
        elif total < 0 or len(coins) == 0:
            return None
        else:
            return min_if_exists(makeChangeHelper(coins,
                                                  total - coins[0],
                                                  count + 1),
                                 makeChangeHelper(coins[1:], total, count))

    if total <= 0:
        return 0
    else:
        count = makeChangeHelper(coins, total, 0)
        if count is not None:
            return count
        return -1
