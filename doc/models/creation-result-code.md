
# Creation Result Code

Notification message. It informs about the outcome of the operation. Possible values:

* CREATED
* ALREADY_EXISTS
* ERROR

## Enumeration

`CreationResultCode`

## Fields

| Name |
|  --- |
| `ALREADY_EXISTS` |
| `CREATED` |
| `ERROR` |

## Example

```python
from adyen.models.creation_result_code import CreationResultCode

creation_result_code = CreationResultCode.ERROR
```

