
# Merchant Balance

*This model accepts additional fields of type Any.*

## Structure

`MerchantBalance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `available_fund` | [`Amount3`](../../doc/models/amount-3.md) | Optional | The amount that must be pushed out or pulled in. You can configure either `sweepAmount` or `targetAmount`, not both. |
| `deposit` | [`Amount3`](../../doc/models/amount-3.md) | Optional | The amount that must be pushed out or pulled in. You can configure either `sweepAmount` or `targetAmount`, not both. |
| `merchant_account` | `str` | Optional | - |
| `next_payout` | [`Amount3`](../../doc/models/amount-3.md) | Optional | The amount that must be pushed out or pulled in. You can configure either `sweepAmount` or `targetAmount`, not both. |
| `pending_balance` | [`Amount3`](../../doc/models/amount-3.md) | Optional | The amount that must be pushed out or pulled in. You can configure either `sweepAmount` or `targetAmount`, not both. |
| `reserve` | [`Amount3`](../../doc/models/amount-3.md) | Optional | The amount that must be pushed out or pulled in. You can configure either `sweepAmount` or `targetAmount`, not both. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_3 import Amount3
from adyen.models.merchant_balance import MerchantBalance

merchant_balance = MerchantBalance(
    available_fund=Amount3(
        currency='currency4',
        value=152,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    deposit=Amount3(
        currency='currency4',
        value=62,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    merchant_account='merchantAccount4',
    next_payout=Amount3(
        currency='currency4',
        value=240,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    pending_balance=Amount3(
        currency='currency2',
        value=254,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

