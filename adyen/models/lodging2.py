from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .enums.lodging_charge_type import LodgingChargeTypeOrStr
from .folio2 import Folio2, Folio2Dict
from .room import Room, RoomDict


class Lodging2(SdkBaseModel):
    """`Lodging enhanced scheme data <https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/lodging/>`__
    that may be required for processing the transaction and/or for interchange savings."""

    check_in_date: Optional[Date] = Field(default=UNSET, alias="checkInDate")
    """The check-in date.
    * Min Length: 10 characters
    * Max Length: 10 characters
    * Format `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__: yyyy-MM-dd
    * **additionalData key:** ``lodging.checkInDate``"""

    check_out_date: Optional[Date] = Field(default=UNSET, alias="checkOutDate")
    """The check-out date.
    * Min Length: 10 characters
    * Max Length: 10 characters
    * Format `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__: yyyy-MM-dd
    * **additionalData key:** ``lodging.checkOutDate``"""

    customer_service_phone_number: Optional[str] = Field(default=UNSET, alias="customerServicePhoneNumber")
    """The toll-free phone number for the lodging customer service.
    * Format: Alphanumeric
    * For US and CA numbers must be 10 characters in length
    * Must not start with a space
    * Must not contain any special characters such as + or -
    * Must not be all zeros.
    * **additionalData key:** ``lodging.customerServiceTollFreeNumber``"""

    fire_safety_compliance: Optional[bool] = Field(default=UNSET, alias="fireSafetyCompliance")
    """Indicates that the facility complies with the Hotel and Motel Fire Safety Act of 1990.
    * **additionalData key:** ``lodging.fireSafetyActIndicator``"""

    folio: Optional[Folio2] = UNSET
    """The folio information for the booking."""

    food_beverage_charges: Optional[int] = Field(default=UNSET, alias="foodBeverageCharges")
    """Any charges for food and beverages associated with the booking, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000
    * **additionalData key:** ``lodging.foodBeverageCharges``"""

    lodging_charge_type: Optional[LodgingChargeTypeOrStr] = Field(default=UNSET, alias="lodgingChargeType")
    """The category of lodging charges for the payment.
    * **additionalData key:** ``lodging.specialProgramCode``"""

    no_show: Optional[bool] = Field(default=UNSET, alias="noShow")
    """Indicates if the customer didn't check in for their booking.
    * **additionalData key:** ``lodging.noShowIndicator``"""

    prepaid_expenses: Optional[int] = Field(default=UNSET, alias="prepaidExpenses")
    """The prepaid expenses for the booking, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000
    * **additionalData key:** ``lodging.prepaidExpenses``"""

    property_phone_number: Optional[str] = Field(default=UNSET, alias="propertyPhoneNumber")
    """The lodging property location's phone number.
    * Format: Alphanumeric
    * Min length: 10 characters
    * For US and CA numbers must be 10 characters in length
    * Must not start with a space
    * Must not contain any special characters such as + or -
    * Must not be all zeros.
    * **additionalData key:** ``lodging.propertyPhoneNumber``"""

    renter_name: Optional[str] = Field(default=UNSET, alias="renterName")
    """The name of the person renting the room.
    * Format: ASCII
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``lodging.renterName``"""

    rooms: Optional[list[Room]] = UNSET
    """The list of rooms booked."""

    total_room_tax: Optional[int] = Field(default=UNSET, alias="totalRoomTax")
    """The total room tax amount, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000
    * **additionalData key:** ``lodging.totalRoomTax``"""

    total_tax: Optional[int] = Field(default=UNSET, alias="totalTax")
    """The total tax amount, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000
    * **additionalData key:** ``lodging.totalTax``"""


class Lodging2Dict(TypedDict):
    check_in_date: NotRequired[Date]
    check_out_date: NotRequired[Date]
    customer_service_phone_number: NotRequired[str]
    fire_safety_compliance: NotRequired[bool]
    folio: NotRequired[Folio2 | Folio2Dict]
    food_beverage_charges: NotRequired[int]
    lodging_charge_type: NotRequired[LodgingChargeTypeOrStr]
    no_show: NotRequired[bool]
    prepaid_expenses: NotRequired[int]
    property_phone_number: NotRequired[str]
    renter_name: NotRequired[str]
    rooms: NotRequired[list[Room | RoomDict]]
    total_room_tax: NotRequired[int]
    total_tax: NotRequired[int]
