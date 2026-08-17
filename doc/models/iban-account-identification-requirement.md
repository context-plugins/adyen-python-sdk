
# Iban Account Identification Requirement

## Structure

`IbanAccountIdentificationRequirement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Specifies the allowed prefixes for the international bank account number as defined in the ISO-13616 standard. |
| `iban_prefixes` | `List[str]` | Optional | Contains the list of allowed prefixes for international bank accounts. For example: NL, US, UK. |
| `mtype` | `str` | Required, Constant | **ibanAccountIdentificationRequirement**<br><br>**Value**: `"ibanAccountIdentificationRequirement"` |

## Example

```python
from adyen.models.iban_account_identification_requirement import IbanAccountIdentificationRequirement

iban_account_identification_requirement = IbanAccountIdentificationRequirement(
    description='description4',
    iban_prefixes=[
        'ibanPrefixes8'
    ]
)
```

