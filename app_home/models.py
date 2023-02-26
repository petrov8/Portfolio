from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from support.validators import check_if_letters_only, check_if_digits_only

# Create your models here.

MAX_DEFAULT_FIELD_LEN = 30
MIN_DEFAULT_FIELD_LEN = 2


class ContactModel(models.Model):
    ordering = ("email", )

    MIN_NUMBER_LEN = 7
    MAX_NUMBER_LEN = 16

    MIN_TEXT_LEN = MIN_NUMBER_LEN

    class Meta:
        db_table = "Contact_Model_Table"

    subject = models.CharField(
        verbose_name="Subject",
        validators=[
            MinLengthValidator(MIN_DEFAULT_FIELD_LEN, message=f"Must be at least {MIN_DEFAULT_FIELD_LEN} chars long."),
            MaxLengthValidator(MAX_DEFAULT_FIELD_LEN,
                               message=f"Must be no more than {MAX_DEFAULT_FIELD_LEN} chars long."),
            check_if_letters_only,
        ],
        max_length=MAX_DEFAULT_FIELD_LEN
    )

    full_name = models.CharField(
        verbose_name="Full Name",
        validators=[
            MinLengthValidator(MIN_DEFAULT_FIELD_LEN, message=f"Must be at least {MIN_DEFAULT_FIELD_LEN} chars long."),
            MaxLengthValidator(MAX_DEFAULT_FIELD_LEN,
                               message=f"Must be no more than {MAX_DEFAULT_FIELD_LEN} chars long."),
            check_if_letters_only,
        ],
        max_length=MAX_DEFAULT_FIELD_LEN
    )

    email = models.EmailField(
        verbose_name="Email",
        unique=True,
        max_length=MAX_DEFAULT_FIELD_LEN
    )

    number = models.CharField(
        verbose_name="Contact Number",
        validators=[
            MinLengthValidator(MIN_NUMBER_LEN, message=f"Must be at least {MIN_NUMBER_LEN} digits long."),
            MaxLengthValidator(MAX_NUMBER_LEN,
                               message=f"Must be no more than {MAX_NUMBER_LEN} chars long."),
            check_if_digits_only,
        ],
        max_length=MAX_DEFAULT_FIELD_LEN
    )

    message = models.TextField(
        verbose_name="Message",
        validators=[
            MinLengthValidator(MIN_TEXT_LEN, message=f"Must be at least {MIN_TEXT_LEN} chars long."),
        ]
    )



