from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.platform_payment_type import PlatformPaymentTypeOrStr
from .enums.type63 import Type63, Type63OrStr


class PlatformPayment(SdkBaseModel):
    modification_merchant_reference: Optional[str] = Field(default=UNSET, alias="modificationMerchantReference")
    """The capture's merchant reference included in the transfer."""

    modification_psp_reference: Optional[str] = Field(default=UNSET, alias="modificationPspReference")
    """The capture reference included in the transfer."""

    payment_merchant_reference: Optional[str] = Field(default=UNSET, alias="paymentMerchantReference")
    """The payment's merchant reference included in the transfer."""

    platform_payment_type: Optional[PlatformPaymentTypeOrStr] = Field(default=UNSET, alias="platformPaymentType")
    """Specifies the nature of the transfer. This parameter helps categorize transfers so you can reconcile transactions
    at a later time, using the Balance Platform Accounting Report for `marketplaces
    <https://docs.adyen.com/marketplaces/reports-and-fees/balance-platform-accounting-report/>`__ or `platforms
    <https://docs.adyen.com/platforms/reports-and-fees/balance-platform-accounting-report/>`__.

    Possible values:

    * **AcquiringFees**: The acquiring fee (the aggregated amount of interchange and scheme fee) incurred on a
        transaction.

    * **AdyenCommission**: The transaction fee due to Adyen under `blended rates
        <https://www.adyen.com/knowledge-hub/guides/payments-training-guide/get-the-best-from-your-card-processing>`__.

    * **AdyenFees**: All transaction fees due to Adyen. This is the aggregated amount of Adyen's commission and markup.

    * **AdyenMarkup**: The transaction fee due to Adyen under `Interchange++ pricing <https://www.adyen.com/pricing>`__.

    * **BalanceAccount**: The amount booked to your user after the deduction of the relevant fees.

    * **Commission**: Your platform's or marketplace's commission on a transaction.

    * **DCCPlatformCommission**: **deprecated** The Dynamic Currency Conversion (DCC) fee on a transaction.

    * **DCCMarkup**: The Dynamic Currency Conversion (DCC) fee on a transaction.

    * **Interchange**: The interchange fee (fee paid to the issuer) incurred on a transaction.

    * **PaymentFee**: The aggregated amount of all transaction fees.

    * **Remainder**: The leftover amount after currency conversion.

    * **SchemeFee**: The scheme fee incurred on a transaction.

    * **Surcharge**: The surcharge paid by the customer on a transaction.

    * **Tip**: The tip paid by the customer.

    * **TopUp**: An incoming transfer to top up your user's balance account.

    * **VAT**: The value-added tax charged on the payment."""

    psp_payment_reference: Optional[str] = Field(default=UNSET, alias="pspPaymentReference")
    """The payment reference included in the transfer."""

    type_: Type63OrStr = Field(default=Type63.PLATFORM_PAYMENT, alias="type")
    """**platformPayment**"""


class PlatformPaymentDict(TypedDict):
    modification_merchant_reference: NotRequired[str]
    modification_psp_reference: NotRequired[str]
    payment_merchant_reference: NotRequired[str]
    platform_payment_type: NotRequired[PlatformPaymentTypeOrStr]
    psp_payment_reference: NotRequired[str]
    type_: NotRequired[Type63OrStr]
