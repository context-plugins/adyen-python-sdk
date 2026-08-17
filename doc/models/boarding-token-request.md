
# Boarding Token Request

## Structure

`BoardingTokenRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `boarding_request_token` | `str` | Required | The boardingToken request token. |

## Example

```python
from adyen.models.boarding_token_request import BoardingTokenRequest

boarding_token_request = BoardingTokenRequest(
    boarding_request_token='boardingRequestToken4'
)
```

