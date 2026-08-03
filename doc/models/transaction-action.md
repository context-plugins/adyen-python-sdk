
# Transaction Action

Action to realise on a transaction. In an `EnableService` request message:

- Starts a transaction by a swipe-ahead mechanism, with the services which are enabled.
- Aborts a swipe-ahead transaction or started by a `CardAcquisition`, and not followed by a service request from the Sale System to complete the transaction.
  Possible values:

* **StartTransaction**
* **AbortTransaction**

## Enumeration

`TransactionAction`

## Fields

| Name |
|  --- |
| `STARTTRANSACTION` |
| `ABORTTRANSACTION` |

## Example

```python
from adyen.models.transaction_action import TransactionAction

transaction_action = TransactionAction.STARTTRANSACTION
```

