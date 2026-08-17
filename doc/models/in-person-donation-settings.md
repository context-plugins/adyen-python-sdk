
# In Person Donation Settings

## Structure

`InPersonDonationSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `default_amount` | [`DonationAmount1`](../../doc/models/donation-amount-1.md) | Optional | The default amount for donations. |
| `display_text_field` | [`DisplayTextField2Enum`](../../doc/models/display-text-field-2-enum.md) | Required | The text shown on the payment terminal, either the name or the cause of the nonprofit organization. |
| `donation_flow` | [`DonationFlow1Enum`](../../doc/models/donation-flow-1-enum.md) | Required | The interaction flow for in-person donations. Possible values:<br><br>- **oneStep**: The shopper presents their payment method for the payment and the donation in one go, after the donation.<br><br>- **twoStep**: The shopper presents their payment method twice: after the payment and after the donation. |
| `donation_type` | [`DonationType1Enum`](../../doc/models/donation-type-1-enum.md) | Optional | The type of donation to collect from the shopper. Possible values:<br><br>- **roundup**: Round up the transaction amount.<br><br>- **fixedAmounts**: Choose a fixed amount.<br><br>- **fixedAmountsRoundup**: Round up, or choose a fixed amount. |
| `merchant_accounts` | `List[str]` | Optional | The merchant accounts for this sales channel that are associated with the donation campaign. |
| `present_card_timeout_ms` | `int` | Optional | Required if `donationFlow` is set to **twoStep**. The time, in milliseconds, that the terminal waits for the shopper to present their card. Defaults to **10000** (10 seconds). Range: 5000 to 15000. |
| `prompt_timeout_ms` | `int` | Optional | The time, in milliseconds, that the terminal waits for the shopper to make a selection on the donation screen. Defaults to **10000** (10 seconds). Range: 5000 to 15000. |
| `store_ids` | `List[str]` | Optional | The Adyen-generated unique identifiers of stores for this sales channel that are associated with the donation campaign. |

## Example

```python
from adyen.models.display_text_field_2_enum import DisplayTextField2Enum
from adyen.models.donation_amount_1 import DonationAmount1
from adyen.models.donation_flow_1_enum import DonationFlow1Enum
from adyen.models.donation_type_1_enum import DonationType1Enum
from adyen.models.in_person_donation_settings import InPersonDonationSettings

in_person_donation_settings = InPersonDonationSettings(
    display_text_field=DisplayTextField2Enum.CAUSENAME,
    donation_flow=DonationFlow1Enum.ONESTEP,
    default_amount=DonationAmount1(
        amounts=[
            78,
            79,
            80
        ],
        currency_code='currencyCode6'
    ),
    donation_type=DonationType1Enum.FIXEDAMOUNTSROUNDUP,
    merchant_accounts=[
        'merchantAccounts2',
        'merchantAccounts1'
    ],
    present_card_timeout_ms=48,
    prompt_timeout_ms=12
)
```

