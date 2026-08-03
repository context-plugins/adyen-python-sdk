
# Account Identification 1

Contains the account number to which the payment funds are sent.

*This model accepts additional fields of type Any.*

## Structure

`AccountIdentification1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_identification_1 import AccountIdentification1

account_identification_1 = AccountIdentification1(
    mtype='AccountIdentification1',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

