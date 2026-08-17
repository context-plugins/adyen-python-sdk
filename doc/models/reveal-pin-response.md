
# Reveal Pin Response

## Structure

`RevealPinResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `encrypted_pin_block` | `str` | Required | The encrypted [PIN block](https://www.pcisecuritystandards.org/glossary/pin-block). |
| `token` | `str` | Required | The 16-digit token that you need to extract the `encryptedPinBlock`. |

## Example

```python
from adyen.models.reveal_pin_response import RevealPinResponse

reveal_pin_response = RevealPinResponse(
    encrypted_pin_block='encryptedPinBlock0',
    token='token0'
)
```

