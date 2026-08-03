
# Reveal Pin Response

*This model accepts additional fields of type Any.*

## Structure

`RevealPinResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `encrypted_pin_block` | `str` | Required | The encrypted [PIN block](https://www.pcisecuritystandards.org/glossary/pin-block). |
| `token` | `str` | Required | The 16-digit token that you need to extract the `encryptedPinBlock`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.reveal_pin_response import RevealPinResponse

reveal_pin_response = RevealPinResponse(
    encrypted_pin_block='encryptedPinBlock0',
    token='token0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

