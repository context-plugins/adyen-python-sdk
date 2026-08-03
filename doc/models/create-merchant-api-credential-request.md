
# Create Merchant Api Credential Request

*This model accepts additional fields of type Any.*

## Structure

`CreateMerchantApiCredentialRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed_origins` | `List[str]` | Optional | The list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) for the new API credential. |
| `description` | `str` | Optional | Description of the API credential. |
| `roles` | `List[str]` | Optional | List of [roles](https://docs.adyen.com/development-resources/api-credentials#roles-1) for the API credential. Only roles assigned to 'ws@Company.<CompanyName>' can be assigned to other API credentials. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.create_merchant_api_credential_request import CreateMerchantApiCredentialRequest

create_merchant_api_credential_request = CreateMerchantApiCredentialRequest(
    allowed_origins=[
        'allowedOrigins2',
        'allowedOrigins3',
        'allowedOrigins4'
    ],
    description='description8',
    roles=[
        'roles0',
        'roles9',
        'roles8'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

