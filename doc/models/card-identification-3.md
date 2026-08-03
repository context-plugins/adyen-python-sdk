
# Card Identification 3

Contains the identification details of the card.

*This model accepts additional fields of type Any.*

## Structure

`CardIdentification3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `expiry_month` | `str` | Optional | The expiry month of the card.<br><br>Format: two digits. Add a leading zero for single-digit months. For example:<br><br>* 03 = March<br>* 11 = November<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `expiry_year` | `str` | Optional | The expiry year of the card.<br><br>Format: four digits. For example: 2020<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `4` |
| `issue_number` | `str` | Optional | The issue number of the card. Applies only to some UK debit cards.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `2` |
| `number` | `str` | Optional | The card number without any separators.<br><br>For security, the response only includes the last four digits of the card number.<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `19` |
| `start_month` | `str` | Optional | The month when the card was issued. Applies only to some UK debit cards.<br><br>Format: two digits. Add a leading zero for single-digit months. For example:<br><br>* 03 = March<br>* 11 = November<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `start_year` | `str` | Optional | The year when the card was issued. Applies only to some UK debit cards.<br><br>Format: four digits. For example: 2020<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `4` |
| `stored_payment_method_id` | `str` | Optional | The unique [token](/payouts/payout-service/pay-out-to-cards/manage-card-information#save-card-details) created to identify the counterparty. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.card_identification_3 import CardIdentification3

card_identification_3 = CardIdentification3(
    expiry_month='expiryMonth2',
    expiry_year='expiryYear2',
    issue_number='issueNumber0',
    number='number6',
    start_month='startMonth8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

