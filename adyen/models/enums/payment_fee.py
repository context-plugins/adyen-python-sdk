from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentFee(str, Enum):
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

    DEDUCT_FROM_LIABLE_ACCOUNT = "deductFromLiableAccount"
    DEDUCT_FROM_ONE_BALANCE_ACCOUNT = "deductFromOneBalanceAccount"

    __str__ = str.__str__


PaymentFeeOrStr: TypeAlias = Annotated[PaymentFee | str, open_enum_validator(PaymentFee)]
