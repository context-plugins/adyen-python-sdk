
# Schedule Account Updater Request

## Structure

`ScheduleAccountUpdaterRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be required for a particular request. |
| `card` | [`Card`](../../doc/models/card.md) | Optional | Credit card data.<br><br>Optional if `shopperReference` and `selectedRecurringDetailReference` are provided. |
| `merchant_account` | `str` | Required | Account of the merchant. |
| `reference` | `str` | Required | A reference that merchants can apply for the call. |
| `selected_recurring_detail_reference` | `str` | Optional | The selected detail recurring reference.<br><br>Optional if `card` is provided. |
| `shopper_reference` | `str` | Optional | The reference of the shopper that owns the recurring contract.<br><br>Optional if `card` is provided. |

## Example

```python
from adyen.models.card import Card
from adyen.models.schedule_account_updater_request import ScheduleAccountUpdaterRequest

schedule_account_updater_request = ScheduleAccountUpdaterRequest(
    merchant_account='merchantAccount0',
    reference='reference6',
    additional_data={
        'key0': 'additionalData8'
    },
    card=Card(
        cvc='cvc0',
        expiry_month='expiryMonth0',
        expiry_year='expiryYear0',
        holder_name='holderName2',
        issue_number='issueNumber8'
    ),
    selected_recurring_detail_reference='selectedRecurringDetailReference2',
    shopper_reference='shopperReference6'
)
```

