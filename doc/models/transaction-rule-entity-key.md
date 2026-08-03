
# Transaction Rule Entity Key

*This model accepts additional fields of type Any.*

## Structure

`TransactionRuleEntityKey`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity_reference` | `str` | Optional | The unique identifier of the resource. |
| `entity_type` | `str` | Optional | The type of resource.<br><br>Possible values: **balancePlatform**, **paymentInstrumentGroup**, **accountHolder**, **balanceAccount**, or **paymentInstrument**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.transaction_rule_entity_key import TransactionRuleEntityKey

transaction_rule_entity_key = TransactionRuleEntityKey(
    entity_reference='entityReference8',
    entity_type='entityType6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

