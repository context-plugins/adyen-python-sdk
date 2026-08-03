
# Return Transfer Request

*This model accepts additional fields of type Any.*

## Structure

`ReturnTransferRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount5`](../../doc/models/amount-5.md) | Required | - |
| `reference` | `str` | Optional | Your internal reference for the return. If you don't provide this in the request, Adyen generates a unique reference. This reference is used in all communication with you about the instruction status.<br><br>We recommend using a unique value per instruction.<br>If you need to provide multiple references for a transaction, separate them with hyphens ("-").<br><br>**Constraints**: *Maximum Length*: `80` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.return_transfer_request import ReturnTransferRequest

return_transfer_request = ReturnTransferRequest(
    amount=Amount5(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    reference='reference6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

