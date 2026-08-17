
# Type 15 Enum

The type of the document. Possible values: **ID**, **DRIVINGLICENSE**, **PASSPORT**, **SOCIALSECURITY**, **VISA**.

To delete an existing entry for a document `type`, send only the `type` field in your request.

## Enumeration

`Type15Enum`

## Fields

| Name |
|  --- |
| `DRIVINGLICENSE` |
| `ID` |
| `PASSPORT` |
| `SOCIALSECURITY` |
| `VISA` |

## Example

```python
from adyen.models.type_15_enum import Type15Enum

type_15 = Type15Enum.PASSPORT
```

