
# List Webhooks Response

*This model accepts additional fields of type Any.*

## Structure

`ListWebhooksResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`PaginationLinks`](../../doc/models/pagination-links.md) | Optional | - |
| `account_reference` | `str` | Optional | Reference to the account. |
| `data` | [`List[Webhook]`](../../doc/models/webhook.md) | Optional | The list of webhooks configured for this account. |
| `items_total` | `int` | Required | Total number of items. |
| `pages_total` | `int` | Required | Total number of pages. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.communication_format import CommunicationFormat
from adyen.models.company_4 import Company4
from adyen.models.first import First
from adyen.models.generate_hmac import GenerateHmac
from adyen.models.last import Last
from adyen.models.list_webhooks_response import ListWebhooksResponse
from adyen.models.merchant_1 import Merchant1
from adyen.models.mself import Self
from adyen.models.next import Next
from adyen.models.pagination_links import PaginationLinks
from adyen.models.prev import Prev
from adyen.models.test_webhook import TestWebhook
from adyen.models.webhook import Webhook
from adyen.models.webhook_links import WebhookLinks

list_webhooks_response = ListWebhooksResponse(
    items_total=198,
    pages_total=160,
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
    account_reference='accountReference6',
    data=[
        Webhook(
            active=False,
            communication_format=CommunicationFormat.JSON,
            mtype='type0',
            url='url4',
            links=WebhookLinks(
                generate_hmac=GenerateHmac(
                    href='href6',
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
                test_webhook=TestWebhook(
                    href='href6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                company=Company4(
                    href='href2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                merchant=Merchant1(
                    href='href6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            accepts_expired_certificate=False,
            accepts_self_signed_certificate=False,
            accepts_untrusted_root_certificate=False,
            account_reference='accountReference2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Webhook(
            active=False,
            communication_format=CommunicationFormat.JSON,
            mtype='type0',
            url='url4',
            links=WebhookLinks(
                generate_hmac=GenerateHmac(
                    href='href6',
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
                test_webhook=TestWebhook(
                    href='href6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                company=Company4(
                    href='href2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                merchant=Merchant1(
                    href='href6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            accepts_expired_certificate=False,
            accepts_self_signed_certificate=False,
            accepts_untrusted_root_certificate=False,
            account_reference='accountReference2',
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

