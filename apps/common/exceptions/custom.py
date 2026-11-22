
from rest_framework import status

from .base import AgriSphereException


class BadRequestException(AgriSphereException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Bad request."
    default_code = "BAD_REQUEST"


class UnauthorizedException(AgriSphereException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Authentication required."
    default_code = "UNAUTHORIZED"


class ForbiddenException(AgriSphereException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "You do not have permission."
    default_code = "FORBIDDEN"


class NotFoundException(AgriSphereException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Resource not found."
    default_code = "NOT_FOUND"


class ConflictException(AgriSphereException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Resource conflict."
    default_code = "CONFLICT"


class ValidationException(AgriSphereException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Validation failed."
    default_code = "VALIDATION_ERROR"
