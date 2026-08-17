
# External Reason 1

The external reason for the transfer status.

## Structure

`ExternalReason1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | The reason code. |
| `description` | `str` | Optional | The description of the reason code. |
| `namespace` | `str` | Optional | The namespace for the reason code. |

## Example

```python
from adyen.models.external_reason_1 import ExternalReason1

external_reason_1 = ExternalReason1(
    code='code6',
    description='description8',
    namespace='namespace4'
)
```

