

from rest_framework.exceptions import ValidationError


class ValidationError(ValidationError):
    """Base class for all validation errors"""
    pass
