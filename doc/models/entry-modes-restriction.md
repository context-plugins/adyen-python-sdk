
# Entry Modes Restriction

## Structure

`EntryModesRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value2Enum]`](../../doc/models/value-2-enum.md) | Optional | List of point-of-sale entry modes.<br><br>Possible values: **barcode**, **chip**, **cof**, **contactless**, **magstripe**, **manual**, **ocr**, **server**. |

## Example

```python
from adyen.models.entry_modes_restriction import EntryModesRestriction
from adyen.models.value_2_enum import Value2Enum

entry_modes_restriction = EntryModesRestriction(
    operation='operation8',
    value=[
        Value2Enum.CHIP,
        Value2Enum.COF,
        Value2Enum.CONTACTLESS
    ]
)
```

