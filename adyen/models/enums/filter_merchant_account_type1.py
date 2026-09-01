from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FilterMerchantAccountType1(str, Enum):
    """Shows how merchant accounts are included in company-level webhooks. Possible values:
    * **includeAccounts**
    * **excludeAccounts**
    * **allAccounts**: Includes all merchant accounts, and does not require specifying ``filterMerchantAccounts``."""

    ALL_ACCOUNTS = "allAccounts"
    EXCLUDE_ACCOUNTS = "excludeAccounts"
    INCLUDE_ACCOUNTS = "includeAccounts"

    __str__ = str.__str__


FilterMerchantAccountType1OrStr: TypeAlias = Annotated[
    FilterMerchantAccountType1 | str, open_enum_validator(FilterMerchantAccountType1)
]
