
# Cardreaderapdu Response 4

*This model accepts additional fields of type Any.*

## Structure

`CardreaderapduResponse4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response3`](../../doc/models/response-3.md) | Required | - |
| `apdu_data` | `str` | Optional | Data field of the APDU command (Lc + Data).<br><br>**Constraints**: *Pattern*: `^.+$` |
| `card_status_words` | `str` | Required | Status of a smartcard response to a command (SW1-SW2).<br><br>**Constraints**: *Pattern*: `^.{2,2}$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.cardreaderapdu_response_4 import CardreaderapduResponse4
from adyen.models.error_condition_1 import ErrorCondition1
from adyen.models.response_3 import Response3
from adyen.models.result_11 import Result11

cardreaderapdu_response_4 = CardreaderapduResponse4(
    response=Response3(
        result=Result11.PARTIAL,
        error_condition=ErrorCondition1.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    card_status_words='CardStatusWords4',
    apdu_data='APDUData6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

