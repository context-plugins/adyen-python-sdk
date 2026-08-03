
# Donation Campaign Update

*This model accepts additional fields of type Any.*

## Structure

`DonationCampaignUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_ids` | `List[str]` | Optional | The unique identifiers of the account holders associated with the donation campaign. |
| `in_person` | [InPersonDonationSettingsUpdate](../../doc/models/in-person-donation-settings-update.md) \| Any \| None | Optional | This is a container for one-of cases. |
| `name` | `str` | Optional | The name of the donation campaign.<br><br>**Constraints**: *Minimum Length*: `1` |
| `online` | [OnlineDonationSettingsUpdate](../../doc/models/online-donation-settings-update.md) \| Any \| None | Optional | This is a container for one-of cases. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.display_text_field_2 import DisplayTextField2
from adyen.models.donation_amount_update import DonationAmountUpdate
from adyen.models.donation_campaign_update import DonationCampaignUpdate
from adyen.models.donation_flow_1 import DonationFlow1
from adyen.models.donation_type import DonationType
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
            currency_code='currencyCode2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        display_text_field=DisplayTextField2.CAUSENAME,
        donation_flow=DonationFlow1.ONESTEP,
        donation_type=DonationType.FIXEDAMOUNTSROUNDUP,
        merchant_accounts=[
            'merchantAccounts4'
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    name='name2',
    online=OnlineDonationSettingsUpdate(
        default_amount=DonationAmountUpdate(
            amounts=[
                40
            ],
            currency_code='currencyCode2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        donation_type=DonationType.ROUNDUP,
        merchant_accounts=[
            'merchantAccounts6',
            'merchantAccounts5',
            'merchantAccounts4'
        ],
        store_ids=[
            'storeIds1',
            'storeIds2',
            'storeIds3'
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

