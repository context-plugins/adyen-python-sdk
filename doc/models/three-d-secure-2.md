
# Three D Secure 2

The data of the result from the 3DS authentication.

*This model accepts additional fields of type Any.*

## Structure

`ThreeDSecure2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acs_transaction_id` | `str` | Optional | The transaction identifier for the Access Control Server |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.three_d_secure_2 import ThreeDSecure2

three_d_secure_2 = ThreeDSecure2(
    acs_transaction_id='acsTransactionId6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

