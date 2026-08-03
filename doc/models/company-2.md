
# Company 2

*This model accepts additional fields of type Any.*

## Structure

`Company2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`CompanyLinks`](../../doc/models/company-links.md) | Optional | - |
| `data_centers` | [`List[DataCenter]`](../../doc/models/data-center.md) | Optional | List of available data centers.<br><br>Adyen has several data centers around the world.In the URL that you use for making API requests, we recommend you use the live URL prefix from the data center closest to your shoppers. |
| `description` | `str` | Optional | Your description for the company account, maximum 300 characters |
| `id` | `str` | Optional | The unique identifier of the company account. |
| `name` | `str` | Optional | The legal or trading name of the company. |
| `reference` | `str` | Optional | Your reference to the account |
| `status` | `str` | Optional | The status of the company account.<br><br>Possible values:<br><br>* **Active**: Users can log in. Processing and payout capabilities depend on the status of the merchant account.<br>* **Inactive**: Users can log in. Payment processing and payouts are disabled.<br>* **Closed**: The company account is closed and this cannot be reversed. Users cannot log in. Payment processing and payouts are disabled. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.company_2 import Company2
from adyen.models.company_links import CompanyLinks
from adyen.models.data_center import DataCenter
from adyen.models.href_2 import Href2
from adyen.models.mself import Self

company_2 = Company2(
    links=CompanyLinks(
        mself=Self(
            href='href0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        api_credentials=Href2(
            href='href8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        users=Href2(
            href='href8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        webhooks=Href2(
            href='href8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    data_centers=[
        DataCenter(
            live_prefix='livePrefix4',
            name='name6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        DataCenter(
            live_prefix='livePrefix4',
            name='name6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        DataCenter(
            live_prefix='livePrefix4',
            name='name6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    description='description2',
    id='id8',
    name='name8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

