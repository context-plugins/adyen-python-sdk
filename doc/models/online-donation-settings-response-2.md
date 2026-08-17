
# Online Donation Settings Response 2

The settings for online donations collected as part of the campaign.

## Structure

`OnlineDonationSettingsResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amounts` | [`List[DonationAmount]`](../../doc/models/donation-amount.md) | Optional | The currency and fixed amounts for donations. We automatically add calculated amounts in other currencies for participating stores that use a different currency than the default. |
| `default_currency` | `str` | Optional | The currency that was used in the request to set fixed donation amounts. Format: three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes). |
| `donation_type` | [`DonationType1Enum`](../../doc/models/donation-type-1-enum.md) | Optional | The type of donation to collect from the shopper. Possible values:<br><br>- **roundup**: Round up the transaction amount.<br><br>- **fixedAmounts**: Choose a fixed amount.<br><br>- **fixedAmountsRoundup**: Round up, or choose a fixed amount. |
| `merchant_accounts` | `List[str]` | Optional | The merchant accounts for this sales channel that are associated with the donation campaign. |
| `store_ids` | `List[str]` | Optional | The Adyen-generated unique identifiers of stores for this sales channel that are associated with the donation campaign. |

## Example

```python
from adyen.models.donation_amount import DonationAmount
from adyen.models.donation_type_1_enum import DonationType1Enum
from adyen.models.online_donation_settings_response_2 import OnlineDonationSettingsResponse2

online_donation_settings_response_2 = OnlineDonationSettingsResponse2(
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
        )
    ],
    default_currency='defaultCurrency4',
    donation_type=DonationType1Enum.ROUNDUP,
    merchant_accounts=[
        'merchantAccounts8'
    ],
    store_ids=[
        'storeIds3',
        'storeIds4'
    ]
)
```

