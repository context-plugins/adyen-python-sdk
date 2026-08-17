
# Donation Campaign Update

## Structure

`DonationCampaignUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_ids` | `List[str]` | Optional | The unique identifiers of the account holders associated with the donation campaign. |
| `in_person` | [InPersonDonationSettingsUpdate](../../doc/models/in-person-donation-settings-update.md) \| None | Optional | This is a container for one-of cases. |
| `name` | `str` | Optional | The name of the donation campaign.<br><br>**Constraints**: *Minimum Length*: `1` |
| `online` | [OnlineDonationSettingsUpdate](../../doc/models/online-donation-settings-update.md) \| None | Optional | This is a container for one-of cases. |

## Example

```python
from adyen.models.display_text_field_2_enum import DisplayTextField2Enum
from adyen.models.donation_amount_update import DonationAmountUpdate
from adyen.models.donation_campaign_update import DonationCampaignUpdate
from adyen.models.donation_flow_1_enum import DonationFlow1Enum
from adyen.models.donation_type_enum import DonationTypeEnum
from adyen.models.in_person_donation_settings_update import InPersonDonationSettingsUpdate
from adyen.models.online_donation_settings_update import OnlineDonationSettingsUpdate

donation_campaign_update = DonationCampaignUpdate(
    account_holder_ids=[
        'accountHolderIds7',
        'accountHolderIds8'
    ],
    in_person=InPersonDonationSettingsUpdate(
        default_amount=DonationAmountUpdate(
            amounts=[
                40
            ],
            currency_code='currencyCode2'
        ),
        display_text_field=DisplayTextField2Enum.CAUSENAME,
        donation_flow=DonationFlow1Enum.ONESTEP,
        donation_type=DonationTypeEnum.FIXEDAMOUNTSROUNDUP,
        merchant_accounts=[
            'merchantAccounts4'
        ]
    ),
    name='name2',
    online=OnlineDonationSettingsUpdate(
        default_amount=DonationAmountUpdate(
            amounts=[
                40
            ],
            currency_code='currencyCode2'
        ),
        donation_type=DonationTypeEnum.ROUNDUP,
        merchant_accounts=[
            'merchantAccounts6',
            'merchantAccounts5',
            'merchantAccounts4'
        ],
        store_ids=[
            'storeIds1',
            'storeIds2',
            'storeIds3'
        ]
    )
)
```

