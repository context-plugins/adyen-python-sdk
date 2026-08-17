
# Transaction Rule Source 2

Contains information about the resource to which the transaction rule applies.

## Structure

`TransactionRuleSource2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | ID of the resource, when applicable. |
| `mtype` | `str` | Optional | Indicates the type of resource for which the transaction rule is defined.<br><br>Possible values:<br><br>* **PaymentInstrumentGroup**<br><br>* **PaymentInstrument**<br><br>* **BalancePlatform**<br><br>* **EntityUsageConfiguration**<br><br>* **PlatformRule**: The transaction rule is a platform-wide rule imposed by Adyen. |

## Example

```python
from adyen.models.transaction_rule_source_2 import TransactionRuleSource2

transaction_rule_source_2 = TransactionRuleSource2(
    id='id2',
    mtype='type8'
)
```

