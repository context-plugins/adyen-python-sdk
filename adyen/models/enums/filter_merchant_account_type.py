from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FilterMerchantAccountType(str, Enum):
    """Shows how merchant accounts are filtered when configuring the webhook.

    Possible values:
    * **allAccounts** : Includes all merchant accounts, and does not require specifying ``filterMerchantAccounts``.
    * **includeAccounts** : The webhook is configured for the merchant accounts listed in ``filterMerchantAccounts``.
    * **excludeAccounts** : The webhook is not configured for the merchant accounts listed in
        ``filterMerchantAccounts``."""

    ALL_ACCOUNTS = "allAccounts"
    EXCLUDE_ACCOUNTS = "excludeAccounts"
    INCLUDE_ACCOUNTS = "includeAccounts"

    __str__ = str.__str__


FilterMerchantAccountTypeOrStr: TypeAlias = Annotated[
    FilterMerchantAccountType | str, open_enum_validator(FilterMerchantAccountType)
]
