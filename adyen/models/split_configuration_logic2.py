from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .additional_commission1 import AdditionalCommission1, AdditionalCommission1Dict
from .commission1 import Commission1, Commission1Dict
from .enums.acquiring_fees import AcquiringFeesOrStr
from .enums.adyen_commission import AdyenCommissionOrStr
from .enums.adyen_fees import AdyenFeesOrStr
from .enums.adyen_markup import AdyenMarkupOrStr
from .enums.behavior import BehaviorOrStr
from .enums.chargeback_cost_allocation import ChargebackCostAllocationOrStr
from .enums.interchange import InterchangeOrStr
from .enums.payment_fee import PaymentFeeOrStr
from .enums.refund_cost_allocation import RefundCostAllocationOrStr
from .enums.remainder import RemainderOrStr
from .enums.scheme_fee import SchemeFeeOrStr
from .enums.surcharge3 import Surcharge3OrStr
from .enums.tip import TipOrStr
from .split_dcc2 import SplitDcc2, SplitDcc2Dict


class SplitConfigurationLogic2(SdkBaseModel):
    """Contains the split logic that is applied if the rule conditions are met."""

    acquiring_fees: Optional[AcquiringFeesOrStr] = Field(default=UNSET, alias="acquiringFees")
    """Deducts the acquiring fees (the aggregated amount of interchange and scheme fee) from the specified balance
    account.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**."""

    additional_commission: Optional[AdditionalCommission1] = Field(default=UNSET, alias="additionalCommission")
    """Defines whether to book an additional commission for payments to your user's balance account. The commission
    amount can be defined as a fixed amount (specified in minor units), a percentage (specified in basis points), or
    both."""

    adyen_commission: Optional[AdyenCommissionOrStr] = Field(default=UNSET, alias="adyenCommission")
    """Deducts the transaction fee due to Adyen under `blended rates
    <https://www.adyen.com/knowledge-hub/guides/payments-training-guide/get-the-best-from-your-card-processing>`__ from
    the specified balance account.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**."""

    adyen_fees: Optional[AdyenFeesOrStr] = Field(default=UNSET, alias="adyenFees")
    """Deducts the fees due to Adyen (markup or commission) from the specified balance account.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**."""

    adyen_markup: Optional[AdyenMarkupOrStr] = Field(default=UNSET, alias="adyenMarkup")
    """Deducts the transaction fee due to Adyen under `Interchange ++ pricing
    <https://www.adyen.com/what-is-interchange>`__ from the specified balance account.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**."""

    chargeback: Optional[BehaviorOrStr] = UNSET
    """Specifies how and from which balance account(s) to deduct the chargeback amount.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**."""

    chargeback_cost_allocation: Optional[ChargebackCostAllocationOrStr] = Field(
        default=UNSET, alias="chargebackCostAllocation"
    )
    """Deducts the chargeback costs from the specified balance account.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**"""

    commission: Commission1
    """Defines your platform's commission for the processed payments as a fixed amount (specified in minor units), a
    percentage (specified in basis points), or both. The commission is booked to your platform's liable balance
    account."""

    dcc: Optional[SplitDcc2] = UNSET
    """Defines the logic for booking the markup paid by the customer for Dynamic Currency Conversion (DCC).

    > This field is in pilot phase, and not yet available for all platforms."""

    interchange: Optional[InterchangeOrStr] = UNSET
    """Deducts the interchange fee from specified balance account.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**."""

    payment_fee: Optional[PaymentFeeOrStr] = Field(default=UNSET, alias="paymentFee")
    """Deducts all transaction fees incurred by the payment from the specified balance account. The transaction fees
    include the acquiring fees (interchange and scheme fee), and the fees due to Adyen (markup or commission). You can
    book any and all these fees to different balance account by specifying other transaction fee parameters in your
    split configuration profile:

    -
        https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId/splitConfigurations#request-rules-splitLogic-adyenCommission):
        The transaction fee due to Adyen under `blended rates
        <https://www.adyen.com/knowledge-hub/interchange-fees-explained#interchange-vs-blended>`__.
    -
        https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId/splitConfigurations#request-rules-splitLogic-adyenMarkup):
        The transaction fee due to Adyen under `Interchange ++ pricing
        <https://www.adyen.com/knowledge-hub/interchange-fees-explained#interchange-vs-blended>`__.
    -
        https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId/splitConfigurations#request-rules-splitLogic-schemeFee):
        The fee paid to the card scheme for using their network.
    -
        https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId/splitConfigurations#request-rules-splitLogic-interchange):
        The fee paid to the issuer for each payment transaction made with the card network.
    -
        https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId/splitConfigurations#request-rules-splitLogic-adyenFees):
        The aggregated amount of Adyen's commission and markup.
    -
        https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId/splitConfigurations#request-rules-splitLogic-acquiringFees):
        The aggregated amount of the interchange and scheme fees.

    If you don't include at least one transaction fee type in the ``splitLogic`` object, Adyen updates the payment
    request with the ``paymentFee`` parameter, booking all transaction fees to your platform's liable balance account.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**."""

    refund: Optional[BehaviorOrStr] = UNSET
    """Specifies how and from which balance account(s) to deduct the refund amount.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**"""

    refund_cost_allocation: Optional[RefundCostAllocationOrStr] = Field(default=UNSET, alias="refundCostAllocation")
    """Deducts the refund costs from the specified balance account.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**"""

    remainder: Optional[RemainderOrStr] = UNSET
    """Books the amount left over after currency conversion to the specified balance account.

    Possible values: **addToLiableAccount**, **addToOneBalanceAccount**."""

    scheme_fee: Optional[SchemeFeeOrStr] = Field(default=UNSET, alias="schemeFee")
    """Deducts the scheme fee from the specified balance account.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**."""

    split_logic_id: Optional[str] = Field(default=UNSET, alias="splitLogicId")
    """Unique identifier of the collection of split instructions that are applied when the rule conditions are met."""

    surcharge: Optional[Surcharge3OrStr] = UNSET
    """Books the surcharge amount to the specified balance account.

    Possible values: **addToLiableAccount**, **addToOneBalanceAccount**"""

    tip: Optional[TipOrStr] = UNSET
    """Books the tips (gratuity) to the specified balance account.

    Possible values: **addToLiableAccount**, **addToOneBalanceAccount**."""


class SplitConfigurationLogic2Dict(TypedDict):
    acquiring_fees: NotRequired[AcquiringFeesOrStr]
    additional_commission: NotRequired[AdditionalCommission1Dict]
    adyen_commission: NotRequired[AdyenCommissionOrStr]
    adyen_fees: NotRequired[AdyenFeesOrStr]
    adyen_markup: NotRequired[AdyenMarkupOrStr]
    chargeback: NotRequired[BehaviorOrStr]
    chargeback_cost_allocation: NotRequired[ChargebackCostAllocationOrStr]
    commission: Commission1Dict
    dcc: NotRequired[SplitDcc2Dict]
    interchange: NotRequired[InterchangeOrStr]
    payment_fee: NotRequired[PaymentFeeOrStr]
    refund: NotRequired[BehaviorOrStr]
    refund_cost_allocation: NotRequired[RefundCostAllocationOrStr]
    remainder: NotRequired[RemainderOrStr]
    scheme_fee: NotRequired[SchemeFeeOrStr]
    split_logic_id: NotRequired[str]
    surcharge: NotRequired[Surcharge3OrStr]
    tip: NotRequired[TipOrStr]
