
# Boarding Token Response

*This model accepts additional fields of type Any.*

## Structure

`BoardingTokenResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `boarding_token` | `str` | Required | The boarding token that allows the Payments App to board. |
| `installation_id` | `str` | Required | The unique identifier of the Payments App instance. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.boarding_token_response import BoardingTokenResponse

boarding_token_response = BoardingTokenResponse(
    boarding_token='boardingToken6',
    installation_id='installationId0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

