
# Transaction Rule Entity Key 2

The type and unique identifier of the resource to which the rule applies.

## Structure

`TransactionRuleEntityKey2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity_reference` | `str` | Optional | The unique identifier of the resource. |
| `entity_type` | `str` | Optional | The type of resource.<br><br>Possible values: **balancePlatform**, **paymentInstrumentGroup**, **accountHolder**, **balanceAccount**, or **paymentInstrument**. |

## Example

```python
from adyen.models.transaction_rule_entity_key_2 import TransactionRuleEntityKey2

transaction_rule_entity_key_2 = TransactionRuleEntityKey2(
    entity_reference='entityReference8',
    entity_type='entityType4'
)
```

