
# Donation Campaign

## Structure

`DonationCampaign`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amounts` | [`Amounts1`](../../doc/models/amounts-1.md) | Optional | The object that contains the fixed donation amounts that the shopper can select from. |
| `banner_url` | `str` | Optional | The URL for the banner of the nonprofit or campaign. |
| `campaign_name` | `str` | Optional | The name of the donation campaign.. |
| `cause_name` | `str` | Optional | The cause of the nonprofit. |
| `donation` | [`Donation1`](../../doc/models/donation-1.md) | Optional | The object that contains the details of the donation. |
| `id` | `str` | Optional | The unique campaign ID of the donation campaign. |
| `logo_url` | `str` | Optional | The URL for the logo of the nonprofit. |
| `nonprofit_description` | `str` | Optional | The description of the nonprofit. |
| `nonprofit_name` | `str` | Optional | The name of the nonprofit organization that receives the donation. |
| `nonprofit_url` | `str` | Optional | The website URL of the nonprofit. |
| `terms_and_conditions_url` | `str` | Optional | The URL of the terms and conditions page of the nonprofit and the campaign. |

## Example

```python
from adyen.models.amounts_1 import Amounts1
from adyen.models.donation_1 import Donation1
from adyen.models.donation_campaign import DonationCampaign

donation_campaign = DonationCampaign(
    amounts=Amounts1(
        currency='currency6',
        values=[
            48,
            49
        ]
    ),
    banner_url='bannerUrl2',
    campaign_name='campaignName4',
    cause_name='causeName8',
    donation=Donation1(
        currency='currency0',
        mtype='type0',
        donation_type='donationType2',
        max_roundup_amount=114,
        values=[
            106,
            105,
            104
        ]
    )
)
```

