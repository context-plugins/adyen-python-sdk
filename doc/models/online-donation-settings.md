
# Online Donation Settings

## Structure

`OnlineDonationSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `default_amount` | [`DonationAmount1`](../../doc/models/donation-amount-1.md) | Optional | The default amount for donations. |
| `donation_type` | [`DonationType1Enum`](../../doc/models/donation-type-1-enum.md) | Optional | The type of donation to collect from the shopper. Possible values:<br><br>- **roundup**: Round up the transaction amount.<br><br>- **fixedAmounts**: Choose a fixed amount.<br><br>- **fixedAmountsRoundup**: Round up, or choose a fixed amount. |
| `merchant_accounts` | `List[str]` | Optional | The merchant accounts for this sales channel that are associated with the donation campaign. |
| `store_ids` | `List[str]` | Optional | The Adyen-generated unique identifiers of stores for this sales channel that are associated with the donation campaign. |

## Example

```python
from adyen.models.donation_amount_1 import DonationAmount1
from adyen.models.donation_type_1_enum import DonationType1Enum
from adyen.models.online_donation_settings import OnlineDonationSettings

online_donation_settings = OnlineDonationSettings(
    default_amount=DonationAmount1(
        amounts=[
            78,
            79,
            80
        ],
        currency_code='currencyCode6'
    ),
    donation_type=DonationType1Enum.ROUNDUP,
    merchant_accounts=[
        'merchantAccounts4'
    ],
    store_ids=[
        'storeIds1',
        'storeIds2'
    ]
)
```

