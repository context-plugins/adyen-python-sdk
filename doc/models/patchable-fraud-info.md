
# Patchable Fraud Info

*This model accepts additional fields of type Any.*

## Structure

`PatchableFraudInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_does_not_belong_to_cardholder` | `bool` | Optional | The card is no longer in the cardholder's possession. Set to **true** if the card is lost or stolen. |
| `card_was_counterfeited` | `bool` | Optional | The card was counterfeited. |
| `description_of_issue` | `str` | Optional | Your description of the issue for raising a dispute of `type` **fraud**.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `2500` |
| `report_only` | `bool` | Optional | Set to **true** to report fraud to Adyen with no further action, such as a request for a chargeback or fee reversal. The default value is **false**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.patchable_fraud_info import PatchableFraudInfo

patchable_fraud_info = PatchableFraudInfo(
    card_does_not_belong_to_cardholder=False,
    card_was_counterfeited=False,
    description_of_issue='descriptionOfIssue2',
    report_only=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

