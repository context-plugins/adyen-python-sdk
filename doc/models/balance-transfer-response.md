
# Balance Transfer Response

*This model accepts additional fields of type Any.*

## Structure

`BalanceTransferResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_at` | `datetime` | Required | The date when the balance transfer was performed. |
| `psp_reference` | `str` | Required | Adyen's 16-character string reference associated with the balance transfer. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.balance_transfer_response import BalanceTransferResponse

balance_transfer_response = BalanceTransferResponse(
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    psp_reference='pspReference4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

