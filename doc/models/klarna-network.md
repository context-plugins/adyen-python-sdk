
# Klarna Network

*This model accepts additional fields of type Any.*

## Structure

`KlarnaNetwork`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `klarna_network_data` | `str` | Optional | A string containing a structured JSON object. This is a passthrough field used to enable custom features or data exchange with Klarna.<br><br>**Constraints**: *Maximum Length*: `10240` |
| `klarna_network_session_token` | `str` | Optional | The token obtained from the Klarna SDK during an Express Checkout flow.<br><br>**Constraints**: *Maximum Length*: `10240` |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type69`](../../doc/models/type-69.md) | Required | **klarna_network** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.klarna_network import KlarnaNetwork
from adyen.models.type_69 import Type69

klarna_network = KlarnaNetwork(
    mtype=Type69.KLARNA_NETWORK,
    checkout_attempt_id='checkoutAttemptId2',
    klarna_network_data='klarnaNetworkData2',
    klarna_network_session_token='klarnaNetworkSessionToken8',
    recurring_detail_reference='recurringDetailReference6',
    sdk_data='sdkData4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

