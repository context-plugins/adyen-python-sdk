
# Store and Forward

## Structure

`StoreAndForward`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `max_amount` | [`List[MinorUnitsMonetaryValue]`](../../doc/models/minor-units-monetary-value.md) | Optional | The maximum amount that the terminal accepts for a single store-and-forward payment. |
| `max_payments` | `int` | Optional | The maximum number of store-and-forward transactions per terminal that you can process while offline. |
| `supported_card_types` | [`SupportedCardTypes2`](../../doc/models/supported-card-types-2.md) | Optional | The type of card for which the terminal accepts store-and-forward payments. You can specify multiple card types. |

## Example

```python
from adyen.models.minor_units_monetary_value import MinorUnitsMonetaryValue
from adyen.models.store_and_forward import StoreAndForward
from adyen.models.supported_card_types_2 import SupportedCardTypes2

store_and_forward = StoreAndForward(
    max_amount=[
        MinorUnitsMonetaryValue(
            amount=50,
            currency_code='currencyCode4'
        )
    ],
    max_payments=192,
    supported_card_types=SupportedCardTypes2(
        credit=False,
        debit=False,
        deferred_debit=False,
        prepaid=False,
        unknown=False
    )
)
```

