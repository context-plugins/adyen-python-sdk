
# Type 14

The [type of rule](https://docs.adyen.com/issuing/transaction-rules#rule-types), which defines if a rule blocks transactions based on individual characteristics or accumulates data.

Possible values:

* **blockList**: decline a transaction when the conditions are met.
* **maxUsage**: add the amount or number of transactions for the lifetime of a payment instrument, and then decline a transaction when the specified limits are met.
* **velocity**: add the amount or number of transactions based on a specified time interval, and then decline a transaction when the specified limits are met.
* **bypass**: bypass or skip a rule for the specified `entityKey`. Transactions processed to that entity are no longer evaluated by the bypassed rule.  You must provide the `id` of the rule to bypass in `overridesRule` and leave the `ruleRestrictions` object empty.

## Enumeration

`Type14`

## Fields

| Name |
|  --- |
| `ALLOWLIST` |
| `BLOCKLIST` |
| `BYPASS` |
| `MAXUSAGE` |
| `VELOCITY` |

## Example

```python
from adyen.models.type_14 import Type14

type_14 = Type14.VELOCITY
```

