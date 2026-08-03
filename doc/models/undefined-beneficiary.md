
# Undefined Beneficiary

*This model accepts additional fields of type Any.*

## Structure

`UndefinedBeneficiary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | The details of the undefined beneficiary. |
| `reference` | `str` | Optional, Read-only | The reference of the undefined beneficiary. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.undefined_beneficiary import UndefinedBeneficiary

undefined_beneficiary = UndefinedBeneficiary(
    description='description4',
    reference='reference8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

