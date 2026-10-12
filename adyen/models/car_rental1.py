from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.rate_type import RateTypeOrStr
from .pickup_info import PickupInfo, PickupInfoDict
from .rental_surcharges import RentalSurcharges, RentalSurchargesDict
from .return_info import ReturnInfo, ReturnInfoDict


class CarRental1(SdkBaseModel):
    """`Car rental enhanced scheme data
    <https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/car-rental/>`__ that may be required for
    processing the transaction and/or for interchange savings."""

    customer_service_phone_number: Optional[str] = Field(default=UNSET, alias="customerServicePhoneNumber")
    """The customer service phone number of the car rental company.
    * Format: Alphanumeric
    * maxLength: 17
    * For US and CA numbers must be 10 characters in length
    * Must not contain any special characters such as + or -
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``carRental.customerServiceTollFreeNumber``"""

    no_show: Optional[bool] = Field(default=UNSET, alias="noShow")
    """Indicates if the customer didn't pick up their rental car.
    * **additionalData key:** ``carRental.noShowIndicator``"""

    pickup_info: Optional[PickupInfo] = Field(default=UNSET, alias="pickupInfo")
    rate_type: Optional[RateTypeOrStr] = Field(default=UNSET, alias="rateType")
    """Indicates whether the rental rate is daily or weekly.
    * **additionalData key:** ``carRental.rateIndicator``"""

    rental_agreement_number: Optional[str] = Field(default=UNSET, alias="rentalAgreementNumber")
    """The rental agreement number for the car rental.
    * Format: ASCII
    * maxLength: 9 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``carRental.rentalAgreementNumber``"""

    rental_class_id: Optional[str] = Field(default=UNSET, alias="rentalClassId")
    """The classification of the rental car.
    * Format: Alphanumeric
    * maxLength: 4 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``carRental.rentalClassId``"""

    rental_days: Optional[int] = Field(default=UNSET, alias="rentalDays")
    """The number of days the car is rented for.
    * Format: Numeric
    * Max value: 9999
    * **additionalData key:** ``carRental.daysRented``"""

    rental_rate: Optional[int] = Field(default=UNSET, alias="rentalRate")
    """Rental rate, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000
    * Frequency of the rental rate is specified in the rateType field.
    * **additionalData key:** ``carRental.rate``"""

    rental_surcharges: Optional[RentalSurcharges] = Field(default=UNSET, alias="rentalSurcharges")
    renter_name: str = Field(alias="renterName")
    """The name of the person renting the car.
    * Format: ASCII
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``carRental.renterName``"""

    return_info: Optional[ReturnInfo] = Field(default=UNSET, alias="returnInfo")
    tax_exempt: Optional[bool] = Field(default=UNSET, alias="taxExempt")
    """Indicates if the goods or services were tax-exempt, or if tax was not collected.
    * **additionalData key:** ``carRental.taxExemptIndicator``"""


class CarRental1Dict(TypedDict):
    customer_service_phone_number: NotRequired[str]
    no_show: NotRequired[bool]
    pickup_info: NotRequired[PickupInfoDict]
    rate_type: NotRequired[RateTypeOrStr]
    rental_agreement_number: NotRequired[str]
    rental_class_id: NotRequired[str]
    rental_days: NotRequired[int]
    rental_rate: NotRequired[int]
    rental_surcharges: NotRequired[RentalSurchargesDict]
    renter_name: str
    return_info: NotRequired[ReturnInfoDict]
    tax_exempt: NotRequired[bool]
