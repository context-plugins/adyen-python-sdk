
# Boarding Token Response

## Structure

`BoardingTokenResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `boarding_token` | `str` | Required | The boarding token that allows the Payments App to board. |
| `installation_id` | `str` | Required | The unique identifier of the Payments App instance. |

## Example

```python
from adyen.models.boarding_token_response import BoardingTokenResponse

boarding_token_response = BoardingTokenResponse(
    boarding_token='boardingToken6',
    installation_id='installationId0'
)
```

