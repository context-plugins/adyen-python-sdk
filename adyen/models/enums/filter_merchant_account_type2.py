from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FilterMerchantAccountType2(str, Enum):
    """Shows how merchant accounts are filtered when configuring the webhook. Possible values:
    * **includeAccounts**: The webhook is configured for the merchant accounts listed in ``filterMerchantAccounts``.
    * **excludeAccounts**: The webhook is not configured for the merchant accounts listed in ``filterMerchantAccounts``.
    * **allAccounts**: Includes all merchant accounts, and does not require specifying ``filterMerchantAccounts``."""

    ALL_ACCOUNTS = "allAccounts"
    EXCLUDE_ACCOUNTS = "excludeAccounts"
    INCLUDE_ACCOUNTS = "includeAccounts"

    __str__ = str.__str__


FilterMerchantAccountType2OrStr: TypeAlias = Annotated[
    FilterMerchantAccountType2 | str, open_enum_validator(FilterMerchantAccountType2)
]
