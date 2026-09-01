from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ResponseAdditionalDataInstallments(SdkBaseModel):
    installment_payment_data_installment_type: Optional[str] = Field(
        default=UNSET, alias="installmentPaymentData.installmentType"
    )
    """Type of installment. The value of ``installmentType`` should be **IssuerFinanced**."""

    installment_payment_data_option_item_nr_annual_percentage_rate: Optional[str] = Field(
        default=UNSET, alias="installmentPaymentData.option[itemNr].annualPercentageRate"
    )
    """Annual interest rate."""

    installment_payment_data_option_item_nr_first_installment_amount: Optional[str] = Field(
        default=UNSET, alias="installmentPaymentData.option[itemNr].firstInstallmentAmount"
    )
    """First Installment Amount in minor units."""

    installment_payment_data_option_item_nr_installment_fee: Optional[str] = Field(
        default=UNSET, alias="installmentPaymentData.option[itemNr].installmentFee"
    )
    """Installment fee amount in minor units."""

    installment_payment_data_option_item_nr_interest_rate: Optional[str] = Field(
        default=UNSET, alias="installmentPaymentData.option[itemNr].interestRate"
    )
    """Interest rate for the installment period."""

    installment_payment_data_option_item_nr_maximum_number_of_installments: Optional[str] = Field(
        default=UNSET, alias="installmentPaymentData.option[itemNr].maximumNumberOfInstallments"
    )
    """Maximum number of installments possible for this payment."""

    installment_payment_data_option_item_nr_minimum_number_of_installments: Optional[str] = Field(
        default=UNSET, alias="installmentPaymentData.option[itemNr].minimumNumberOfInstallments"
    )
    """Minimum number of installments possible for this payment."""

    installment_payment_data_option_item_nr_number_of_installments: Optional[str] = Field(
        default=UNSET, alias="installmentPaymentData.option[itemNr].numberOfInstallments"
    )
    """Total number of installments possible for this payment."""

    installment_payment_data_option_item_nr_subsequent_installment_amount: Optional[str] = Field(
        default=UNSET, alias="installmentPaymentData.option[itemNr].subsequentInstallmentAmount"
    )
    """Subsequent Installment Amount in minor units."""

    installment_payment_data_option_item_nr_total_amount_due: Optional[str] = Field(
        default=UNSET, alias="installmentPaymentData.option[itemNr].totalAmountDue"
    )
    """Total amount in minor units."""

    installment_payment_data_payment_options: Optional[str] = Field(
        default=UNSET, alias="installmentPaymentData.paymentOptions"
    )
    """Possible values:
    * PayInInstallmentsOnly
    * PayInFullOnly
    * PayInFullOrInstallments"""

    installments_value: Optional[str] = Field(default=UNSET, alias="installments.value")
    """The number of installments that the payment amount should be charged with.

    Example: 5
    > Only relevant for card payments in countries that support installments."""


class ResponseAdditionalDataInstallmentsDict(TypedDict):
    installment_payment_data_installment_type: NotRequired[str]
    installment_payment_data_option_item_nr_annual_percentage_rate: NotRequired[str]
    installment_payment_data_option_item_nr_first_installment_amount: NotRequired[str]
    installment_payment_data_option_item_nr_installment_fee: NotRequired[str]
    installment_payment_data_option_item_nr_interest_rate: NotRequired[str]
    installment_payment_data_option_item_nr_maximum_number_of_installments: NotRequired[str]
    installment_payment_data_option_item_nr_minimum_number_of_installments: NotRequired[str]
    installment_payment_data_option_item_nr_number_of_installments: NotRequired[str]
    installment_payment_data_option_item_nr_subsequent_installment_amount: NotRequired[str]
    installment_payment_data_option_item_nr_total_amount_due: NotRequired[str]
    installment_payment_data_payment_options: NotRequired[str]
    installments_value: NotRequired[str]
