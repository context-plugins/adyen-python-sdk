
# Donation Campaigns Response

## Structure

`DonationCampaignsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `donation_campaigns` | [`List[DonationCampaign]`](../../doc/models/donation-campaign.md) | Optional | List of active donation campaigns for your merchant account. |

## Example

```python
from adyen.models.amounts_1 import Amounts1
from adyen.models.donation_1 import Donation1
from adyen.models.donation_campaign import DonationCampaign
from adyen.models.donation_campaigns_response import DonationCampaignsResponse

donation_campaigns_response = DonationCampaignsResponse(
    donation_campaigns=[
        DonationCampaign(
            amounts=Amounts1(
                currency='currency6',
                values=[
                    48,
                    49
                ]
            ),
            banner_url='bannerUrl0',
            campaign_name='campaignName2',
            cause_name='causeName6',
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
        ),
        DonationCampaign(
            amounts=Amounts1(
                currency='currency6',
                values=[
                    48,
                    49
                ]
            ),
            banner_url='bannerUrl0',
            campaign_name='campaignName2',
            cause_name='causeName6',
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
        ),
        DonationCampaign(
            amounts=Amounts1(
                currency='currency6',
                values=[
                    48,
                    49
                ]
            ),
            banner_url='bannerUrl0',
            campaign_name='campaignName2',
            cause_name='causeName6',
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
    ]
)
```

