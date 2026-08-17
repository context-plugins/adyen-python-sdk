
# Undefined Beneficiary

## Structure

`UndefinedBeneficiary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | The details of the undefined beneficiary. |
| `reference` | `str` | Optional, Read-only | The reference of the undefined beneficiary. |

## Example

```python
from adyen.models.undefined_beneficiary import UndefinedBeneficiary

undefined_beneficiary = UndefinedBeneficiary(
    description='description4'
)
```

