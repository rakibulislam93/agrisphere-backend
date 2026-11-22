
from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError
from .base import AgriSphereException


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        return None

    if isinstance(exc, AgriSphereException):
        message = str(exc.detail)
        errors = exc.errors
        error_code = exc.error_code

    elif isinstance(exc, ValidationError):
        message = "Validation failed."
        errors = response.data
        error_code = "VALIDATION_ERROR"

    else:
        message = "An error occurred."
        errors = response.data
        error_code = "API_ERROR"

    response.data = {
        "success": False,
        "message": message,
        "errors": errors,
        "error_code": error_code,
    }

    return response
