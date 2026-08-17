
# Additional Bank Identification Requirement

## Structure

`AdditionalBankIdentificationRequirement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_bank_identification_type` | [`AdditionalBankIdentificationTypeEnum`](../../doc/models/additional-bank-identification-type-enum.md) | Optional | The type of additional bank identification, depending on the country.<br><br>Possible values:<br><br>* **auBsbCode**: The 6-digit [Australian Bank State Branch (BSB) code](https://en.wikipedia.org/wiki/Bank_state_branch), without separators or spaces.<br>* **caRoutingNumber**: The 9-digit [Canadian routing number](https://en.wikipedia.org/wiki/Routing_number_(Canada)), in EFT format, without separators or spaces.<br>* **gbSortCode**: The 6-digit [UK sort code](https://en.wikipedia.org/wiki/Sort_code), without separators or spaces<br>* **usRoutingNumber**: The 9-digit [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or spaces. |
| `description` | `str` | Optional | The description of the additional bank identification requirement. |
| `mtype` | `str` | Required, Constant | **additionalBankIdentificationRequirement**<br><br>**Value**: `"additionalBankIdentificationRequirement"` |

## Example

```python
from adyen.models.additional_bank_identification_requirement import AdditionalBankIdentificationRequirement
from adyen.models.additional_bank_identification_type_enum import AdditionalBankIdentificationTypeEnum

additional_bank_identification_requirement = AdditionalBankIdentificationRequirement(
    additional_bank_identification_type=AdditionalBankIdentificationTypeEnum.AUBSBCODE,
    description='description2'
)
```

