
# Split Dcc 2

Defines the logic for booking the markup paid by the customer for Dynamic Currency Conversion (DCC).

> This field is in pilot phase, and not yet available for all platforms.

*This model accepts additional fields of type Any.*

## Structure

`SplitDcc2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_percentage` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.split_dcc_2 import SplitDcc2

split_dcc_2 = SplitDcc2(
    account_holder_percentage=134,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

