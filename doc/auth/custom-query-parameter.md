
# Custom Query Parameter



Documentation for accessing and setting credentials for clientKey.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| clientKey | `str` | - | `client_key` |



**Note:** Auth credentials can be set using `ClientKeyCredentials` object, passed in as named parameter `client_key_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from adyen.adyen_client import AdyenClient
from adyen.http.auth.client_key import ClientKeyCredentials

client = AdyenClient(
    client_key_credentials=ClientKeyCredentials(
        client_key='clientKey'
    )
)
```


