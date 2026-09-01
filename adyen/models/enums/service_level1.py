from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceLevel1(str, Enum):
    """Specifies the service level (settlement type) of this payment method. Required for merchants operating in Japan.
    Possible values:
     * **noContract**: Adyen holds the contract with JCB.
     * **gatewayContract**: JCB receives the settlement and handles disputes, then pays out to you or your sub-merchant
            directly."""

    NO_CONTRACT = "noContract"
    GATEWAY_CONTRACT = "gatewayContract"

    __str__ = str.__str__


ServiceLevel1OrStr: TypeAlias = Annotated[ServiceLevel1 | str, open_enum_validator(ServiceLevel1)]
