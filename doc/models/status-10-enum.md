
# Status 10 Enum

The status of the payment instrument. If a status is not specified when creating a payment instrument, it is set to **active** by default. However, there can be exceptions for cards based on the `card.formFactor` and the `issuingCountryCode`. For example, when issuing physical cards in the US, the default status is **inactive**.

Possible values:

* **active**:  The payment instrument is active and can be used to make payments.

* **inactive**: The payment instrument is inactive and cannot be used to make payments.

* **suspended**: The payment instrument is suspended, either because it was stolen or lost.

* **closed**: The payment instrument is permanently closed. This action cannot be undone.

## Enumeration

`Status10Enum`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `CLOSED` |
| `INACTIVE` |
| `SUSPENDED` |

## Example

```python
from adyen.models.status_10_enum import Status10Enum

status_10 = Status10Enum.INACTIVE
```

