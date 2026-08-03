
# Api Credential Links

*This model accepts additional fields of type Any.*

## Structure

`ApiCredentialLinks`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed_origins` | [`AllowedOrigins`](../../doc/models/allowed-origins.md) | Optional | - |
| `company` | [`Company4`](../../doc/models/company-4.md) | Optional | - |
| `generate_api_key` | [`GenerateApiKey`](../../doc/models/generate-api-key.md) | Optional | - |
| `generate_client_key` | [`GenerateClientKey`](../../doc/models/generate-client-key.md) | Optional | - |
| `merchant` | [`Merchant1`](../../doc/models/merchant-1.md) | Optional | - |
| `mself` | [`Self`](../../doc/models/self.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.allowed_origins import AllowedOrigins
from adyen.models.api_credential_links import ApiCredentialLinks
from adyen.models.company_4 import Company4
from adyen.models.generate_api_key import GenerateApiKey
from adyen.models.generate_client_key import GenerateClientKey
from adyen.models.merchant_1 import Merchant1
from adyen.models.mself import Self

api_credential_links = ApiCredentialLinks(
    mself=Self(
        href='href0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    allowed_origins=AllowedOrigins(
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
    generate_api_key=GenerateApiKey(
        href='href6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    generate_client_key=GenerateClientKey(
        href='href4',
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

