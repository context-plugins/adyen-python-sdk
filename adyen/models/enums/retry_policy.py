from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RetryPolicy(str, Enum):
    """When set to true, you can retry for failed recurring payments. The default value is true."""

    TRUE = "true"
    FALSE = "false"

    __str__ = str.__str__


RetryPolicyOrStr: TypeAlias = Annotated[RetryPolicy | str, open_enum_validator(RetryPolicy)]
