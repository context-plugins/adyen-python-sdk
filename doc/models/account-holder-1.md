
# Account Holder 1

Contains the full name of the person or entity that receives the payment funds).

*This model accepts additional fields of type Any.*

## Structure

`AccountHolder1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `full_name` | `str` | Required | Full name of the account holder.<br><br>**Constraints**: *Minimum Length*: `1` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_holder_1 import AccountHolder1

account_holder_1 = AccountHolder1(
    full_name='John Doe',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

