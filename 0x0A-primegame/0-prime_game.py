#!/usr/bin/python3
"""Prime game."""


def playRound(n, primes):
    """Play a single round."""
    while n not in primes and n > 1:
        n -= 1
    if n in primes:
        return primes[n]
    return "Ben"


def isWinner(x, nums):
    """Get the overall winner of the prime game."""
    if x <= 0:
        return None
    if len(nums) == 0:
        return None
    highest = max(nums)
    if highest == 1:
        return "Ben"
    num = 3
    primes = [2]
    winner = "Maria"
    prime_winner = {2: winner}
    while num <= highest:
        if all([num % prime != 0 for prime in primes]):
            if winner == "Ben":
                winner = "Maria"
            else:
                winner = "Ben"
            primes.append(num)
            prime_winner[num] = winner
        num += 2
    count = {"Ben": 0, "Maria": 0}
    for n in nums:
        count[playRound(n, prime_winner)] += 1
    if count["Ben"] > count["Maria"]:
        return "Ben"
    elif count["Maria"] > count["Ben"]:
        return "Maria"
    else:
        return None
