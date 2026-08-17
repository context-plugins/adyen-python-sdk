
# Fraud Info 1

Additional information for raising a dispute of `type` **fraud**. Required for disputes of `type` **fraud**.

## Structure

`FraudInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_does_not_belong_to_cardholder` | `bool` | Required | The card is no longer in the cardholder's possession. Set to **true** if the card is lost or stolen. |
| `card_was_counterfeited` | `bool` | Required | The card was counterfeited. |
| `description_of_issue` | `str` | Required | Your description of the issue for raising a dispute of `type` **fraud**.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `2500` |
| `report_only` | `bool` | Optional | Set to **true** to report fraud to Adyen with no further action, such as a request for a chargeback or fee reversal. The default value is **false**. |

## Example

```python
from adyen.models.fraud_info_1 import FraudInfo1

fraud_info_1 = FraudInfo1(
    card_does_not_belong_to_cardholder=False,
    card_was_counterfeited=False,
    description_of_issue='descriptionOfIssue0',
    report_only=False
)
```

