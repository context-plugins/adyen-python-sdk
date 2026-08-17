
# Admin Request 2

Content of the Admin Request message.

## Structure

`AdminRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_identification` | `str` | Optional | Identification of the administrative service to process.<br><br>**Constraints**: *Pattern*: `^.+$` |

## Example

```python
from adyen.models.admin_request_2 import AdminRequest2

admin_request_2 = AdminRequest2(
    service_identification='ServiceIdentification0'
)
```

