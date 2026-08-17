
# In Person Donation Settings Response

## Structure

`InPersonDonationSettingsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amounts` | [`List[DonationAmount]`](../../doc/models/donation-amount.md) | Optional | The currency and fixed amounts for donations. We automatically add calculated amounts in other currencies for participating stores that use a different currency than the default. |
| `default_currency` | `str` | Optional | The currency that was used in the request to set fixed donation amounts. Format: three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes). |
| `display_text_field` | [`DisplayTextField1Enum`](../../doc/models/display-text-field-1-enum.md) | Optional | The text shown on the payment terminal, asking the shopper for a donation. |
| `donation_flow` | [`DonationFlow4Enum`](../../doc/models/donation-flow-4-enum.md) | Optional | The interaction flow for in-person donations: complete payment for the purchase and the donation in one go, or separately. |
| `donation_type` | [`DonationType1Enum`](../../doc/models/donation-type-1-enum.md) | Optional | The type of donation to collect from the shopper. Possible values:<br><br>- **roundup**: Round up the transaction amount.<br><br>- **fixedAmounts**: Choose a fixed amount.<br><br>- **fixedAmountsRoundup**: Round up, or choose a fixed amount. |
| `merchant_accounts` | `List[str]` | Optional | The merchant accounts for this sales channel that are associated with the donation campaign. |
| `present_card_timeout_ms` | `int` | Optional | The time, in milliseconds, that the terminal waits for the shopper to present their card. |
| `prompt_timeout_ms` | `int` | Optional | The time, in milliseconds, that the terminal waits for the shopper to respond to the text asking for a donation. |
| `store_ids` | `List[str]` | Optional | The Adyen-generated unique identifiers of stores for this sales channel that are associated with the donation campaign. |

## Example

```python
from adyen.models.display_text_field_1_enum import DisplayTextField1Enum
from adyen.models.donation_amount import DonationAmount
from adyen.models.donation_flow_4_enum import DonationFlow4Enum
from adyen.models.donation_type_1_enum import DonationType1Enum
from adyen.models.in_person_donation_settings_response import InPersonDonationSettingsResponse

in_person_donation_settings_response = InPersonDonationSettingsResponse(
    amounts=[
        DonationAmount(
            amounts=[
                48,
                49,
                50
            ],
            currency_code='currencyCode6'
        ),
        DonationAmount(
            amounts=[
                48,
                49,
                50
            ],
            currency_code='currencyCode6'
        ),
        DonationAmount(
            amounts=[
                48,
                49,
                50
            ],
            currency_code='currencyCode6'
        )
    ],
    default_currency='defaultCurrency8',
    display_text_field=DisplayTextField1Enum.CAUSENAME,
    donation_flow=DonationFlow4Enum.ONESTEP,
    donation_type=DonationType1Enum.FIXEDAMOUNTS
)
```

