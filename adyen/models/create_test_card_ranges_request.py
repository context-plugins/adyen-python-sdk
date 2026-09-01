from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .test_card_range import TestCardRange, TestCardRangeDict


class CreateTestCardRangesRequest(SdkBaseModel):
    account_code: str = Field(alias="accountCode")
    """The code of the account, for which the test card ranges should be created."""

    account_type_code: str = Field(alias="accountTypeCode")
    """The type of the account, for which the test card ranges should be created.

    Permitted values:
    * Company
    * MerchantAccount
    > These values are case-sensitive."""

    test_card_ranges: list[TestCardRange] = Field(alias="testCardRanges")
    """A list of test card ranges to create."""


class CreateTestCardRangesRequestDict(TypedDict):
    account_code: str
    account_type_code: str
    test_card_ranges: list[TestCardRange | TestCardRangeDict]
