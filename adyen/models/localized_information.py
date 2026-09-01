from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .local_shopper_statement import LocalShopperStatement, LocalShopperStatementDict


class LocalizedInformation(SdkBaseModel):
    local_shopper_statement: list[LocalShopperStatement] = Field(alias="localShopperStatement")
    """An array of local shopper statements. Card schemes use this in the bank statement.

    For Japan local shopper statements in both ja-Hani and ja-Kana are required."""


class LocalizedInformationDict(TypedDict):
    local_shopper_statement: list[LocalShopperStatement | LocalShopperStatementDict]
