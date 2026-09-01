from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type11(str, Enum):
    """The part of the payment you want to book to the specified ``account``.

    Possible values for the `Balance Platform <https://docs.adyen.com/adyen-for-platforms-model>`__:
    * **BalanceAccount**: Books part of the payment (specified in ``amount``) to the specified ``account``.
    * Transaction fees types that you can book to the specified ``account``:
       * **AcquiringFees**: The aggregated amount of the interchange and scheme fees.
       * **PaymentFee**: The aggregated amount of all transaction fees.
       * **AdyenFees**: The aggregated amount of Adyen's commission and markup fees.
       * **AdyenCommission**: The transaction fees due to Adyen under `blended rates
            <https://www.adyen.com/knowledge-hub/interchange-fees-explained>`__.
       * **AdyenMarkup**: The transaction fees due to Adyen under `Interchange ++ pricing
            <https://www.adyen.com/knowledge-hub/interchange-fees-explained>`__.
       * **Interchange**: The fees paid to the issuer for each payment made with the card network.
       * **SchemeFee**: The fees paid to the card scheme for using their network.
    * **Commission**: Your platform's commission on the payment (specified in ``amount``), booked to your liable balance
        account.
    * **Remainder**: The amount left over after a currency conversion, booked to the specified ``account``.
    * **Surcharge**: The payment acceptance fee imposed by the card scheme or debit network provider, paid by your
        user's customer.
    * **TopUp**: Allows you and your users to top up balance accounts using direct debit, card payments, or other
        payment methods.
    * **VAT**: The value-added tax charged on the payment, booked to your platforms liable balance account.
    * **Default**: In very specific use cases, allows you to book the specified ``amount`` to the specified ``account``.
        For more information, contact Adyen support.

    Possible values for the `Classic Platforms integration <https://docs.adyen.com/classic-platforms>`__:
    **Commission**, **Default**, **MarketPlace**, **PaymentFee**, **VAT**."""

    ACQUIRING_FEES = "AcquiringFees"
    ADYEN_COMMISSION = "AdyenCommission"
    ADYEN_FEES = "AdyenFees"
    ADYEN_MARKUP = "AdyenMarkup"
    BALANCE_ACCOUNT = "BalanceAccount"
    COMMISSION = "Commission"
    DEFAULT = "Default"
    INTERCHANGE = "Interchange"
    MARKET_PLACE = "MarketPlace"
    PAYMENT_FEE = "PaymentFee"
    REMAINDER = "Remainder"
    SCHEME_FEE = "SchemeFee"
    SURCHARGE = "Surcharge"
    TIP = "Tip"
    TOP_UP = "TopUp"
    VAT = "VAT"

    __str__ = str.__str__


Type11OrStr: TypeAlias = Annotated[Type11 | str, open_enum_validator(Type11)]
