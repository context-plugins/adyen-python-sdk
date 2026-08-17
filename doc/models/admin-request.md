
# Admin Request

Empty.
Content of the Custom Admin Request message.

## Structure

`AdminRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_identification` | `str` | Optional | Identification of the administrative service to process.<br><br>**Constraints**: *Pattern*: `^.+$` |

## Example

```python
from adyen.models.admin_request import AdminRequest

admin_request = AdminRequest(
    service_identification='ServiceIdentification4'
)
```

