from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status41(str, Enum):
    """The status of the store. Possible values are:

    - **active**: This value is assigned automatically when a store is created.
    - **inactive**: The maximum `transaction limits and number of Store-and-Forward transactions
        <https://docs.adyen.com/point-of-sale/determine-account-structure/configure-features#payment-features>`__ for
        the store are set to 0. This blocks new transactions, but captures are still possible.
    - **closed**: The terminals of the store are reassigned to the merchant inventory, so they can't process payments.

    You can change the status from **active** to **inactive**, and from **inactive** to **active** or **closed**. Once
    **closed**, a store can't be reopened."""

    ACTIVE = "active"
    CLOSED = "closed"
    INACTIVE = "inactive"

    __str__ = str.__str__


Status41OrStr: TypeAlias = Annotated[Status41 | str, open_enum_validator(Status41)]
