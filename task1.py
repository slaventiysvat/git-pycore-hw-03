from datetime import datetime
import re

_STRICT_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

def get_days_from_today(date: str) -> int:
    """
    Calculate the number of days between the given date and today's date.

    Args:
        date (str): Date in strict 'YYYY-MM-DD' format (zero-padded).

    Returns:
        int: Days from given date to today (positive if past, negative if future).

    Raises:
        ValueError: If the date string is not in strict 'YYYY-MM-DD' format
                    or is not a valid calendar date.
    """
    if not isinstance(date, str) or not _STRICT_DATE_RE.match(date):
        raise ValueError("Invalid date format. Use strict 'YYYY-MM-DD'.")

    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        # invalid calendar date like 2021-02-30
        raise ValueError("Invalid date value. Use a real calendar date in 'YYYY-MM-DD'.")

    today = datetime.today().date()
    return (today - given_date).days


if __name__ == "__main__":
    print(get_days_from_today("2020-10-09"))  # Наприклад, 1492 (залежно від поточної дати)
    print(get_days_from_today("2030-01-01"))  # Від’ємне число, бо в майбутньому
