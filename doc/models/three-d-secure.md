
# Three D Secure

*This model accepts additional fields of type Any.*

## Structure

`ThreeDSecure`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acs_transaction_id` | `str` | Optional | The transaction identifier for the Access Control Server |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.three_d_secure import ThreeDSecure

three_d_secure = ThreeDSecure(
    acs_transaction_id='acsTransactionId4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

