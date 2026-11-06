"""Unit tests for every reusable HealthMate validation function."""

import unittest
from datetime import date

from validation import (
    validate_category,
    validate_date,
    validate_description,
    validate_medicine,
    validate_medicine_name,
    validate_name,
    validate_reminder,
    validate_required,
    validate_time,
)


class ValidationTests(unittest.TestCase):
    def test_required_field_trims_text_and_rejects_empty_values(self):
        self.assertEqual(validate_required("  Water  ", "Category"), "Water")
        for value in ("", "   ", None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                validate_required(value, "Category")

    def test_name_minimum_maximum_and_empty(self):
        self.assertEqual(validate_name(" Walk "), "Walk")
        self.assertEqual(validate_name("x" * 60), "x" * 60)
        with self.assertRaisesRegex(ValueError, "at least 3"):
            validate_name("ab")
        with self.assertRaisesRegex(ValueError, "cannot exceed 60"):
            validate_name("x" * 61)
        with self.assertRaisesRegex(ValueError, "cannot be empty"):
            validate_name(" ")

    def test_time_requires_valid_24_hour_hh_mm(self):
        for value in ("00:00", "09:30", "14:45", "23:59"):
            with self.subTest(value=value):
                self.assertEqual(validate_time(value), value)
        with self.assertRaisesRegex(ValueError, "Time cannot be empty"):
            validate_time("")
        for value in ("9:30", "24:00", "25:70", "12:90", "12:5a", " 09:30"):
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "HH:MM"):
                validate_time(value)

    def test_date_allows_daily_and_rejects_invalid_or_past_calendar_dates(self):
        today = date(2026, 11, 1)
        self.assertEqual(validate_date("", today=today), "")
        self.assertEqual(validate_date("01-11-2026", today=today), "01-11-2026")
        self.assertEqual(validate_date("29-02-2028", today=today), "29-02-2028")
        for value in ("31-02-2027", "29-02-2027", "2026-11-01", "1-11-2026"):
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "valid date"):
                validate_date(value, today=today)
        with self.assertRaisesRegex(ValueError, "past"):
            validate_date("31-10-2026", today=today)
        self.assertEqual(
            validate_date("31-10-2026", allow_past=True, today=today), "31-10-2026"
        )

    def test_category_is_required_and_limited_to_supported_values(self):
        for category in (
            "Water", "Medicine", "Exercise", "Walking", "Meditation", "Break", "Other"
        ):
            with self.subTest(category=category):
                self.assertEqual(validate_category(category), category)
        for category in ("", "   ", "Sleep", "water"):
            with self.subTest(category=category), self.assertRaises(ValueError):
                validate_category(category)

    def test_description_is_optional_but_limited_and_trimmed(self):
        self.assertEqual(validate_description(""), "")
        self.assertEqual(validate_description(None), "")
        self.assertEqual(validate_description("  Take a break  "), "Take a break")
        self.assertEqual(validate_description("x" * 200), "x" * 200)
        with self.assertRaisesRegex(ValueError, "only spaces"):
            validate_description("   ")
        with self.assertRaisesRegex(ValueError, "200 characters"):
            validate_description("x" * 201)

    def test_medicine_name_has_two_character_minimum(self):
        self.assertEqual(validate_medicine_name("Rx"), "Rx")
        with self.assertRaisesRegex(ValueError, "at least 2"):
            validate_medicine_name("x")
        with self.assertRaisesRegex(ValueError, "cannot be empty"):
            validate_medicine_name(" ")
        with self.assertRaisesRegex(ValueError, "60"):
            validate_medicine_name("x" * 61)

    def test_combined_reminder_validation_normalizes_all_fields(self):
        result = validate_reminder(
            "  Morning walk ", "Exercise", "", "09:30", "  Stretch first  "
        )
        self.assertEqual(
            result,
            {
                "title": "Morning walk",
                "category": "Exercise",
                "date": "",
                "time": "09:30",
                "description": "Stretch first",
            },
        )
        with self.assertRaisesRegex(ValueError, "Reminder name"):
            validate_reminder("", "Exercise", "", "09:30")

    def test_medicine_validation_requires_name_and_time(self):
        self.assertEqual(
            validate_medicine("Vitamin plan", "08:15")["category"], "Medicine"
        )
        with self.assertRaisesRegex(ValueError, "Medicine name"):
            validate_medicine("", "08:15")
        with self.assertRaisesRegex(ValueError, "Time"):
            validate_medicine("Medicine", "")
        with self.assertRaisesRegex(ValueError, "HH:MM"):
            validate_medicine("Medicine", "9:30")


if __name__ == "__main__":
    unittest.main()
