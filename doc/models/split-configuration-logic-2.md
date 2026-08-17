
# Split Configuration Logic 2

Contains the split logic that is applied if the rule conditions are met.

## Structure

`SplitConfigurationLogic2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acquiring_fees` | [`AcquiringFeesEnum`](../../doc/models/acquiring-fees-enum.md) | Optional | Deducts the acquiring fees (the aggregated amount of interchange and scheme fee) from the specified balance account.<br><br>Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
| `additional_commission` | [`AdditionalCommission1`](../../doc/models/additional-commission-1.md) | Optional | Defines whether to book an additional commission for payments to your user's balance account. The commission amount can be defined as a fixed amount (specified in minor units), a percentage (specified in basis points), or both. |
| `adyen_commission` | [`AdyenCommissionEnum`](../../doc/models/adyen-commission-enum.md) | Optional | Deducts the transaction fee due to Adyen under [blended rates](https://www.adyen.com/knowledge-hub/guides/payments-training-guide/get-the-best-from-your-card-processing) from the specified balance account.<br><br>Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
| `adyen_fees` | [`AdyenFeesEnum`](../../doc/models/adyen-fees-enum.md) | Optional | Deducts the fees due to Adyen (markup or commission) from the specified balance account.<br><br>Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
| `adyen_markup` | [`AdyenMarkupEnum`](../../doc/models/adyen-markup-enum.md) | Optional | Deducts the transaction fee due to Adyen under [Interchange ++ pricing](https://www.adyen.com/what-is-interchange) from the specified balance account.<br><br>Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
| `chargeback` | [`BehaviorEnum`](../../doc/models/behavior-enum.md) | Optional | Specifies how and from which balance account(s) to deduct the chargeback amount.<br><br>Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**. |
| `chargeback_cost_allocation` | [`ChargebackCostAllocationEnum`](../../doc/models/chargeback-cost-allocation-enum.md) | Optional | Deducts the chargeback costs from the specified balance account.<br><br>Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount** |
| `commission` | [`Commission1`](../../doc/models/commission-1.md) | Required | Defines your platform's commission for the processed payments as a fixed amount (specified in minor units), a percentage (specified in basis points), or both. The commission is booked to your platform's liable balance account. |
| `dcc` | [`SplitDcc2`](../../doc/models/split-dcc-2.md) | Optional | Defines the logic for booking the markup paid by the customer for Dynamic Currency Conversion (DCC).<br><br>> This field is in pilot phase, and not yet available for all platforms. |
| `interchange` | [`InterchangeEnum`](../../doc/models/interchange-enum.md) | Optional | Deducts the interchange fee from specified balance account.<br><br>Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
| `payment_fee` | [`PaymentFeeEnum`](../../doc/models/payment-fee-enum.md) | Optional | Deducts all transaction fees incurred by the payment from the specified balance account. The transaction fees include the acquiring fees (interchange and scheme fee), and the fees due to Adyen (markup or commission). You can book any and all these fees to different balance account by specifying other transaction fee parameters in your split configuration profile:<br><br>- [`adyenCommission`](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic-adyenCommission): The transaction fee due to Adyen under [blended rates](https://www.adyen.com/knowledge-hub/interchange-fees-explained#interchange-vs-blended).<br>- [`adyenMarkup`](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic-adyenMarkup): The transaction fee due to Adyen under [Interchange ++ pricing](https://www.adyen.com/knowledge-hub/interchange-fees-explained#interchange-vs-blended).<br>- [`schemeFee`](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic-schemeFee): The fee paid to the card scheme for using their network.<br>- [`interchange`](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic-interchange): The fee paid to the issuer for each payment transaction made with the card network.<br>- [`adyenFees`](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic-adyenFees): The aggregated amount of Adyen's commission and markup.<br>- [`acquiringFees`](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic-acquiringFees): The aggregated amount of the interchange and scheme fees.<br><br>If you don't include at least one transaction fee type in the `splitLogic` object, Adyen updates the payment request with the `paymentFee` parameter, booking all transaction fees to your platform's liable balance account.<br><br>Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
| `refund` | [`BehaviorEnum`](../../doc/models/behavior-enum.md) | Optional | Specifies how and from which balance account(s) to deduct the refund amount.<br><br>Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio** |
| `refund_cost_allocation` | [`RefundCostAllocationEnum`](../../doc/models/refund-cost-allocation-enum.md) | Optional | Deducts the refund costs from the specified balance account.<br><br>Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount** |
| `remainder` | [`RemainderEnum`](../../doc/models/remainder-enum.md) | Optional | Books the amount left over after currency conversion to the specified balance account.<br><br>Possible values: **addToLiableAccount**, **addToOneBalanceAccount**. |
| `scheme_fee` | [`SchemeFeeEnum`](../../doc/models/scheme-fee-enum.md) | Optional | Deducts the scheme fee from the specified balance account.<br><br>Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
| `split_logic_id` | `str` | Optional, Read-only | Unique identifier of the collection of split instructions that are applied when the rule conditions are met. |
| `surcharge` | [`Surcharge3Enum`](../../doc/models/surcharge-3-enum.md) | Optional | Books the surcharge amount to the specified balance account.<br><br>Possible values: **addToLiableAccount**, **addToOneBalanceAccount** |
| `tip` | [`TipEnum`](../../doc/models/tip-enum.md) | Optional | Books the tips (gratuity) to the specified balance account.<br><br>Possible values: **addToLiableAccount**, **addToOneBalanceAccount**. |

## Example

```python
from adyen.models.acquiring_fees_enum import AcquiringFeesEnum
from adyen.models.additional_commission_1 import AdditionalCommission1
from adyen.models.adyen_commission_enum import AdyenCommissionEnum
from adyen.models.adyen_fees_enum import AdyenFeesEnum
from adyen.models.adyen_markup_enum import AdyenMarkupEnum
from adyen.models.commission_1 import Commission1
from adyen.models.split_configuration_logic_2 import SplitConfigurationLogic2

split_configuration_logic_2 = SplitConfigurationLogic2(
    commission=Commission1(
        fixed_amount=112,
        variable_percentage=52
    ),
    acquiring_fees=AcquiringFeesEnum.DEDUCTFROMLIABLEACCOUNT,
    additional_commission=AdditionalCommission1(
        balance_account_id='balanceAccountId0',
        fixed_amount=100,
        variable_percentage=64
    ),
    adyen_commission=AdyenCommissionEnum.DEDUCTFROMLIABLEACCOUNT,
    adyen_fees=AdyenFeesEnum.DEDUCTFROMLIABLEACCOUNT,
    adyen_markup=AdyenMarkupEnum.DEDUCTFROMLIABLEACCOUNT
)
```

