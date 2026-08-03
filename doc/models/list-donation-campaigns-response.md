
# List Donation Campaigns Response

*This model accepts additional fields of type Any.*

## Structure

`ListDonationCampaignsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`PaginationLinks`](../../doc/models/pagination-links.md) | Optional | - |
| `campaigns` | [`List[DonationCampaign1]`](../../doc/models/donation-campaign-1.md) | Optional | The list of donation campaigns. |
| `items_total` | `int` | Required | Total number of items. |
| `pages_total` | `int` | Required | Total number of pages. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.display_text_field_1 import DisplayTextField1
from adyen.models.donation_amount import DonationAmount
from adyen.models.donation_campaign_1 import DonationCampaign1
from adyen.models.donation_campaign_nonprofit_cause import DonationCampaignNonprofitCause
from adyen.models.donation_campaign_status_2 import DonationCampaignStatus2
from adyen.models.donation_flow_4 import DonationFlow4
from adyen.models.donation_type_1 import DonationType1
from adyen.models.first import First
from adyen.models.in_person_donation_settings_response import InPersonDonationSettingsResponse
from adyen.models.last import Last
from adyen.models.list_donation_campaigns_response import ListDonationCampaignsResponse
from adyen.models.mself import Self
from adyen.models.next import Next
from adyen.models.online_donation_settings_response import OnlineDonationSettingsResponse
from adyen.models.pagination_links import PaginationLinks
from adyen.models.prev import Prev

list_donation_campaigns_response = ListDonationCampaignsResponse(
    items_total=224,
    pages_total=70,
    links=PaginationLinks(
        first=First(
            href='href2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        last=Last(
            href='href2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        mself=Self(
            href='href0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        next=Next(
            href='href4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        prev=Prev(
            href='href8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    campaigns=[
        DonationCampaign1(
            id='id6',
            name='name6',
            nonprofit_cause=DonationCampaignNonprofitCause(
                banner_url='bannerUrl4',
                cause_id='causeId0',
                description='description4',
                global_website_url='globalWebsiteUrl6',
                goals=[
                    'goals9'
                ],
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            status=DonationCampaignStatus2.ACTIVE,
            account_holder_ids=[
                'accountHolderIds1',
                'accountHolderIds2',
                'accountHolderIds3'
            ],
            activated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            ended_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            in_person=InPersonDonationSettingsResponse(
                amounts=[
                    DonationAmount(
                        amounts=[
                            48,
                            49,
                            50
                        ],
                        currency_code='currencyCode6',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    )
                ],
                default_currency='defaultCurrency0',
                display_text_field=DisplayTextField1.CAUSENAME,
                donation_flow=DonationFlow4.ONESTEP,
                donation_type=DonationType1.FIXEDAMOUNTSROUNDUP,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            online=OnlineDonationSettingsResponse(
                amounts=[
                    DonationAmount(
                        amounts=[
                            48,
                            49,
                            50
                        ],
                        currency_code='currencyCode6',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    DonationAmount(
                        amounts=[
                            48,
                            49,
                            50
                        ],
                        currency_code='currencyCode6',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    DonationAmount(
                        amounts=[
                            48,
                            49,
                            50
                        ],
                        currency_code='currencyCode6',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    )
                ],
                default_currency='defaultCurrency0',
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

