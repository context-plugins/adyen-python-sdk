
# Dcc 1

Settings for Dynamic Currency Conversion (DCC).

*This model accepts additional fields of type Any.*

## Structure

`Dcc1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_dcc` | `bool` | Optional | Enable Dynamic Currency Conversion (DCC). When you enable DCC, you are responsible for complying with [DCC receipt requirements and terms of use](https://help.adyen.com/en_US/knowledge/in-person-payments/terminal-features/dynamic-currency-conversion-dcc-rules-regulations). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.dcc_1 import Dcc1

dcc_1 = Dcc1(
    enable_dcc=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

