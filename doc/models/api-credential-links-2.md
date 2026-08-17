
# Api Credential Links 2

References to resources linked to the API credential.

## Structure

`ApiCredentialLinks2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed_origins` | [`LinksElement1`](../../doc/models/links-element-1.md) | Optional | List of allowed origins. |
| `company` | [`LinksElement2`](../../doc/models/links-element-2.md) | Optional | Company account that the API credential is linked to. Only present for company-level webhooks. |
| `generate_api_key` | [`LinksElement3`](../../doc/models/links-element-3.md) | Optional | Generates a new API key. When you generate a new one, the existing key remains valid for 24 hours. |
| `generate_client_key` | [`LinksElement4`](../../doc/models/links-element-4.md) | Optional | Generates a new client key, used to authenticate client-side requests. When you generate a new one, the existing key remains valid for 24 hours. |
| `merchant` | [`LinksElement5`](../../doc/models/links-element-5.md) | Optional | The merchant account that the API credential is linked to. Only present for merchant-level API credentials. |
| `mself` | [`LinksElement6`](../../doc/models/links-element-6.md) | Required | Link to the resource itself. |

## Example

```python
from adyen.models.api_credential_links_2 import ApiCredentialLinks2
from adyen.models.links_element_1 import LinksElement1
from adyen.models.links_element_2 import LinksElement2
from adyen.models.links_element_3 import LinksElement3
from adyen.models.links_element_4 import LinksElement4
from adyen.models.links_element_5 import LinksElement5
from adyen.models.links_element_6 import LinksElement6

api_credential_links_2 = ApiCredentialLinks2(
    mself=LinksElement6(
        href='href0'
    ),
    allowed_origins=LinksElement1(
        href='href6'
    ),
    company=LinksElement2(
        href='href2'
    ),
    generate_api_key=LinksElement3(
        href='href6'
    ),
    generate_client_key=LinksElement4(
        href='href4'
    ),
    merchant=LinksElement5(
        href='href6'
    )
)
```

