
# Create Company Api Credential Request

*This model accepts additional fields of type Any.*

## Structure

`CreateCompanyApiCredentialRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed_origins` | `List[str]` | Optional | List of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) for the new API credential. |
| `associated_merchant_accounts` | `List[str]` | Optional | List of merchant accounts that the API credential has access to. |
| `description` | `str` | Optional | Description of the API credential. |
| `roles` | `List[str]` | Optional | List of [roles](https://docs.adyen.com/development-resources/api-credentials#roles-1) for the API credential. Only roles assigned to 'ws@Company.<CompanyName>' can be assigned to other API credentials. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.create_company_api_credential_request import CreateCompanyApiCredentialRequest

create_company_api_credential_request = CreateCompanyApiCredentialRequest(
    allowed_origins=[
        'allowedOrigins8'
    ],
    associated_merchant_accounts=[
        'associatedMerchantAccounts4',
        'associatedMerchantAccounts5',
        'associatedMerchantAccounts6'
    ],
    description='description6',
    roles=[
        'roles2'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

