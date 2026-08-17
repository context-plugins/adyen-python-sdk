
# List Company Api Credentials Response

## Structure

`ListCompanyApiCredentialsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`PaginationLinks1`](../../doc/models/pagination-links-1.md) | Optional | Pagination references. |
| `data` | [`List[CompanyApiCredential]`](../../doc/models/company-api-credential.md) | Optional | The list of API credentials. |
| `items_total` | `int` | Required | Total number of items. |
| `pages_total` | `int` | Required | Total number of pages. |

## Example

```python
from adyen.models.allowed_origin import AllowedOrigin
from adyen.models.api_credential_links_2 import ApiCredentialLinks2
from adyen.models.company_api_credential import CompanyApiCredential
from adyen.models.links_2 import Links2
from adyen.models.links_element_1 import LinksElement1
from adyen.models.links_element_10 import LinksElement10
from adyen.models.links_element_11 import LinksElement11
from adyen.models.links_element_12 import LinksElement12
from adyen.models.links_element_13 import LinksElement13
from adyen.models.links_element_2 import LinksElement2
from adyen.models.links_element_3 import LinksElement3
from adyen.models.links_element_4 import LinksElement4
from adyen.models.links_element_5 import LinksElement5
from adyen.models.links_element_6 import LinksElement6
from adyen.models.links_element_9 import LinksElement9
from adyen.models.list_company_api_credentials_response import ListCompanyApiCredentialsResponse
from adyen.models.pagination_links_1 import PaginationLinks1

list_company_api_credentials_response = ListCompanyApiCredentialsResponse(
    items_total=46,
    pages_total=248,
    links=PaginationLinks1(
        first=LinksElement9(
            href='href2'
        ),
        last=LinksElement10(
            href='href2'
        ),
        mself=LinksElement13(
            href='href0'
        ),
        next=LinksElement11(
            href='href4'
        ),
        prev=LinksElement12(
            href='href8'
        )
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
                )
            ],
            associated_merchant_accounts=[
                'associatedMerchantAccounts0',
                'associatedMerchantAccounts1',
                'associatedMerchantAccounts2'
            ],
            description='description0',
            subject_dn='subjectDN0'
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
                )
            ],
            associated_merchant_accounts=[
                'associatedMerchantAccounts0',
                'associatedMerchantAccounts1',
                'associatedMerchantAccounts2'
            ],
            description='description0',
            subject_dn='subjectDN0'
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
                )
            ],
            associated_merchant_accounts=[
                'associatedMerchantAccounts0',
                'associatedMerchantAccounts1',
                'associatedMerchantAccounts2'
            ],
            description='description0',
            subject_dn='subjectDN0'
        )
    ]
)
```

