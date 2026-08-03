
# Donation Campaign Request

*This model accepts additional fields of type Any.*

## Structure

`DonationCampaignRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_ids` | `List[str]` | Optional | The unique identifiers of the account holders associated with the donation campaign. |
| `in_person` | [`InPersonDonationSettings`](../../doc/models/in-person-donation-settings.md) | Optional | - |
| `name` | `str` | Required | The name of the donation campaign.<br><br>**Constraints**: *Minimum Length*: `1` |
| `nonprofit_cause_id` | `str` | Required | The unique identifier of the nonprofit cause that the campaign supports.<br><br>**Constraints**: *Minimum Length*: `1` |
| `online` | [`OnlineDonationSettings`](../../doc/models/online-donation-settings.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.display_text_field_2 import DisplayTextField2
from adyen.models.donation_amount import DonationAmount
from adyen.models.donation_campaign_request import DonationCampaignRequest
from adyen.models.donation_flow_1 import DonationFlow1
from adyen.models.donation_type_1 import DonationType1
from adyen.models.in_person_donation_settings import InPersonDonationSettings
from adyen.models.online_donation_settings import OnlineDonationSettings

donation_campaign_request = DonationCampaignRequest(
    name='name6',
    nonprofit_cause_id='nonprofitCauseId0',
    account_holder_ids=[
        'accountHolderIds1',
        'accountHolderIds2',
        'accountHolderIds3'
    ],
    in_person=InPersonDonationSettings(
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
            'merchantAccounts6',
            'merchantAccounts5',
            'merchantAccounts4'
        ],
        present_card_timeout_ms=102,
        prompt_timeout_ms=66,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    online=OnlineDonationSettings(
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
        donation_type=DonationType1.FIXEDAMOUNTS,
        merchant_accounts=[
            'merchantAccounts4',
            'merchantAccounts3',
            'merchantAccounts2'
        ],
        store_ids=[
            'storeIds9',
            'storeIds0',
            'storeIds1'
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

