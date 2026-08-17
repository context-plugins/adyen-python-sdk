
# Bank Identification

## Structure

`BankIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country` | `str` | Optional | Two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. |
| `identification` | `str` | Optional | The bank identification code. |
| `identification_type` | [`IdentificationTypeEnum`](../../doc/models/identification-type-enum.md) | Optional | The type of the identification.<br><br>Possible values: **iban**, **routingNumber**, **sortCode**, **bic**. |

## Example

```python
from adyen.models.bank_identification import BankIdentification
from adyen.models.identification_type_enum import IdentificationTypeEnum

bank_identification = BankIdentification(
    country='country6',
    identification='identification0',
    identification_type=IdentificationTypeEnum.BIC
)
```

