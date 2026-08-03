
# Bank Account Identification

*This model accepts additional fields of type Any.*

## Structure

`BankAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bank_account_identification import BankAccountIdentification

bank_account_identification = BankAccountIdentification(
    mtype='BankAccountIdentification',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

