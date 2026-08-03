
# Ideal Authenticate Request

*This model accepts additional fields of type Any.*

## Structure

`IdealAuthenticateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Required | The unique identifier for an account holder.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `150` |
| `payload` | `str` | Required | A payload provided by iDEAL to complete the authentication process.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `400` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.ideal_authenticate_request import IdealAuthenticateRequest

ideal_authenticate_request = IdealAuthenticateRequest(
    account_holder_id='AH00000000000000000000000',
    payload='https://ideal.auth/somePayload',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

