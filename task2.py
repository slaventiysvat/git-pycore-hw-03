import random
from typing import List

def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> List[int]:
    """
    Generate a sorted list of unique random lottery numbers.

    Args:
        min_value (int): Minimum possible number (>= 1)
        max_value (int): Maximum possible number (<= 1000)
        quantity (int): How many unique numbers to generate

    Returns:
        List[int]: Sorted list of unique random numbers.
                   Empty list if parameters are invalid.
    """
    # Validate parameters
    if (
        not isinstance(min_value, int)
        or not isinstance(max_value, int)
        or not isinstance(quantity, int)
        or min_value < 1
        or max_value > 1000
        or min_value >= max_value
        or quantity <= 0
        or quantity > (max_value - min_value + 1)
    ):
        return []

    # Generate unique random numbers using random.sample
    numbers = random.sample(range(min_value, max_value + 1), quantity)

    # Sort before returning (for readability and reproducibility)
    return sorted(numbers)

if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)
