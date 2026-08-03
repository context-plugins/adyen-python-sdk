# Networktokens

```python
networktokens_api = client.networktokens
```

## Class Name

`NetworktokensApi`

## Methods

* [Get-Network Tokens-Network Token Id](../../doc/controllers/networktokens.md#get-network-tokens-network-token-id)
* [Patch-Network Tokens-Network Token Id](../../doc/controllers/networktokens.md#patch-network-tokens-network-token-id)


# Get-Network Tokens-Network Token Id

Returns the details of a network token.

```python
def get_network_tokens_network_token_id(self,
                                       network_token_id)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `network_token_id` | `str` | Template, Required | The unique identifier of the network token. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetNetworkTokenResponse`](../../doc/models/get-network-token-response.md).

## Example Usage

```python
network_token_id = 'networkTokenId4'

result = network_tokens_api.get_network_tokens_network_token_id(network_token_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Patch-Network Tokens-Network Token Id

Updates the status of the network token.

```python
def patch_network_tokens_network_token_id(self,
                                         network_token_id,
                                         body=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `network_token_id` | `str` | Template, Required | The unique identifier of the network token. |
| `body` | [`UpdateNetworkTokenRequest`](../../doc/models/update-network-token-request.md) | Body, Optional | - |

## Response Type

**202**: No Content - look at the actual response code for the status of the request.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
network_token_id = 'networkTokenId4'

result = network_tokens_api.patch_network_tokens_network_token_id(network_token_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |

