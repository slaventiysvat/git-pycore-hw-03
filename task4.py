from __future__ import annotations

from datetime import datetime, date, timedelta
from typing import List, Dict


def _to_date_yyyy_mm_dd(dot_date: str) -> date:
    """Parse 'YYYY.MM.DD' into date."""
    return datetime.strptime(dot_date, "%Y.%m.%d").date()


def _format_dot(d: date) -> str:
    """Format date as 'YYYY.MM.DD' with leading zeros."""
    return d.strftime("%Y.%m.%d")


def _shift_to_monday(d: date) -> date:
    """If d is Saturday (5) or Sunday (6), shift forward to next Monday."""
    if d.weekday() == 5:  # Saturday
        return d + timedelta(days=2)
    if d.weekday() == 6:  # Sunday
        return d + timedelta(days=1)
    return d


def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Return a list of {'name': str, 'congratulation_date': 'YYYY.MM.DD'}
    for all users whose birthday occurs within the next 7 days (inclusive of today).
    If a birthday falls on a weekend, the congratulation date is moved to the next Monday.

    Input:
        users: list of dicts with keys:
            - 'name': user's name (str)
            - 'birthday': 'YYYY.MM.DD' (str)

    Notes:
        - If the birthday this year has already passed (strictly < today), we look at next year.
        - Inclusion criterion uses the actual birthday date (before weekend shifting):
          today <= birthday_date <= today + 7 days.
        - The returned congratulation_date may therefore be the Monday *after* the 7-day window.
    """
    today = date.today()
    horizon = today + timedelta(days=7)
    results: List[Dict[str, str]] = []

    for user in users:
        try:
            bday_orig = _to_date_yyyy_mm_dd(user["birthday"])
            name = user["name"]
        except (KeyError, ValueError, TypeError):
            # Skip invalid records silently (could also raise if required)
            continue

        # Birthday this year
        bday_this_year = bday_orig.replace(year=today.year)

        # If already passed this year, take next year
        if bday_this_year < today:
            bday_target = bday_this_year.replace(year=today.year + 1)
        else:
            bday_target = bday_this_year

        # Check if the actual birthday date is within [today, today+7]
        if today <= bday_target <= horizon:
            congrats_date = _shift_to_monday(bday_target)
            results.append({
                "name": name,
                "congratulation_date": _format_dot(congrats_date),
            })

    # Optional: sort by congratulation date for stable, nice output
    results.sort(key=lambda x: x["congratulation_date"])
    return results

if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith1", "birthday": "1990.11.27"},
        {"name": "Jane Smith2", "birthday": "1995.11.05"},
        {"name": "Jane Smith3", "birthday": "1996.11.06"},
        {"name": "Jane 4", "birthday": "1997.11.07"},
        {"name": "Jane Smith5", "birthday": "1998.11.08"},
    ]
    upcoming = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming)
