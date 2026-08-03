
# Me Api Credential

*This model accepts additional fields of type Any.*

## Structure

`MeApiCredential`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`ApiCredentialLinks`](../../doc/models/api-credential-links.md) | Optional | - |
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
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.allowed_origin import AllowedOrigin
from adyen.models.allowed_origins import AllowedOrigins
from adyen.models.api_credential_links import ApiCredentialLinks
from adyen.models.company_4 import Company4
from adyen.models.generate_api_key import GenerateApiKey
from adyen.models.generate_client_key import GenerateClientKey
from adyen.models.links_2 import Links2
from adyen.models.me_api_credential import MeApiCredential
from adyen.models.merchant_1 import Merchant1
from adyen.models.mself import Self

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
    links=ApiCredentialLinks(
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
    ),
    allowed_origins=[
        AllowedOrigin(
            domain='domain0',
            links=Links2(
                mself=Self(
                    href='href0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            id='id4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        AllowedOrigin(
            domain='domain0',
            links=Links2(
                mself=Self(
                    href='href0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            id='id4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    company_name='companyName0',
    description='description8',
    subject_dn='subjectDN8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

