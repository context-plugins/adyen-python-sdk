
# In Person Donation Settings Update

*This model accepts additional fields of type Any.*

## Structure

`InPersonDonationSettingsUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `default_amount` | [DonationAmountUpdate](../../doc/models/donation-amount-update.md) \| Any \| None | Optional | This is a container for one-of cases. |
| `display_text_field` | [`DisplayTextField2`](../../doc/models/display-text-field-2.md) | Optional | - |
| `donation_flow` | [`DonationFlow1`](../../doc/models/donation-flow-1.md) | Optional | - |
| `donation_type` | [DonationType](../../doc/models/donation-type.md) \| Any \| None | Optional | This is a container for one-of cases. |
| `merchant_accounts` | `List[str]` | Optional | The merchant accounts for this sales channel that are associated with the donation campaign. |
| `present_card_timeout_ms` | `int` | Optional | Required if `donationFlow` is set to **twoStep**. The time, in milliseconds, that the terminal waits for the shopper to present their card. Defaults to **10000** (10 seconds). Range: 5000 to 15000. |
| `prompt_timeout_ms` | `int` | Optional | The time, in milliseconds, that the terminal waits for the shopper to make a selection on the donation screen. Defaults to **10000** (10 seconds). Range: 5000 to 15000. |
| `store_ids` | `List[str]` | Optional | The Adyen-generated unique identifiers of stores for this sales channel that are associated with the donation campaign. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.display_text_field_2 import DisplayTextField2
from adyen.models.donation_amount_update import DonationAmountUpdate
from adyen.models.donation_flow_1 import DonationFlow1
from adyen.models.donation_type import DonationType
from adyen.models.in_person_donation_settings_update import InPersonDonationSettingsUpdate

in_person_donation_settings_update = InPersonDonationSettingsUpdate(
    default_amount=DonationAmountUpdate(
        amounts=[
            40
        ],
        currency_code='currencyCode2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    display_text_field=DisplayTextField2.CAUSENAME,
    donation_flow=DonationFlow1.ONESTEP,
    donation_type=DonationType.FIXEDAMOUNTS,
    merchant_accounts=[
        'merchantAccounts0',
        'merchantAccounts9'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

