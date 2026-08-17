
# PSE Latam

## Structure

`PSELatam`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank` | `str` | Required | The shopper's bank. |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `client_type` | `str` | Required | The client type. |
| `identification` | `str` | Required | The identification code. |
| `identification_type` | `str` | Required | The identification type. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type46Enum`](../../doc/models/type-46-enum.md) | Optional | The payment method type. |

## Example

```python
from adyen.models.pse_latam import PSELatam
from adyen.models.type_46_enum import Type46Enum

pse_latam = PSELatam(
    bank='bank2',
    client_type='clientType2',
    identification='identification8',
    identification_type='identificationType6',
    checkout_attempt_id='checkoutAttemptId0',
    sdk_data='sdkData6',
    mtype=Type46Enum.PSE_PAYULATAM
)
```

