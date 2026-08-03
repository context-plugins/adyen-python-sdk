
# Boarding Token Request

*This model accepts additional fields of type Any.*

## Structure

`BoardingTokenRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `boarding_request_token` | `str` | Required | The boardingToken request token. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.boarding_token_request import BoardingTokenRequest

boarding_token_request = BoardingTokenRequest(
    boarding_request_token='boardingRequestToken4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

