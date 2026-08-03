
# Online Donation Settings

*This model accepts additional fields of type Any.*

## Structure

`OnlineDonationSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `default_amount` | [`DonationAmount`](../../doc/models/donation-amount.md) | Optional | - |
| `donation_type` | [`DonationType1`](../../doc/models/donation-type-1.md) | Optional | - |
| `merchant_accounts` | `List[str]` | Optional | The merchant accounts for this sales channel that are associated with the donation campaign. |
| `store_ids` | `List[str]` | Optional | The Adyen-generated unique identifiers of stores for this sales channel that are associated with the donation campaign. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.donation_amount import DonationAmount
from adyen.models.donation_type_1 import DonationType1
from adyen.models.online_donation_settings import OnlineDonationSettings

online_donation_settings = OnlineDonationSettings(
    default_amount=DonationAmount(
        amounts=[
            78,
            79,
            80
        ],
        currency_code='currencyCode6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    donation_type=DonationType1.ROUNDUP,
    merchant_accounts=[
        'merchantAccounts4'
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

