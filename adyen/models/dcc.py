from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Dcc(SdkBaseModel):
    enable_dcc: Optional[bool] = Field(default=UNSET, alias="enableDcc")
    """Enable Dynamic Currency Conversion (DCC). When you enable DCC, you are responsible for complying with `DCC
    receipt requirements and terms of use
    <https://help.adyen.com/en_US/knowledge/in-person-payments/terminal-features/dynamic-currency-conversion-dcc-rules-regulations>`__."""


class DccDict(TypedDict):
    enable_dcc: NotRequired[bool]
