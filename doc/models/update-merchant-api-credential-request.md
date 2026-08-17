
# Update Merchant Api Credential Request

## Structure

`UpdateMerchantApiCredentialRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `active` | `bool` | Optional | Indicates if the API credential is enabled. |
| `allowed_origins` | `List[str]` | Optional | The new list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) for the API credential. |
| `description` | `str` | Optional | Description of the API credential. |
| `roles` | `List[str]` | Optional | List of [roles](https://docs.adyen.com/development-resources/api-credentials#roles-1) for the API credential. Only roles assigned to 'ws@Company.<CompanyName>' can be assigned to other API credentials. |
| `subject_dn` | `str` | Optional | The subject DN of the certificate issued by Adyen. |

## Example

```python
from adyen.models.update_merchant_api_credential_request import UpdateMerchantApiCredentialRequest

update_merchant_api_credential_request = UpdateMerchantApiCredentialRequest(
    active=False,
    allowed_origins=[
        'allowedOrigins6',
        'allowedOrigins5'
    ],
    description='description0',
    roles=[
        'roles4',
        'roles3',
        'roles2'
    ],
    subject_dn='subjectDN0'
)
```

