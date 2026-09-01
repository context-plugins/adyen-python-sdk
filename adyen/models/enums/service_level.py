from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceLevel(str, Enum):
    """Specifies the service level (settlement type) of this payment method. Possible values:
    * **noContract**: Adyen holds the contract with American Express.
    * **gatewayContract**: American Express receives the settlement and handles disputes, then pays out to you or your
        sub-merchant directly.
    * **paymentDesignatorContract**: Adyen receives the settlement, and handles disputes and payouts."""

    NO_CONTRACT = "noContract"
    GATEWAY_CONTRACT = "gatewayContract"
    PAYMENT_DESIGNATOR_CONTRACT = "paymentDesignatorContract"

    __str__ = str.__str__


ServiceLevelOrStr: TypeAlias = Annotated[ServiceLevel | str, open_enum_validator(ServiceLevel)]
