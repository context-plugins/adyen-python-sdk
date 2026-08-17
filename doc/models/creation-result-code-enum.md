
# Creation Result Code Enum

Notification message. It informs about the outcome of the operation. Possible values:

* CREATED
* ALREADY_EXISTS
* ERROR

## Enumeration

`CreationResultCodeEnum`

## Fields

| Name |
|  --- |
| `ALREADY_EXISTS` |
| `CREATED` |
| `ERROR` |

## Example

```python
from adyen.models.creation_result_code_enum import CreationResultCodeEnum

creation_result_code = CreationResultCodeEnum.ERROR
```

