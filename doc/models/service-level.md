
# Service Level

Specifies the service level (settlement type) of this payment method. Possible values:

* **noContract**: Adyen holds the contract with American Express.
* **gatewayContract**: American Express receives the settlement and handles disputes, then pays out to you or your sub-merchant directly.
* **paymentDesignatorContract**: Adyen receives the settlement, and handles disputes and payouts.

## Enumeration

`ServiceLevel`

## Fields

| Name |
|  --- |
| `NOCONTRACT` |
| `GATEWAYCONTRACT` |
| `PAYMENTDESIGNATORCONTRACT` |

## Example

```python
from adyen.models.service_level import ServiceLevel

service_level = ServiceLevel.NOCONTRACT
```

