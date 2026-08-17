
# Transaction Action 1 Enum

Action to realise on a transaction. In an `EnableService` request message:

- Starts a transaction by a swipe-ahead mechanism, with the services which are enabled.
- Aborts a swipe-ahead transaction or started by a `CardAcquisition`, and not followed by a service request from the Sale System to complete the transaction.
  Possible values:

* **AbortTransaction**
* **StartTransaction**

## Enumeration

`TransactionAction1Enum`

## Fields

| Name |
|  --- |
| `STARTTRANSACTION` |
| `ABORTTRANSACTION` |

## Example

```python
from adyen.models.transaction_action_1_enum import TransactionAction1Enum

transaction_action_1 = TransactionAction1Enum.STARTTRANSACTION
```

