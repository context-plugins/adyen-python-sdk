
# List Donation Campaigns Response

## Structure

`ListDonationCampaignsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`PaginationLinks1`](../../doc/models/pagination-links-1.md) | Optional | Pagination references. |
| `campaigns` | [`List[DonationCampaign1]`](../../doc/models/donation-campaign-1.md) | Optional | The list of donation campaigns. |
| `items_total` | `int` | Required | Total number of items. |
| `pages_total` | `int` | Required | Total number of pages. |

## Example

```python
from adyen.models.display_text_field_1_enum import DisplayTextField1Enum
from adyen.models.donation_amount import DonationAmount
from adyen.models.donation_campaign_1 import DonationCampaign1
from adyen.models.donation_campaign_nonprofit_cause_2 import DonationCampaignNonprofitCause2
from adyen.models.donation_campaign_status_2_enum import DonationCampaignStatus2Enum
from adyen.models.donation_flow_4_enum import DonationFlow4Enum
from adyen.models.donation_type_1_enum import DonationType1Enum
from adyen.models.in_person_donation_settings_response_2 import InPersonDonationSettingsResponse2
from adyen.models.links_element_10 import LinksElement10
from adyen.models.links_element_11 import LinksElement11
from adyen.models.links_element_12 import LinksElement12
from adyen.models.links_element_13 import LinksElement13
from adyen.models.links_element_9 import LinksElement9
from adyen.models.list_donation_campaigns_response import ListDonationCampaignsResponse
from adyen.models.online_donation_settings_response_2 import OnlineDonationSettingsResponse2
from adyen.models.pagination_links_1 import PaginationLinks1

list_donation_campaigns_response = ListDonationCampaignsResponse(
    items_total=224,
    pages_total=70,
    links=PaginationLinks1(
        first=LinksElement9(
            href='href2'
        ),
        last=LinksElement10(
            href='href2'
        ),
        mself=LinksElement13(
            href='href0'
        ),
        next=LinksElement11(
            href='href4'
        ),
        prev=LinksElement12(
            href='href8'
        )
    ),
    campaigns=[
        DonationCampaign1(
            id=None,
            name='name6',
            nonprofit_cause=DonationCampaignNonprofitCause2(
                banner_url='bannerUrl4',
                cause_id='causeId0',
                description='description4',
                global_website_url='globalWebsiteUrl6',
                goals=[
                    'goals9'
                ]
            ),
            status=DonationCampaignStatus2Enum.ACTIVE,
            account_holder_ids=[
                'accountHolderIds1',
                'accountHolderIds2',
                'accountHolderIds3'
            ],
            in_person=InPersonDonationSettingsResponse2(
                amounts=[
                    DonationAmount(
                        amounts=[
                            48,
                            49,
                            50
                        ],
                        currency_code='currencyCode6'
                    )
                ],
                default_currency='defaultCurrency0',
                display_text_field=DisplayTextField1Enum.CAUSENAME,
                donation_flow=DonationFlow4Enum.ONESTEP,
                donation_type=DonationType1Enum.FIXEDAMOUNTSROUNDUP
            ),
            online=OnlineDonationSettingsResponse2(
                amounts=[
                    DonationAmount(
                        amounts=[
                            48,
                            49,
                            50
                        ],
                        currency_code='currencyCode6'
                    ),
                    DonationAmount(
                        amounts=[
                            48,
                            49,
                            50
                        ],
                        currency_code='currencyCode6'
                    ),
                    DonationAmount(
                        amounts=[
                            48,
                            49,
                            50
                        ],
                        currency_code='currencyCode6'
                    )
                ],
                default_currency='defaultCurrency0',
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
    ]
)
```

