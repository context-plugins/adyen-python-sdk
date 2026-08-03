
# Pse Latam

*This model accepts additional fields of type Any.*

## Structure

`PseLatam`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank` | `str` | Required | The shopper's bank. |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `client_type` | `str` | Required | The client type. |
| `identification` | `str` | Required | The identification code. |
| `identification_type` | `str` | Required | The identification type. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type46`](../../doc/models/type-46.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.pse_latam import PseLatam
from adyen.models.type_46 import Type46

pse_latam = PseLatam(
    bank='bank2',
    client_type='clientType2',
    identification='identification8',
    identification_type='identificationType6',
    checkout_attempt_id='checkoutAttemptId0',
    sdk_data='sdkData6',
    mtype=Type46.PSE_PAYULATAM,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

