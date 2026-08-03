
# Bank Account Model 1

Contains the business account details.

*This model accepts additional fields of type Any.*

## Structure

`BankAccountModel1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `form_factor` | `Any` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bank_account_model_1 import BankAccountModel1

bank_account_model_1 = BankAccountModel1(
    form_factor=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

