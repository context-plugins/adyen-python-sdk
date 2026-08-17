
# External Reason

## Structure

`ExternalReason`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | The reason code. |
| `description` | `str` | Optional | The description of the reason code. |
| `namespace` | `str` | Optional | The namespace for the reason code. |

## Example

```python
from adyen.models.external_reason import ExternalReason

external_reason = ExternalReason(
    code='code6',
    description='description8',
    namespace='namespace4'
)
```

