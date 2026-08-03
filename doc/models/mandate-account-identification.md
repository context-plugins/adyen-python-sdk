
# Mandate Account Identification

*This model accepts additional fields of type Any.*

## Structure

`MandateAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.mandate_account_identification import MandateAccountIdentification

mandate_account_identification = MandateAccountIdentification(
    mtype='MandateAccountIdentification',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

