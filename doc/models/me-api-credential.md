
# Me Api Credential

## Structure

`MeApiCredential`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`ApiCredentialLinks2`](../../doc/models/api-credential-links-2.md) | Optional | References to resources linked to the API credential. |
| `active` | `bool` | Required | Indicates if the API credential is enabled. Must be set to **true** to use the credential in your integration. |
| `allowed_ip_addresses` | `List[str]` | Required | List of IP addresses from which your client can make requests.<br><br>If the list is empty, we allow requests from any IP.<br>If the list is not empty and we get a request from an IP which is not on the list, you get a security error. |
| `allowed_origins` | [`List[AllowedOrigin]`](../../doc/models/allowed-origin.md) | Optional | List containing the [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) linked to the API credential. |
| `client_key` | `str` | Required | Public key used for [client-side authentication](https://docs.adyen.com/development-resources/client-side-authentication). The client key is required for Drop-in and Components integrations. |
| `company_name` | `str` | Optional | Name of the company linked to the API credential. |
| `description` | `str` | Optional | Description of the API credential.<br><br>**Constraints**: *Maximum Length*: `50` |
| `id` | `str` | Required | Unique identifier of the API credential. |
| `roles` | `List[str]` | Required | List of [roles](https://docs.adyen.com/development-resources/api-credentials#roles-1) for the API credential. |
| `subject_dn` | `str` | Optional | The subject DN of the certificate issued by Adyen. |
| `username` | `str` | Required | The name of the [API credential](https://docs.adyen.com/development-resources/api-credentials), for example **ws@Company.TestCompany**. |

## Example

```python
from adyen.models.allowed_origin import AllowedOrigin
from adyen.models.api_credential_links_2 import ApiCredentialLinks2
from adyen.models.links_2 import Links2
from adyen.models.links_element_1 import LinksElement1
from adyen.models.links_element_2 import LinksElement2
from adyen.models.links_element_3 import LinksElement3
from adyen.models.links_element_4 import LinksElement4
from adyen.models.links_element_5 import LinksElement5
from adyen.models.links_element_6 import LinksElement6
from adyen.models.me_api_credential import MeApiCredential

me_api_credential = MeApiCredential(
    active=False,
    allowed_ip_addresses=[
        'allowedIpAddresses3',
        'allowedIpAddresses4'
    ],
    client_key='clientKey8',
    id='id8',
    roles=[
        'roles2',
        'roles1',
        'roles0'
    ],
    username='username8',
    links=ApiCredentialLinks2(
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
    ),
    allowed_origins=[
        AllowedOrigin(
            domain='domain0',
            links=Links2(
                mself=LinksElement6(
                    href='href0'
                )
            ),
            id='id4'
        ),
        AllowedOrigin(
            domain='domain0',
            links=Links2(
                mself=LinksElement6(
                    href='href0'
                )
            ),
            id='id4'
        )
    ],
    company_name='companyName0',
    description='description8',
    subject_dn='subjectDN8'
)
```

