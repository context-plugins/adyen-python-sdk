
# Donation Campaign

*This model accepts additional fields of type Any.*

## Structure

`DonationCampaign`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amounts` | [`Amounts`](../../doc/models/amounts.md) | Optional | - |
| `banner_url` | `str` | Optional | The URL for the banner of the nonprofit or campaign. |
| `campaign_name` | `str` | Optional | The name of the donation campaign.. |
| `cause_name` | `str` | Optional | The cause of the nonprofit. |
| `donation` | [`Donation`](../../doc/models/donation.md) | Optional | - |
| `id` | `str` | Optional | The unique campaign ID of the donation campaign. |
| `logo_url` | `str` | Optional | The URL for the logo of the nonprofit. |
| `nonprofit_description` | `str` | Optional | The description of the nonprofit. |
| `nonprofit_name` | `str` | Optional | The name of the nonprofit organization that receives the donation. |
| `nonprofit_url` | `str` | Optional | The website URL of the nonprofit. |
| `terms_and_conditions_url` | `str` | Optional | The URL of the terms and conditions page of the nonprofit and the campaign. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amounts import Amounts
from adyen.models.donation import Donation
from adyen.models.donation_campaign import DonationCampaign

donation_campaign = DonationCampaign(
    amounts=Amounts(
        currency='currency6',
        values=[
            48,
            49
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    banner_url='bannerUrl2',
    campaign_name='campaignName4',
    cause_name='causeName8',
    donation=Donation(
        currency='currency0',
        mtype='type0',
        donation_type='donationType2',
        max_roundup_amount=114,
        values=[
            106,
            105,
            104
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

