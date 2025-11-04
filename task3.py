import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalize a phone number to international format for SMS sending.

    Args:
        phone_number (str): Raw phone number in arbitrary format.

    Returns:
        str: Normalized phone number that starts with '+',
             contains only digits afterward, and always includes
             the country code '+38' if missing.
    """
    if not isinstance(phone_number, str):
        raise ValueError("Phone number must be a string.")

    # remove all characters except digits and '+'
    cleaned = re.sub(r"[^\d+]", "", phone_number)

    # if starts with '+', ensure no duplicate '+'
    if cleaned.startswith("++"):
        cleaned = cleaned.lstrip("+")

    # normalize prefix
    if cleaned.startswith("+380"):
        # already correct
        normalized = cleaned
    elif cleaned.startswith("380"):
        # missing '+'
        normalized = "+" + cleaned
    elif cleaned.startswith("+38"):
        # rare case '+38...' (without 0)
        normalized = cleaned
    else:
        # local number without country code
        # add +38 (Ukraine)
        normalized = "+38" + cleaned.lstrip("+")

    return normalized

if __name__ == "__main__":
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
