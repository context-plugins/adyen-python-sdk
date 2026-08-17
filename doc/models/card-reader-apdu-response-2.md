
# Card Reader APDU Response 2

Content of the Card Reader APDU Response message.

## Structure

`CardReaderAPDUResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response11`](../../doc/models/response-11.md) | Required | Result of a message request processing. |
| `apdu_data` | `str` | Optional | Data field of the APDU command (Lc + Data).<br><br>**Constraints**: *Pattern*: `^.+$` |
| `card_status_words` | `str` | Required | Status of a smartcard response to a command (SW1-SW2).<br><br>**Constraints**: *Pattern*: `^.{2,2}$` |

## Example

```python
from adyen.models.card_reader_apdu_response_2 import CardReaderAPDUResponse2
from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.response_11 import Response11
from adyen.models.result_11_enum import Result11Enum

card_reader_apdu_response_2 = CardReaderAPDUResponse2(
    response=Response11(
        result=Result11Enum.PARTIAL,
        error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8'
    ),
    card_status_words='CardStatusWords0',
    apdu_data='APDUData2'
)
```

