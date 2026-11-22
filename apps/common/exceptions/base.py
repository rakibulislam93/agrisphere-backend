

from rest_framework.exceptions import APIException


class AgriSphereException(APIException):
    status_code = 400
    default_detail = "An error occurred."
    default_code = "GENERAL_ERROR"

    def __init__(
        self,
        message=None,
        errors=None,
        error_code=None,
        status_code=None,
    ):
        self.errors = errors
        self.error_code = error_code or self.default_code

        if status_code is not None:
            self.status_code = status_code

        super().__init__(
            detail=message or self.default_detail,
            code=self.error_code,
        )