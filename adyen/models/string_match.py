from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.operation import OperationOrStr


class StringMatch(SdkBaseModel):
    operation: Optional[OperationOrStr] = UNSET
    """The type of string matching operation. Possible values: **startsWith**, **endsWith**, **isEqualTo**,
    **contains**,"""

    value: Optional[str] = UNSET
    """The string to be matched."""


class StringMatchDict(TypedDict):
    operation: NotRequired[OperationOrStr]
    value: NotRequired[str]
