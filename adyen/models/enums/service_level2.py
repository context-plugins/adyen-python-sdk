from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceLevel2(str, Enum):
    """Specifies the service level (settlement type) of this payment method. Required for merchants operating in Japan.
    Possible values:
    * **noContract**: Adyen holds the contract with JCB for merchants operating in Japan or American Express for
        merchants operating in Canada, Australia and New Zealand.
    * **gatewayContract**: JCB or American Express receives the settlement and handles disputes, then pays out to you or
        your sub-merchant directly.
    * **paymentDesignatorContract**: Available only for merchants operating in Canada, Australia and New Zealand. Adyen
        receives the settlement, and handles disputes and payouts."""

    NO_CONTRACT = "noContract"
    GATEWAY_CONTRACT = "gatewayContract"
    PAYMENT_DESIGNATOR_CONTRACT = "paymentDesignatorContract"

    __str__ = str.__str__


ServiceLevel2OrStr: TypeAlias = Annotated[ServiceLevel2 | str, open_enum_validator(ServiceLevel2)]
