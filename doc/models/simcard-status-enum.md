
# Simcard Status Enum

Indicates the status of the SIM card in the payment terminal. Can be updated and received only at terminal level, and only for models that support cellular connectivity.

Possible values:

* **ACTIVATED**: the SIM card is activated. Cellular connectivity may still need to be enabled on the terminal itself, in the **Network** settings.
* **INVENTORY**: the SIM card is not activated. The terminal can't use cellular connectivity.

## Enumeration

`SimcardStatusEnum`

## Fields

| Name |
|  --- |
| `ACTIVATED` |
| `INVENTORY` |

## Example

```python
from adyen.models.simcard_status_enum import SimcardStatusEnum

simcard_status = SimcardStatusEnum.ACTIVATED
```

