
# Donation Campaign Request

## Structure

`DonationCampaignRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_ids` | `List[str]` | Optional | The unique identifiers of the account holders associated with the donation campaign. |
| `in_person` | [`InPersonDonationSettings2`](../../doc/models/in-person-donation-settings-2.md) | Optional | The settings for in-person donations collected as part of the campaign. |
| `name` | `str` | Required | The name of the donation campaign.<br><br>**Constraints**: *Minimum Length*: `1` |
| `nonprofit_cause_id` | `str` | Required | The unique identifier of the nonprofit cause that the campaign supports.<br><br>**Constraints**: *Minimum Length*: `1` |
| `online` | [`OnlineDonationSettings2`](../../doc/models/online-donation-settings-2.md) | Optional | The settings for online donations collected as part of the campaign. |

## Example

```python
from adyen.models.display_text_field_2_enum import DisplayTextField2Enum
from adyen.models.donation_amount_1 import DonationAmount1
from adyen.models.donation_campaign_request import DonationCampaignRequest
from adyen.models.donation_flow_1_enum import DonationFlow1Enum
from adyen.models.donation_type_1_enum import DonationType1Enum
from adyen.models.in_person_donation_settings_2 import InPersonDonationSettings2
from adyen.models.online_donation_settings_2 import OnlineDonationSettings2

donation_campaign_request = DonationCampaignRequest(
    name='name6',
    nonprofit_cause_id='nonprofitCauseId0',
    account_holder_ids=[
        'accountHolderIds1',
        'accountHolderIds2',
        'accountHolderIds3'
    ],
    in_person=InPersonDonationSettings2(
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
            'merchantAccounts6',
            'merchantAccounts5',
            'merchantAccounts4'
        ],
        present_card_timeout_ms=102,
        prompt_timeout_ms=66
    ),
    online=OnlineDonationSettings2(
        default_amount=DonationAmount1(
            amounts=[
                78,
                79,
                80
            ],
            currency_code='currencyCode6'
        ),
        donation_type=DonationType1Enum.FIXEDAMOUNTS,
        merchant_accounts=[
            'merchantAccounts4',
            'merchantAccounts3',
            'merchantAccounts2'
        ],
        store_ids=[
            'storeIds9',
            'storeIds0',
            'storeIds1'
        ]
    )
)
```

