
# Bank Account Model

*This model accepts additional fields of type Any.*

## Structure

`BankAccountModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `form_factor` | `Any` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bank_account_model import BankAccountModel

bank_account_model = BankAccountModel(
    form_factor=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

