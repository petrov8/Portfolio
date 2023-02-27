
import re

from django.core import exceptions


def check_if_letters_and_digits_only(value):
    result = re.search(r"[^\W\d_]", value)
    if not result:
        raise exceptions.ValidationError("Must be letters or digits only.")
    return


def check_if_letters_only(value):
    result = re.search(r"^[a-zA-Z]+(?:[\s.]+[a-zA-Z]+)*$", value)
    if not result:
        raise exceptions.ValidationError("Must be letters only.")
    return


def check_if_digits_only(value):
    result = re.search(r"^[0-9]+$", value)
    if not result:
        raise exceptions.ValidationError("Must be digits only.")
    return


def check_if_full_name(value):
    try:
        first, last = value.split(" ")
        check_if_letters_only(first + last)
    except ValueError:
        raise exceptions.ValidationError("First and Surname required.")

    if len(first) < 2 or len(last) < 2:
        raise exceptions.ValidationError("No initials allowed.")


