from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IndustryUsage(str, Enum):
    """In case of `asynchronous authorisation adjustment
    <https://docs.adyen.com/online-payments/adjust-authorisation#adjust-authorisation>`__, this field denotes why the
    additional payment is made.

    Possible values:

     * **NoShow**: An incremental charge is carried out because of a no-show for a guaranteed reservation.

     * **DelayedCharge**: An incremental charge is carried out to process an additional payment after the original
            services have been rendered and the respective payment has been processed."""

    NO_SHOW = "NoShow"
    DELAYED_CHARGE = "DelayedCharge"

    __str__ = str.__str__


IndustryUsageOrStr: TypeAlias = Annotated[IndustryUsage | str, open_enum_validator(IndustryUsage)]
