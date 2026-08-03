
# Custom Header Signature



Documentation for accessing and setting credentials for ApiKeyAuth.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| X-API-Key | `str` | - | `x_api_key` |



**Note:** Auth credentials can be set using `ApiKeyAuthCredentials` object, passed in as named parameter `api_key_auth_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from adyen.adyen_client import AdyenClient
from adyen.http.auth.api_key_auth import ApiKeyAuthCredentials

client = AdyenClient(
    api_key_auth_credentials=ApiKeyAuthCredentials(
        x_api_key='X-API-Key'
    )
)
```


