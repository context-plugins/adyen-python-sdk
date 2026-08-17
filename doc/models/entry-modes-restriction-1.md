
# Entry Modes Restriction 1

List of point-of-sale entry modes and the operation..

Supported operations: **anyMatch**, **noneMatch**.

## Structure

`EntryModesRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value2Enum]`](../../doc/models/value-2-enum.md) | Optional | List of point-of-sale entry modes.<br><br>Possible values: **barcode**, **chip**, **cof**, **contactless**, **magstripe**, **manual**, **ocr**, **server**. |

## Example

```python
from adyen.models.entry_modes_restriction_1 import EntryModesRestriction1
from adyen.models.value_2_enum import Value2Enum

entry_modes_restriction_1 = EntryModesRestriction1(
    operation='operation0',
    value=[
        Value2Enum.UNKNOWN
    ]
)
```

