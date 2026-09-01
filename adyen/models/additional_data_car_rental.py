from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdditionalDataCarRental(SdkBaseModel):
    car_rental_check_out_date: Optional[str] = Field(default=UNSET, alias="carRental.checkOutDate")
    """The pick-up date.
    * Date format: ``yyyyMMdd``"""

    car_rental_customer_service_toll_free_number: Optional[str] = Field(
        default=UNSET, alias="carRental.customerServiceTollFreeNumber"
    )
    """The customer service phone number of the car rental company.
    * Format: Alphanumeric
    * maxLength: 17
    * For US and CA numbers must be 10 characters in length
    * Must not start with a space
    * Must not contain any special characters such as + or -
    *Must not be all zeros."""

    car_rental_days_rented: Optional[str] = Field(default=UNSET, alias="carRental.daysRented")
    """Number of days for which the car is being rented.
    * Format: Numeric
    * maxLength: 4
    * Must not be all spaces"""

    car_rental_fuel_charges: Optional[str] = Field(default=UNSET, alias="carRental.fuelCharges")
    """Any fuel charges associated with the rental, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__.
    * Format: Numeric
    * maxLength: 12"""

    car_rental_insurance_charges: Optional[str] = Field(default=UNSET, alias="carRental.insuranceCharges")
    """Any insurance charges associated with the rental, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__.
    * Format: Numeric
    * maxLength: 12
    * Must not be all spaces
    *Must not be all zeros."""

    car_rental_location_city: Optional[str] = Field(default=UNSET, alias="carRental.locationCity")
    """The city where the car is rented.
    * Format: Alphanumeric
    * maxLength: 18
    * Must not start with a space or be all spaces
    *Must not be all zeros."""

    car_rental_location_country: Optional[str] = Field(default=UNSET, alias="carRental.locationCountry")
    """The country where the car is rented, in `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__
    format.
    * Format: Alphanumeric
    * maxLength: 2"""

    car_rental_location_state_province: Optional[str] = Field(default=UNSET, alias="carRental.locationStateProvince")
    """The state or province where the car is rented.
    * Format: Alphanumeric
    * maxLength: 2
    * Must not start with a space or be all spaces
    *Must not be all zeros."""

    car_rental_no_show_indicator: Optional[str] = Field(default=UNSET, alias="carRental.noShowIndicator")
    """Indicates if the customer didn't pick up their rental car.
    * Y - Customer did not pick up their car
    * N - Not applicable"""

    car_rental_one_way_drop_off_charges: Optional[str] = Field(default=UNSET, alias="carRental.oneWayDropOffCharges")
    """The charge for not returning a car to the original rental location, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__.
    * maxLength: 12"""

    car_rental_rate: Optional[str] = Field(default=UNSET, alias="carRental.rate")
    """The daily rental rate, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * Format: Alphanumeric
    * maxLength: 12"""

    car_rental_rate_indicator: Optional[str] = Field(default=UNSET, alias="carRental.rateIndicator")
    """Specifies whether the given rate is applied daily or weekly.
    * D - Daily rate
    * W - Weekly rate"""

    car_rental_rental_agreement_number: Optional[str] = Field(default=UNSET, alias="carRental.rentalAgreementNumber")
    """The rental agreement number for the car rental.
    * Format: Alphanumeric
    * maxLength: 9
    * Must not start with a space or be all spaces
    *Must not be all zeros."""

    car_rental_rental_class_id: Optional[str] = Field(default=UNSET, alias="carRental.rentalClassId")
    """The classification of the rental car.
    * Format: Alphanumeric
    * maxLength: 4
    * Must not start with a space or be all spaces
    *Must not be all zeros."""

    car_rental_renter_name: Optional[str] = Field(default=UNSET, alias="carRental.renterName")
    """The name of the person renting the car.
    * Format: Alphanumeric
    * maxLength: 26
    * If you send more than 26 characters, the name is truncated
    * Must not start with a space or be all spaces
    *Must not be all zeros."""

    car_rental_return_city: Optional[str] = Field(default=UNSET, alias="carRental.returnCity")
    """The city where the car must be returned.
    * Format: Alphanumeric
    * maxLength: 18
    * Must not start with a space or be all spaces
    *Must not be all zeros."""

    car_rental_return_country: Optional[str] = Field(default=UNSET, alias="carRental.returnCountry")
    """The country where the car must be returned, in `ISO 3166-1 alpha-2
    <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ format.
    * Format: Alphanumeric
    * maxLength: 2"""

    car_rental_return_date: Optional[str] = Field(default=UNSET, alias="carRental.returnDate")
    """The last date to return the car by.
    * Date format: ``yyyyMMdd``
    * maxLength: 8"""

    car_rental_return_location_id: Optional[str] = Field(default=UNSET, alias="carRental.returnLocationId")
    """The agency code, phone number, or address abbreviation
    * Format: Alphanumeric
    * maxLength: 10
    * Must not start with a space or be all spaces
    *Must not be all zeros."""

    car_rental_return_state_province: Optional[str] = Field(default=UNSET, alias="carRental.returnStateProvince")
    """The state or province where the car must be returned.
    * Format: Alphanumeric
    * maxLength: 3
    * Must not start with a space or be all spaces
    *Must not be all zeros."""

    car_rental_tax_exempt_indicator: Optional[str] = Field(default=UNSET, alias="carRental.taxExemptIndicator")
    """Indicates if the goods or services were tax-exempt, or if tax was not paid on them.

    Values:
    * Y - Goods or services were tax exempt
    * N - Tax was not collected"""

    travel_entertainment_auth_data_duration: Optional[str] = Field(
        default=UNSET, alias="travelEntertainmentAuthData.duration"
    )
    """Number of days the car is rented for. This should be included in the auth message.
    * Format: Numeric
    * maxLength: 4"""

    travel_entertainment_auth_data_market: Optional[str] = Field(
        default=UNSET, alias="travelEntertainmentAuthData.market"
    )
    """Indicates what market-specific dataset will be submitted or is being submitted. Value should be 'A' for car
    rental. This should be included in the auth message.
    * Format: Alphanumeric
    * maxLength: 1"""


class AdditionalDataCarRentalDict(TypedDict):
    car_rental_check_out_date: NotRequired[str]
    car_rental_customer_service_toll_free_number: NotRequired[str]
    car_rental_days_rented: NotRequired[str]
    car_rental_fuel_charges: NotRequired[str]
    car_rental_insurance_charges: NotRequired[str]
    car_rental_location_city: NotRequired[str]
    car_rental_location_country: NotRequired[str]
    car_rental_location_state_province: NotRequired[str]
    car_rental_no_show_indicator: NotRequired[str]
    car_rental_one_way_drop_off_charges: NotRequired[str]
    car_rental_rate: NotRequired[str]
    car_rental_rate_indicator: NotRequired[str]
    car_rental_rental_agreement_number: NotRequired[str]
    car_rental_rental_class_id: NotRequired[str]
    car_rental_renter_name: NotRequired[str]
    car_rental_return_city: NotRequired[str]
    car_rental_return_country: NotRequired[str]
    car_rental_return_date: NotRequired[str]
    car_rental_return_location_id: NotRequired[str]
    car_rental_return_state_province: NotRequired[str]
    car_rental_tax_exempt_indicator: NotRequired[str]
    travel_entertainment_auth_data_duration: NotRequired[str]
    travel_entertainment_auth_data_market: NotRequired[str]
