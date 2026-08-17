
# String Match

## Structure

`StringMatch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | [`OperationEnum`](../../doc/models/operation-enum.md) | Optional | The type of string matching operation. Possible values:  **startsWith**, **endsWith**, **isEqualTo**, **contains**, |
| `value` | `str` | Optional | The string to be matched. |

## Example

```python
from adyen.models.operation_enum import OperationEnum
from adyen.models.string_match import StringMatch

string_match = StringMatch(
    operation=OperationEnum.ISEQUALTO,
    value='value4'
)
```

