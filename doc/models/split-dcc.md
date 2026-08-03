
# Split Dcc

*This model accepts additional fields of type Any.*

## Structure

`SplitDcc`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_percentage` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.split_dcc import SplitDcc

split_dcc = SplitDcc(
    account_holder_percentage=214,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

