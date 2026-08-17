
# Additional Bank Identification

## Structure

`AdditionalBankIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | The value of the additional bank identification. |
| `mtype` | [`Type510Enum`](../../doc/models/type-510-enum.md) | Optional | The type of additional bank identification, depending on the country.<br><br>Possible values:<br><br>* **auBsbCode**: The 6-digit [Australian Bank State Branch (BSB) code](https://en.wikipedia.org/wiki/Bank_state_branch), without separators or spaces.<br>* **caRoutingNumber**: The 9-digit [Canadian routing number](https://en.wikipedia.org/wiki/Routing_number_(Canada)), in EFT format, without separators or spaces.<br>* **gbSortCode**: The 6-digit [UK sort code](https://en.wikipedia.org/wiki/Sort_code), without separators or spaces<br>* **usRoutingNumber**: The 9-digit [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or spaces. |

## Example

```python
from adyen.models.additional_bank_identification import AdditionalBankIdentification
from adyen.models.type_510_enum import Type510Enum

additional_bank_identification = AdditionalBankIdentification(
    code='code4',
    mtype=Type510Enum.AUBSBCODE
)
```

