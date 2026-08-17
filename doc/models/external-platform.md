
# External Platform

Third-party developed platform used to initiate payment requests. For example, Magento, Zuora, etc.

## Structure

`ExternalPlatform`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `integrator` | `str` | Optional | External platform integrator. |
| `name` | `str` | Optional | Name of the field. For example, Name of External Platform. |
| `version` | `str` | Optional | Version of the field. For example, Version of External Platform. |

## Example

```python
from adyen.models.external_platform import ExternalPlatform

external_platform = ExternalPlatform(
    integrator='integrator2',
    name='name6',
    version='version8'
)
```

