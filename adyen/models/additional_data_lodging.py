from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdditionalDataLodging(SdkBaseModel):
    lodging_special_program_code: Optional[str] = Field(default=UNSET, alias="lodging.SpecialProgramCode")
    """A code that corresponds to the category of lodging charges for the payment. Possible values:
    * 1: Lodging
    * 2: No show reservation
    * 3: Advanced deposit"""

    lodging_check_in_date: Optional[str] = Field(default=UNSET, alias="lodging.checkInDate")
    """The arrival date.
    * Date format: **yyyyMmDd**. For example, for 2023 April 22, **20230422**."""

    lodging_check_out_date: Optional[str] = Field(default=UNSET, alias="lodging.checkOutDate")
    """The departure date.
    * Date format: **yyyyMmDd**. For example, for 2023 April 22, **20230422**."""

    lodging_customer_service_toll_free_number: Optional[str] = Field(
        default=UNSET, alias="lodging.customerServiceTollFreeNumber"
    )
    """The toll-free phone number for the lodging.
    * Format: numeric
    * Max length: 17 characters.
    * For US and CA numbers must be 10 characters in length
    * Must not start with a space
    * Must not contain any special characters such as + or -
    * Must not be all zeros."""

    lodging_fire_safety_act_indicator: Optional[str] = Field(default=UNSET, alias="lodging.fireSafetyActIndicator")
    """Identifies that the facility complies with the Hotel and Motel Fire Safety Act of 1990. Must be 'Y' or 'N'.
    * Format: alphabetic
    * Max length: 1 character"""

    lodging_folio_cash_advances: Optional[str] = Field(default=UNSET, alias="lodging.folioCashAdvances")
    """The folio cash advances, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * Format: numeric
    * Max length: 12 characters"""

    lodging_folio_number: Optional[str] = Field(default=UNSET, alias="lodging.folioNumber")
    """The card acceptor’s internal invoice or billing ID reference number.
    * Max length: 25 characters
    * Must not start with a space
    * Must not contain any special characters
    * Must not be all zeros."""

    lodging_food_beverage_charges: Optional[str] = Field(default=UNSET, alias="lodging.foodBeverageCharges")
    """Any charges for food and beverages associated with the booking, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__.
    * Format: numeric
    * Max length: 12 characters"""

    lodging_no_show_indicator: Optional[str] = Field(default=UNSET, alias="lodging.noShowIndicator")
    """Indicates if the customer didn't check in for their booking.
     Possible values:
    * **Y**: the customer didn't check in
    * **N**: the customer checked in"""

    lodging_prepaid_expenses: Optional[str] = Field(default=UNSET, alias="lodging.prepaidExpenses")
    """The prepaid expenses for the booking.
    * Format: numeric
    * Max length: 12 characters"""

    lodging_property_phone_number: Optional[str] = Field(default=UNSET, alias="lodging.propertyPhoneNumber")
    """The lodging property location's phone number.
    * Format: numeric
    * Min length: 10 characters
    * Max length: 17 characters
    * For US and CA numbers must be 10 characters in length
    * Must not start with a space
    * Must not contain any special characters such as + or -
    * Must not be all zeros."""

    lodging_room1_number_of_nights: Optional[str] = Field(default=UNSET, alias="lodging.room1.numberOfNights")
    """The total number of nights the room is booked for.
    * Format: numeric
    * Must be a number between 0 and 99
    * Max length: 4 characters"""

    lodging_room1_rate: Optional[str] = Field(default=UNSET, alias="lodging.room1.rate")
    """The rate for the room, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * Format: numeric
    * Max length: 12 characters
    * Must not be a negative number"""

    lodging_total_room_tax: Optional[str] = Field(default=UNSET, alias="lodging.totalRoomTax")
    """The total room tax amount, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * Format: numeric
    * Max length: 12 characters
    * Must not be a negative number"""

    lodging_total_tax: Optional[str] = Field(default=UNSET, alias="lodging.totalTax")
    """The total tax amount, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * Format: numeric
    * Max length: 12 characters
    * Must not be a negative number"""

    travel_entertainment_auth_data_duration: Optional[str] = Field(
        default=UNSET, alias="travelEntertainmentAuthData.duration"
    )
    """The number of nights. This should be included in the auth message.
    * Format: numeric
    * Max length: 4 characters"""

    travel_entertainment_auth_data_market: Optional[str] = Field(
        default=UNSET, alias="travelEntertainmentAuthData.market"
    )
    """Indicates what market-specific dataset will be submitted. Must be 'H' for Hotel. This should be included in the
    auth message.

    * Format: alphanumeric
    * Max length: 1 character"""


class AdditionalDataLodgingDict(TypedDict):
    lodging_special_program_code: NotRequired[str]
    lodging_check_in_date: NotRequired[str]
    lodging_check_out_date: NotRequired[str]
    lodging_customer_service_toll_free_number: NotRequired[str]
    lodging_fire_safety_act_indicator: NotRequired[str]
    lodging_folio_cash_advances: NotRequired[str]
    lodging_folio_number: NotRequired[str]
    lodging_food_beverage_charges: NotRequired[str]
    lodging_no_show_indicator: NotRequired[str]
    lodging_prepaid_expenses: NotRequired[str]
    lodging_property_phone_number: NotRequired[str]
    lodging_room1_number_of_nights: NotRequired[str]
    lodging_room1_rate: NotRequired[str]
    lodging_total_room_tax: NotRequired[str]
    lodging_total_tax: NotRequired[str]
    travel_entertainment_auth_data_duration: NotRequired[str]
    travel_entertainment_auth_data_market: NotRequired[str]
