class TenorException(Exception):
    """Base class for all Tenor based exceptions."""


class InvalidIDError(TenorException):
    """Error when the gif ID passed is not valid."""
    # error code 1


class TenorServerError(TenorException):
    """Error when a 5** status code occurs."""


class NotFound(TenorException):
    """Error when a 404 status code occurs."""
