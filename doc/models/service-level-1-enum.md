
# Service Level 1 Enum

Specifies the service level (settlement type) of this payment method. Required for merchants operating in Japan. Possible values:

* **noContract**: Adyen holds the contract with JCB.
* **gatewayContract**: JCB receives the settlement and handles disputes, then pays out to you or your sub-merchant directly.

## Enumeration

`ServiceLevel1Enum`

## Fields

| Name |
|  --- |
| `NOCONTRACT` |
| `GATEWAYCONTRACT` |

## Example

```python
from adyen.models.service_level_1_enum import ServiceLevel1Enum

service_level_1 = ServiceLevel1Enum.NOCONTRACT
```

