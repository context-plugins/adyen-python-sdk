
# Online Donation Settings Update

*This model accepts additional fields of type Any.*

## Structure

`OnlineDonationSettingsUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `default_amount` | [DonationAmountUpdate](../../doc/models/donation-amount-update.md) \| Any \| None | Optional | This is a container for one-of cases. |
| `donation_type` | [DonationType](../../doc/models/donation-type.md) \| Any \| None | Optional | This is a container for one-of cases. |
| `merchant_accounts` | `List[str]` | Optional | The merchant accounts for this sales channel that are associated with the donation campaign. |
| `store_ids` | `List[str]` | Optional | The Adyen-generated unique identifiers of stores for this sales channel that are associated with the donation campaign. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.donation_amount_update import DonationAmountUpdate
from adyen.models.donation_type import DonationType
from adyen.models.online_donation_settings_update import OnlineDonationSettingsUpdate

online_donation_settings_update = OnlineDonationSettingsUpdate(
    default_amount=DonationAmountUpdate(
        amounts=[
            40
        ],
        currency_code='currencyCode2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    donation_type=DonationType.ROUNDUP,
    merchant_accounts=[
        'merchantAccounts6',
        'merchantAccounts7',
        'merchantAccounts8'
    ],
    store_ids=[
        'storeIds1',
        'storeIds2'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

