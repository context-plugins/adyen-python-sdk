
# Type

The type of the document. Possible values: **ID**, **DRIVINGLICENSE**, **PASSPORT**, **SOCIALSECURITY**, **VISA**.

To delete an existing entry for a document `type`, send only the `type` field in your request.

## Enumeration

`Type`

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
from adyen.models.mtype import Type

mtype = Type.VISA
```

