
# Donation Campaigns Response

*This model accepts additional fields of type Any.*

## Structure

`DonationCampaignsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `donation_campaigns` | [`List[DonationCampaign]`](../../doc/models/donation-campaign.md) | Optional | List of active donation campaigns for your merchant account. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amounts import Amounts
from adyen.models.donation import Donation
from adyen.models.donation_campaign import DonationCampaign
from adyen.models.donation_campaigns_response import DonationCampaignsResponse

donation_campaigns_response = DonationCampaignsResponse(
    donation_campaigns=[
        DonationCampaign(
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
            banner_url='bannerUrl0',
            campaign_name='campaignName2',
            cause_name='causeName6',
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
        ),
        DonationCampaign(
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
            banner_url='bannerUrl0',
            campaign_name='campaignName2',
            cause_name='causeName6',
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
        ),
        DonationCampaign(
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
            banner_url='bannerUrl0',
            campaign_name='campaignName2',
            cause_name='causeName6',
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

