
# Company 2

## Structure

`Company2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`CompanyLinks2`](../../doc/models/company-links-2.md) | Optional | References to resources connected with this company. |
| `data_centers` | [`List[DataCenter]`](../../doc/models/data-center.md) | Optional | List of available data centers.<br><br>Adyen has several data centers around the world.In the URL that you use for making API requests, we recommend you use the live URL prefix from the data center closest to your shoppers. |
| `description` | `str` | Optional | Your description for the company account, maximum 300 characters |
| `id` | `str` | Optional | The unique identifier of the company account. |
| `name` | `str` | Optional | The legal or trading name of the company. |
| `reference` | `str` | Optional | Your reference to the account |
| `status` | `str` | Optional | The status of the company account.<br><br>Possible values:<br><br>* **Active**: Users can log in. Processing and payout capabilities depend on the status of the merchant account.<br>* **Inactive**: Users can log in. Payment processing and payouts are disabled.<br>* **Closed**: The company account is closed and this cannot be reversed. Users cannot log in. Payment processing and payouts are disabled. |

## Example

```python
from adyen.models.company_2 import Company2
from adyen.models.company_links_2 import CompanyLinks2
from adyen.models.data_center import DataCenter
from adyen.models.links_element import LinksElement
from adyen.models.links_element_6 import LinksElement6

company_2 = Company2(
    links=CompanyLinks2(
        mself=LinksElement6(
            href='href0'
        ),
        api_credentials=LinksElement(
            href='href8'
        ),
        users=LinksElement(
            href='href8'
        ),
        webhooks=LinksElement(
            href='href8'
        )
    ),
    data_centers=[
        DataCenter(
            live_prefix='livePrefix4',
            name='name6'
        ),
        DataCenter(
            live_prefix='livePrefix4',
            name='name6'
        ),
        DataCenter(
            live_prefix='livePrefix4',
            name='name6'
        )
    ],
    description='description2',
    id='id8',
    name='name8'
)
```

