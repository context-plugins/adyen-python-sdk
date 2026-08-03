
# List Company Api Credentials Response

*This model accepts additional fields of type Any.*

## Structure

`ListCompanyApiCredentialsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`PaginationLinks`](../../doc/models/pagination-links.md) | Optional | - |
| `data` | [`List[CompanyApiCredential]`](../../doc/models/company-api-credential.md) | Optional | The list of API credentials. |
| `items_total` | `int` | Required | Total number of items. |
| `pages_total` | `int` | Required | Total number of pages. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.allowed_origin import AllowedOrigin
from adyen.models.allowed_origins import AllowedOrigins
from adyen.models.api_credential_links import ApiCredentialLinks
from adyen.models.company_4 import Company4
from adyen.models.company_api_credential import CompanyApiCredential
from adyen.models.first import First
from adyen.models.generate_api_key import GenerateApiKey
from adyen.models.generate_client_key import GenerateClientKey
from adyen.models.last import Last
from adyen.models.links_2 import Links2
from adyen.models.list_company_api_credentials_response import ListCompanyApiCredentialsResponse
from adyen.models.merchant_1 import Merchant1
from adyen.models.mself import Self
from adyen.models.next import Next
from adyen.models.pagination_links import PaginationLinks
from adyen.models.prev import Prev

list_company_api_credentials_response = ListCompanyApiCredentialsResponse(
    items_total=46,
    pages_total=248,
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
    data=[
        CompanyApiCredential(
            active=False,
            allowed_ip_addresses=[
                'allowedIpAddresses5'
            ],
            client_key='clientKey6',
            id='id0',
            roles=[
                'roles8'
            ],
            username='username0',
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
                )
            ],
            associated_merchant_accounts=[
                'associatedMerchantAccounts0',
                'associatedMerchantAccounts1',
                'associatedMerchantAccounts2'
            ],
            description='description0',
            subject_dn='subjectDN0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        CompanyApiCredential(
            active=False,
            allowed_ip_addresses=[
                'allowedIpAddresses5'
            ],
            client_key='clientKey6',
            id='id0',
            roles=[
                'roles8'
            ],
            username='username0',
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
                )
            ],
            associated_merchant_accounts=[
                'associatedMerchantAccounts0',
                'associatedMerchantAccounts1',
                'associatedMerchantAccounts2'
            ],
            description='description0',
            subject_dn='subjectDN0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        CompanyApiCredential(
            active=False,
            allowed_ip_addresses=[
                'allowedIpAddresses5'
            ],
            client_key='clientKey6',
            id='id0',
            roles=[
                'roles8'
            ],
            username='username0',
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
                )
            ],
            associated_merchant_accounts=[
                'associatedMerchantAccounts0',
                'associatedMerchantAccounts1',
                'associatedMerchantAccounts2'
            ],
            description='description0',
            subject_dn='subjectDN0',
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

