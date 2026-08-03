
# List Nonprofits Response

*This model accepts additional fields of type Any.*

## Structure

`ListNonprofitsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`PaginationLinks`](../../doc/models/pagination-links.md) | Optional | - |
| `items_total` | `int` | Required | Total number of items. |
| `nonprofits` | [`List[Nonprofit]`](../../doc/models/nonprofit.md) | Optional | The supported nonprofit organizations. |
| `pages_total` | `int` | Required | Total number of pages. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.first import First
from adyen.models.last import Last
from adyen.models.list_nonprofits_response import ListNonprofitsResponse
from adyen.models.mself import Self
from adyen.models.next import Next
from adyen.models.nonprofit import Nonprofit
from adyen.models.nonprofit_cause import NonprofitCause
from adyen.models.pagination_links import PaginationLinks
from adyen.models.prev import Prev

list_nonprofits_response = ListNonprofitsResponse(
    items_total=8,
    pages_total=226,
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
    nonprofits=[
        Nonprofit(
            causes=[
                NonprofitCause(
                    banner_url='bannerUrl6',
                    description='description6',
                    locales=[
                        'locales6',
                        'locales7'
                    ],
                    name='name6',
                    id='id6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            description='description8',
            goals=[
                'goals3',
                'goals4',
                'goals5'
            ],
            locales=[
                'locales8',
                'locales9'
            ],
            logo_url='logoUrl8',
            name='name8',
            regions=[
                'regions3',
                'regions4'
            ],
            terms_and_conditions_url='termsAndConditionsUrl6',
            website='website4',
            id='id8',
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

