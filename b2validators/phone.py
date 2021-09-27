from b2validators.exceptions import ValidationError
from b2validators.values import DDD
import re


def validate_phone_e164(value):
    """
    validates if phone is format E.164
    """
    if not re.match(r'^\+[1-9]\d{1,14}$', value):
        raise ValidationError(
            'Phone number must be in E.164 format'
        )


def validate_phone_ddd(value):
    """
    validates if phone is format DDD
    """
    if not re.match(r'^\d{2}$', str(value)) or str(value) not in DDD:
        raise ValidationError('DDD inválido.')
    return value
