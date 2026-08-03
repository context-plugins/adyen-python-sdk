
# Split Configuration Logic

*This model accepts additional fields of type Any.*

## Structure

`SplitConfigurationLogic`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acquiring_fees` | [`AcquiringFees`](../../doc/models/acquiring-fees.md) | Optional | - |
| `additional_commission` | [`AdditionalCommission`](../../doc/models/additional-commission.md) | Optional | - |
| `adyen_commission` | [`AdyenCommission`](../../doc/models/adyen-commission.md) | Optional | - |
| `adyen_fees` | [`AdyenFees`](../../doc/models/adyen-fees.md) | Optional | - |
| `adyen_markup` | [`AdyenMarkup`](../../doc/models/adyen-markup.md) | Optional | - |
| `chargeback` | [`Behavior`](../../doc/models/behavior.md) | Optional | - |
| `chargeback_cost_allocation` | [`ChargebackCostAllocation`](../../doc/models/chargeback-cost-allocation.md) | Optional | - |
| `commission` | [`Commission`](../../doc/models/commission.md) | Required | - |
| `dcc` | [`SplitDcc`](../../doc/models/split-dcc.md) | Optional | - |
| `interchange` | [`Interchange`](../../doc/models/interchange.md) | Optional | - |
| `payment_fee` | [`PaymentFee`](../../doc/models/payment-fee.md) | Optional | - |
| `refund` | [`Behavior`](../../doc/models/behavior.md) | Optional | - |
| `refund_cost_allocation` | [`RefundCostAllocation`](../../doc/models/refund-cost-allocation.md) | Optional | - |
| `remainder` | [`Remainder`](../../doc/models/remainder.md) | Optional | - |
| `scheme_fee` | [`SchemeFee`](../../doc/models/scheme-fee.md) | Optional | - |
| `split_logic_id` | `str` | Optional, Read-only | Unique identifier of the collection of split instructions that are applied when the rule conditions are met. |
| `surcharge` | [`Surcharge3`](../../doc/models/surcharge-3.md) | Optional | - |
| `tip` | [`Tip`](../../doc/models/tip.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.acquiring_fees import AcquiringFees
from adyen.models.additional_commission import AdditionalCommission
from adyen.models.adyen_commission import AdyenCommission
from adyen.models.adyen_fees import AdyenFees
from adyen.models.adyen_markup import AdyenMarkup
from adyen.models.commission import Commission
from adyen.models.split_configuration_logic import SplitConfigurationLogic

split_configuration_logic = SplitConfigurationLogic(
    commission=Commission(
        fixed_amount=112,
        variable_percentage=52,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    acquiring_fees=AcquiringFees.DEDUCTFROMLIABLEACCOUNT,
    additional_commission=AdditionalCommission(
        balance_account_id='balanceAccountId0',
        fixed_amount=100,
        variable_percentage=64,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    adyen_commission=AdyenCommission.DEDUCTFROMLIABLEACCOUNT,
    adyen_fees=AdyenFees.DEDUCTFROMLIABLEACCOUNT,
    adyen_markup=AdyenMarkup.DEDUCTFROMLIABLEACCOUNT,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

