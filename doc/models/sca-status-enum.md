
# Sca Status Enum

The status of Strong Customer Authentication (SCA). Possible values:

* **notPerformed**: the requester was unable to successfully authenticate the request using SCA, or has an SCA exemption.
* **pending**: the request is pending SCA authentication.
* **performed**: the request is successfully authenticated using SCA.

## Enumeration

`ScaStatusEnum`

## Fields

| Name |
|  --- |
| `NOTPERFORMED` |
| `PENDING` |
| `PERFORMED` |

## Example

```python
from adyen.models.sca_status_enum import ScaStatusEnum

sca_status = ScaStatusEnum.PENDING
```

