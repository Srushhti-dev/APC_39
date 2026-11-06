"""Reusable input validation for HealthMate."""

import re
from datetime import date, datetime


TIME_PATTERN = re.compile(r"^(?:[01]\d|2[0-3]):[0-5]\d$")
DATE_PATTERN = re.compile(r"^\d{2}-\d{2}-\d{4}$")
ALLOWED_CATEGORIES = {
    "Water", "Medicine", "Exercise", "Walking", "Meditation", "Break", "Other"
}


def validate_required(value, label):
    """Return trimmed text or raise a clear validation error."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} cannot be empty.")
    return value.strip()


def validate_name(value):
    """Validate a reminder title and return its trimmed value."""
    name = validate_required(value, "Reminder name")
    if len(name) < 3:
        raise ValueError("Reminder name must contain at least 3 characters.")
    if len(name) > 60:
        raise ValueError("Reminder name cannot exceed 60 characters.")
    return name


def validate_time(value):
    """Accept only a valid 24-hour HH:MM time."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Time cannot be empty.")
    time_text = value
    if not TIME_PATTERN.fullmatch(time_text):
        raise ValueError("Please enter a valid time in HH:MM format.")
    return time_text


def validate_date(value, allow_past=False, today=None):
    """Validate DD-MM-YYYY; empty means a repeating daily reminder."""
    if not isinstance(value, str):
        raise ValueError("Please enter a valid date.")
    date_text = value.strip()
    if not date_text:
        return ""
    if not DATE_PATTERN.fullmatch(date_text):
        raise ValueError("Please enter a valid date.")
    try:
        parsed_date = datetime.strptime(date_text, "%d-%m-%Y").date()
    except ValueError as exc:
        raise ValueError("Please enter a valid date.") from exc
    reference_date = today or date.today()
    if not allow_past and parsed_date < reference_date:
        raise ValueError("One-time reminder date cannot be in the past.")
    return parsed_date.strftime("%d-%m-%Y")


def validate_category(value):
    """Validate a category against the application's supported categories."""
    category = validate_required(value, "Category")
    if category not in ALLOWED_CATEGORIES:
        raise ValueError("Please choose a valid category.")
    return category


def validate_description(value):
    """Validate an optional description and return normalized text."""
    if value is None or value == "":
        return ""
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Description cannot contain only spaces.")
    description = value.strip()
    if len(description) > 200:
        raise ValueError("Description cannot exceed 200 characters.")
    return description


def validate_medicine_name(value):
    """Validate a medicine label without suggesting a medicine or dosage."""
    name = validate_required(value, "Medicine name")
    if len(name) < 2:
        raise ValueError("Medicine name must contain at least 2 characters.")
    if len(name) > 60:
        raise ValueError("Medicine name cannot exceed 60 characters.")
    return name


def validate_reminder(title, category, reminder_date, reminder_time, description=""):
    """Validate and normalize all fields used to create a reminder."""
    return {
        "title": validate_name(title),
        "category": validate_category(category),
        "date": validate_date(reminder_date),
        "time": validate_time(reminder_time),
        "description": validate_description(description),
    }


def validate_medicine(title, reminder_time, reminder_date="", description=""):
    """Validate the required medicine name/time and optional details."""
    return {
        "title": validate_medicine_name(title),
        "category": "Medicine",
        "date": validate_date(reminder_date),
        "time": validate_time(reminder_time),
        "description": validate_description(description),
    }


def validate_positive_integer(value, label, maximum=1000):
    """Validate a positive whole number with a field-specific error."""
    try:
        number = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{label} must be a whole number.") from exc
    if str(value).strip() != str(number):
        raise ValueError(f"{label} must be a whole number.")
    if number < 1:
        raise ValueError(f"{label} must be greater than zero.")
    if number > maximum:
        raise ValueError(f"{label} cannot exceed {maximum}.")
    return number


def validate_profile_name(value):
    """Validate a display name for the saved profile."""
    name = validate_required(value, "Name")
    if len(name) > 60:
        raise ValueError("Name cannot exceed 60 characters.")
    return name


def validate_water_goal(value):
    """Validate a daily water goal in glasses."""
    return validate_positive_integer(value, "Daily water goal", maximum=30)


def validate_optional_water_goal(value):
    """Validate an optional personal goal, using zero to represent unset."""
    if value is None or (isinstance(value, str) and not value.strip()):
        return 0
    return validate_water_goal(value)
