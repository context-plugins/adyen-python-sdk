
# Webhook Links

*This model accepts additional fields of type Any.*

## Structure

`WebhookLinks`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company` | [`Company4`](../../doc/models/company-4.md) | Optional | - |
| `generate_hmac` | [`GenerateHmac`](../../doc/models/generate-hmac.md) | Required | - |
| `merchant` | [`Merchant1`](../../doc/models/merchant-1.md) | Optional | - |
| `mself` | [`Self`](../../doc/models/self.md) | Required | - |
| `test_webhook` | [`TestWebhook`](../../doc/models/test-webhook.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.company_4 import Company4
from adyen.models.generate_hmac import GenerateHmac
from adyen.models.merchant_1 import Merchant1
from adyen.models.mself import Self
from adyen.models.test_webhook import TestWebhook
from adyen.models.webhook_links import WebhookLinks

webhook_links = WebhookLinks(
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
)
```

