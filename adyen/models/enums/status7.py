from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status7(str, Enum):
    """The status of the app. Possible values:
    * ``processing``: the app is being signed and converted to a format that the terminal can handle.
    * ``error``: something went wrong. Check that the app matches the `requirements
        <https://docs.adyen.com/point-of-sale/android-terminals/app-requirements>`__.
    * ``invalid``: there is something wrong with the APK file of the app.
    * ``ready``: the app has been signed and converted.
    * ``archived``: the app is no longer available."""

    ARCHIVED = "archived"
    ERROR = "error"
    INVALID = "invalid"
    PROCESSING = "processing"
    READY = "ready"

    __str__ = str.__str__


Status7OrStr: TypeAlias = Annotated[Status7 | str, open_enum_validator(Status7)]
