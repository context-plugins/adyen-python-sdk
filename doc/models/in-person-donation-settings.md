
# In Person Donation Settings

*This model accepts additional fields of type Any.*

## Structure

`InPersonDonationSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `default_amount` | [`DonationAmount`](../../doc/models/donation-amount.md) | Optional | - |
| `display_text_field` | [`DisplayTextField2`](../../doc/models/display-text-field-2.md) | Required | - |
| `donation_flow` | [`DonationFlow1`](../../doc/models/donation-flow-1.md) | Required | - |
| `donation_type` | [`DonationType1`](../../doc/models/donation-type-1.md) | Optional | - |
| `merchant_accounts` | `List[str]` | Optional | The merchant accounts for this sales channel that are associated with the donation campaign. |
| `present_card_timeout_ms` | `int` | Optional | Required if `donationFlow` is set to **twoStep**. The time, in milliseconds, that the terminal waits for the shopper to present their card. Defaults to **10000** (10 seconds). Range: 5000 to 15000. |
| `prompt_timeout_ms` | `int` | Optional | The time, in milliseconds, that the terminal waits for the shopper to make a selection on the donation screen. Defaults to **10000** (10 seconds). Range: 5000 to 15000. |
| `store_ids` | `List[str]` | Optional | The Adyen-generated unique identifiers of stores for this sales channel that are associated with the donation campaign. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.display_text_field_2 import DisplayTextField2
from adyen.models.donation_amount import DonationAmount
from adyen.models.donation_flow_1 import DonationFlow1
from adyen.models.donation_type_1 import DonationType1
from adyen.models.in_person_donation_settings import InPersonDonationSettings

in_person_donation_settings = InPersonDonationSettings(
    display_text_field=DisplayTextField2.CAUSENAME,
    donation_flow=DonationFlow1.ONESTEP,
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
    donation_type=DonationType1.FIXEDAMOUNTSROUNDUP,
    merchant_accounts=[
        'merchantAccounts2',
        'merchantAccounts1'
    ],
    present_card_timeout_ms=48,
    prompt_timeout_ms=12,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

