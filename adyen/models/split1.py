from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type60 import Type60OrStr
from .split_amount import SplitAmount, SplitAmountDict


class Split1(SdkBaseModel):
    account: Optional[str] = UNSET
    """The unique identifier of the account to which the split amount is booked. Required if ``type`` is **MarketPlace**
    or **BalanceAccount**.

    * `Classic Platforms integration <https://docs.adyen.com/classic-platforms>`__: The
        https://docs.adyen.com/api-explorer/Account/latest/post/updateAccount#request-accountCode of the account to
        which the split amount is booked.
    * `Balance Platform <https://docs.adyen.com/adyen-for-platforms-model>`__: The
        https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/_id_#path-id of the account to
        which the split amount is booked."""

    amount: Optional[SplitAmount] = UNSET
    """The amount of the split item.

    * Required for all split types in the `Classic Platforms integration <https://docs.adyen.com/classic-platforms>`__.
    * Required if ``type`` is **BalanceAccount**, **Commission**, **Default**, or **VAT** in your `Balance Platform
        <https://docs.adyen.com/adyen-for-platforms-model>`__ integration."""

    description: Optional[str] = UNSET
    """Your description for the split item."""

    reference: Optional[str] = UNSET
    """Your unique reference for the part of the payment booked to the specified ``account``.

    This is required if ``type`` is **MarketPlace** (`Classic Platforms integration
    <https://docs.adyen.com/classic-platforms>`__) or **BalanceAccount** (`Balance Platform
    <https://docs.adyen.com/adyen-for-platforms-model>`__).

    For the other types, we also recommend providing a **unique** reference so you can reconcile the split and the
    associated payment in the transaction overview and in the reports."""

    type_: Type60OrStr = Field(alias="type")
    """The part of the payment you want to book to the specified ``account``.

    Possible values for the `Balance Platform <https://docs.adyen.com/adyen-for-platforms-model>`__:
    * **BalanceAccount**: books part of the payment (specified in ``amount``) to the specified ``account``.
    * Transaction fees types that you can book to the specified ``account``:
       * **AcquiringFees**: the aggregated amount of the interchange and scheme fees.
       * **PaymentFee**: the aggregated amount of all transaction fees.
       * **AdyenFees**: the aggregated amount of Adyen's commission and markup fees.
       * **AdyenCommission**: the transaction fees due to Adyen under `blended rates
            <https://www.adyen.com/knowledge-hub/interchange-fees-explained>`__.
       * **AdyenMarkup**: the transaction fees due to Adyen under `Interchange ++ pricing
            <https://www.adyen.com/knowledge-hub/interchange-fees-explained>`__.
       * **Interchange**: the fees paid to the issuer for each payment made with the card network.
       * **SchemeFee**: the fees paid to the card scheme for using their network.
    * **Commission**: your platform's commission on the payment (specified in ``amount``), booked to your liable balance
        account.
    * **Remainder**: the amount left over after a currency conversion, booked to the specified ``account``.
    * **TopUp**: allows you and your users to top up balance accounts using direct debit, card payments, or other
        payment methods.
    * **VAT**: the value-added tax charged on the payment, booked to your platforms liable balance account.
    * **Commission**: your platform's commission (specified in ``amount``) on the payment, booked to your liable balance
        account.
    * **Default**: in very specific use cases, allows you to book the specified ``amount`` to the specified ``account``.
        For more information, contact Adyen support.

    Possible values for the `Classic Platforms integration <https://docs.adyen.com/classic-platforms>`__:
    **Commission**, **Default**, **Marketplace**, **PaymentFee**, **VAT**."""


class Split1Dict(TypedDict):
    account: NotRequired[str]
    amount: NotRequired[SplitAmountDict]
    description: NotRequired[str]
    reference: NotRequired[str]
    type_: Type60OrStr
