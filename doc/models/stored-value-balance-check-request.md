
# Stored Value Balance Check Request

*This model accepts additional fields of type Any.*

## Structure

`StoredValueBalanceCheckRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Optional | - |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `payment_method` | `Dict[str, str]` | Required | The collection that contains the type of the payment method and its specific information if available |
| `recurring_detail_reference` | `str` | Optional | - |
| `reference` | `str` | Required | The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a requirement.<br>If you need to provide multiple references for a transaction, separate them with hyphens ("-").<br>Maximum length: 80 characters. |
| `shopper_interaction` | [`ShopperInteraction1`](../../doc/models/shopper-interaction-1.md) | Optional | - |
| `shopper_reference` | `str` | Optional | - |
| `store` | `str` | Optional | The physical store, for which this payment is processed.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `16` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.shopper_interaction_1 import ShopperInteraction1
from adyen.models.stored_value_balance_check_request import StoredValueBalanceCheckRequest

stored_value_balance_check_request = StoredValueBalanceCheckRequest(
    merchant_account='merchantAccount4',
    payment_method={
        'key0': 'paymentMethod4',
        'key1': 'paymentMethod5'
    },
    reference='reference8',
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    recurring_detail_reference='recurringDetailReference2',
    shopper_interaction=ShopperInteraction1.MOTO,
    shopper_reference='shopperReference0',
    store='store2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

