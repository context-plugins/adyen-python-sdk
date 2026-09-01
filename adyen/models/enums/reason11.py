from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Reason11(str, Enum):
    """The reason why the transfer failed Adyen's internal review.

    Possible values:

    - **refusedForRegulatoryReasons**: the transfer does not comply with Adyen's risk policy. For more information,
        `contact the Support Team <https://www.adyen.help/hc/en-us/requests/new>`__."""

    REFUSED_FOR_REGULATORY_REASONS = "refusedForRegulatoryReasons"

    __str__ = str.__str__


Reason11OrStr: TypeAlias = Annotated[Reason11 | str, open_enum_validator(Reason11)]
