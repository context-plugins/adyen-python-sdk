from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RentalSurcharges(SdkBaseModel):
    fuel: Optional[int] = UNSET
    """The fuel charges associated with the rental, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000
    * **additionalData key:** ``carRental.fuelCharges``"""

    insurance: Optional[int] = UNSET
    """Any insurance charges associated with the rental, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000
    * **additionalData key:** ``carRental.insuranceCharges``"""

    one_way_drop_off: Optional[int] = Field(default=UNSET, alias="oneWayDropOff")
    """The charge for not returning a car to the original rental location, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000
    * **additionalData key:** ``carRental.oneWayDropOffCharges``"""


class RentalSurchargesDict(TypedDict):
    fuel: NotRequired[int]
    insurance: NotRequired[int]
    one_way_drop_off: NotRequired[int]
