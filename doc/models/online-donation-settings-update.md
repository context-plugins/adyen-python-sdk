
# Online Donation Settings Update

## Structure

`OnlineDonationSettingsUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `default_amount` | [DonationAmountUpdate](../../doc/models/donation-amount-update.md) \| None | Optional | This is a container for one-of cases. |
| `donation_type` | [DonationType](../../doc/models/donation-type-enum.md) \| None | Optional | This is a container for one-of cases. |
| `merchant_accounts` | `List[str]` | Optional | The merchant accounts for this sales channel that are associated with the donation campaign. |
| `store_ids` | `List[str]` | Optional | The Adyen-generated unique identifiers of stores for this sales channel that are associated with the donation campaign. |

## Example

```python
from adyen.models.donation_amount_update import DonationAmountUpdate
from adyen.models.donation_type_enum import DonationTypeEnum
from adyen.models.online_donation_settings_update import OnlineDonationSettingsUpdate

online_donation_settings_update = OnlineDonationSettingsUpdate(
    default_amount=DonationAmountUpdate(
        amounts=[
            40
        ],
        currency_code='currencyCode2'
    ),
    donation_type=DonationTypeEnum.ROUNDUP,
    merchant_accounts=[
        'merchantAccounts6',
        'merchantAccounts7',
        'merchantAccounts8'
    ],
    store_ids=[
        'storeIds1',
        'storeIds2'
    ]
)
```

