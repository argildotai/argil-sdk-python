from typing import Optional

class ArgilError(Exception):
    """
    Custom error class for Argil SDK.
    This provides more detailed and specific error messages.
    It can also include additional properties if needed.
    """
    def __init__(self, message: str, status_code: Optional[int] = None, details: Optional[str] = None):
        super().__init__(message)
        self.status_code = status_code
        self.details = details

    def __str__(self) -> str:
        """
        Convert the error to a string.
        This will include the error name, the error message, and the status code (if applicable).
        @returns {str} The string representation of the error.
        """
        str = f"{self.__class__.__name__}: {self.args[0]}"
        if self.status_code:
            str += f" (status code: {self.status_code})"
        if self.details:
            str += f" (details: {self.details})"
        return str

