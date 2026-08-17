
# Signature

## Structure

`Signature`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ask_signature_on_screen` | `bool` | Optional | If `skipSignature` is false, indicates whether the shopper should provide a signature on the display (**true**) or on the merchant receipt (**false**). |
| `device_name` | `str` | Optional | Name that identifies the terminal. |
| `device_slogan` | `str` | Optional | Slogan shown on the start screen of the device.<br><br>**Constraints**: *Maximum Length*: `50` |
| `skip_signature` | `bool` | Optional | Skip asking for a signature. This is possible because all global card schemes (American Express, Diners, Discover, JCB, MasterCard, VISA, and UnionPay) regard a signature as optional. |

## Example

```python
from adyen.models.signature import Signature

signature = Signature(
    ask_signature_on_screen=False,
    device_name='deviceName8',
    device_slogan='deviceSlogan6',
    skip_signature=False
)
```

