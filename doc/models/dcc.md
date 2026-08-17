
# Dcc

## Structure

`Dcc`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_dcc` | `bool` | Optional | Enable Dynamic Currency Conversion (DCC). When you enable DCC, you are responsible for complying with [DCC receipt requirements and terms of use](https://help.adyen.com/en_US/knowledge/in-person-payments/terminal-features/dynamic-currency-conversion-dcc-rules-regulations). |

## Example

```python
from adyen.models.dcc import Dcc

dcc = Dcc(
    enable_dcc=False
)
```

