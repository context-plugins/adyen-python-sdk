
# Dcc 1

Settings for Dynamic Currency Conversion (DCC).

## Structure

`Dcc1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_dcc` | `bool` | Optional | Enable Dynamic Currency Conversion (DCC). When you enable DCC, you are responsible for complying with [DCC receipt requirements and terms of use](https://help.adyen.com/en_US/knowledge/in-person-payments/terminal-features/dynamic-currency-conversion-dcc-rules-regulations). |

## Example

```python
from adyen.models.dcc_1 import Dcc1

dcc_1 = Dcc1(
    enable_dcc=False
)
```

