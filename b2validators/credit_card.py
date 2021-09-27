from b2validators.exceptions import ValidationError
import re
import datetime


def validate_number(value):
    """
    checks if the value is a valid credit_card number
    """
    value = re.sub("[^0-9]", "", value)
    card_number = list(value.strip())
    check_digit = card_number.pop()
    card_number.reverse()
    card_number = [int(i) for i in card_number]

    for index, digit in enumerate(card_number):
        if index % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        card_number[index] = digit

    card_number = sum(card_number) + int(check_digit)
    if card_number % 10 != 0:
        raise ValidationError("Número de cartão inválido.")
    return value


def validate_cvv(value):
    """
    checks if the value is a valid cvv number
    """
    value = re.sub("[^0-9]", "", value)
    if len(value) != 3:
        raise ValidationError("CVV inválido.")
    return value


def validate_expiration_date_month(value):
    """
    checks if the value is a valid expiration date month
    """
    value = re.sub("[^0-9]", "", value)
    if len(value) != 2:
        raise ValidationError("Mês inválido.")
    if int(value) < 1 or int(value) > 12:
        raise ValidationError("Mês inválido.")
    return value


def validate_expiration_date_year(value, current_year):
    """
    checks if the value is a valid expiration date year
    """
    value = re.sub("[^0-9]", "", value)
    if int(value) < current_year:
        raise ValidationError("Ano inválido.")
    return value


def validate_expiration_date(value):
    """
    checks if the value is a valid expiration date
    """
    pattern_long_year = re.compile(r"^[0-9]{2}/[0-9]{4}$")
    pattern_short_year = re.compile(r"^[0-9]{2}/[0-9]{2}$")
    if pattern_long_year.match(value):
        month = value[:2]
        year = value[3:]
    elif pattern_short_year.match(value):
        month = value[:2]
        year = "20"+value[3:]
    else:
        raise ValidationError(
            "Formato inválido. A data deve ter o formato MM/YY ou MM/YYYY.")
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    validate_expiration_date_month(month)
    validate_expiration_date_year(year, current_year)
    if int(year) < current_year and current_month < int(month):
        raise ValidationError("Data de expiração inválida.")
    return value
