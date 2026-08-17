
# Card Holder PIN

## Structure

`CardHolderPIN`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `encr_pin_block` | `str` | Required | - |
| `pin_format` | [`PINFormat1Enum`](../../doc/models/pin-format-1-enum.md) | Required | Possible values:<br><br>* **ISO0**<br>* **ISO1**<br>* **ISO2**<br>* **ISO3** |
| `additional_input` | `str` | Optional | **Constraints**: *Pattern*: `^.+$` |

## Example

```python
from adyen.models.card_holder_pin import CardHolderPIN
from adyen.models.pin_format_1_enum import PINFormat1Enum

card_holder_pin = CardHolderPIN(
    encr_pin_block='EncrPINBlock2',
    pin_format=PINFormat1Enum.ISO2,
    additional_input='AdditionalInput2'
)
```

