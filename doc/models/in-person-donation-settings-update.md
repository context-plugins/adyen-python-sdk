
# In Person Donation Settings Update

## Structure

`InPersonDonationSettingsUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `default_amount` | [DonationAmountUpdate](../../doc/models/donation-amount-update.md) \| None | Optional | This is a container for one-of cases. |
| `display_text_field` | [`DisplayTextField2Enum`](../../doc/models/display-text-field-2-enum.md) | Optional | The text shown on the payment terminal, either the name or the cause of the nonprofit organization. |
| `donation_flow` | [`DonationFlow1Enum`](../../doc/models/donation-flow-1-enum.md) | Optional | The interaction flow for in-person donations. Possible values:<br><br>- **oneStep**: The shopper presents their payment method for the payment and the donation in one go, after the donation.<br><br>- **twoStep**: The shopper presents their payment method twice: after the payment and after the donation. |
| `donation_type` | [DonationType](../../doc/models/donation-type-enum.md) \| None | Optional | This is a container for one-of cases. |
| `merchant_accounts` | `List[str]` | Optional | The merchant accounts for this sales channel that are associated with the donation campaign. |
| `present_card_timeout_ms` | `int` | Optional | Required if `donationFlow` is set to **twoStep**. The time, in milliseconds, that the terminal waits for the shopper to present their card. Defaults to **10000** (10 seconds). Range: 5000 to 15000. |
| `prompt_timeout_ms` | `int` | Optional | The time, in milliseconds, that the terminal waits for the shopper to make a selection on the donation screen. Defaults to **10000** (10 seconds). Range: 5000 to 15000. |
| `store_ids` | `List[str]` | Optional | The Adyen-generated unique identifiers of stores for this sales channel that are associated with the donation campaign. |

## Example

```python
from adyen.models.display_text_field_2_enum import DisplayTextField2Enum
from adyen.models.donation_amount_update import DonationAmountUpdate
from adyen.models.donation_flow_1_enum import DonationFlow1Enum
from adyen.models.donation_type_enum import DonationTypeEnum
from adyen.models.in_person_donation_settings_update import InPersonDonationSettingsUpdate

in_person_donation_settings_update = InPersonDonationSettingsUpdate(
    default_amount=DonationAmountUpdate(
        amounts=[
            40
        ],
        currency_code='currencyCode2'
    ),
    display_text_field=DisplayTextField2Enum.CAUSENAME,
    donation_flow=DonationFlow1Enum.ONESTEP,
    donation_type=DonationTypeEnum.FIXEDAMOUNTS,
    merchant_accounts=[
        'merchantAccounts0',
        'merchantAccounts9'
    ]
)
```

