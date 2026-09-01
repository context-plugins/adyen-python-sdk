from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LocalShopperStatement(SdkBaseModel):
    script: str
    """The character set of the local shopper statement.

    Possible values: **ja-Hani**, **ja-Kana**."""

    value: str
    """The text of the local shopper statement in the specified character set."""


class LocalShopperStatementDict(TypedDict):
    script: str
    value: str
