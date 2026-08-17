# Payments App

```python
payments_app_api = client.payments_app
```

## Class Name

`PaymentsAppApi`

## Methods

* [Post-Merchants-Merchant Id-Generate Payments App Boarding Token](../../doc/controllers/payments-app.md#post-merchants-merchant-id-generate-payments-app-boarding-token)
* [Post-Merchants-Merchant Id-Stores-Store Id-Generate Payments App Boarding Token](../../doc/controllers/payments-app.md#post-merchants-merchant-id-stores-store-id-generate-payments-app-boarding-token)
* [Get-Merchants-Merchant Id-Payments Apps](../../doc/controllers/payments-app.md#get-merchants-merchant-id-payments-apps)
* [Get-Merchants-Merchant Id-Stores-Store Id-Payments Apps](../../doc/controllers/payments-app.md#get-merchants-merchant-id-stores-store-id-payments-apps)
* [Post-Merchants-Merchant Id-Payments Apps-Installation Id-Revoke](../../doc/controllers/payments-app.md#post-merchants-merchant-id-payments-apps-installation-id-revoke)


# Post-Merchants-Merchant Id-Generate Payments App Boarding Token

Creates a boarding token used to authenticate the installation of a Payments App instance on an Android device. The boarding token is created for the `boardingRequestToken` of the Payments App for the merchant account identified in the path.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Adyen Payments App role

:information_source: **Note** This endpoint does not require authentication.

```python
def post_merchants_merchant_id_generate_payments_app_boarding_token(self,
                                                                   merchant_id,
                                                                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account.<br><br>**Constraints**: *Minimum Length*: `1` |
| `body` | [`BoardingTokenRequest`](../../doc/models/boarding-token-request.md) | Body, Required | - |

## Response Type

**200**: OK - the request has succeeded.

[`BoardingTokenResponse`](../../doc/models/boarding-token-response.md)

## Example Usage

```python
merchant_id = 'merchantId6'

body = BoardingTokenRequest(
    boarding_request_token='boardingRequestToken6'
)

result = payments_app_api.post_merchants_merchant_id_generate_payments_app_boarding_token(
    merchant_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Post-Merchants-Merchant Id-Stores-Store Id-Generate Payments App Boarding Token

Creates a boarding token used to authenticate the installation of a Payments App instance on an Android device. The boarding token is created for the `boardingRequestToken` of the Payments App for the store identified in the path.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Adyen Payments App role

:information_source: **Note** This endpoint does not require authentication.

```python
def post_merchants_merchant_id_stores_store_id_generate_payments_app_boarding_token(self,
                                                                                   merchant_id,
                                                                                   store_id,
                                                                                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account.<br><br>**Constraints**: *Minimum Length*: `1` |
| `store_id` | `str` | Template, Required | The unique identifier of the store.<br><br>**Constraints**: *Minimum Length*: `1` |
| `body` | [`BoardingTokenRequest`](../../doc/models/boarding-token-request.md) | Body, Required | - |

## Response Type

**200**: OK - the request has succeeded.

[`BoardingTokenResponse`](../../doc/models/boarding-token-response.md)

## Example Usage

```python
merchant_id = 'merchantId6'

store_id = 'storeId6'

body = BoardingTokenRequest(
    boarding_request_token='boardingRequestToken6'
)

result = payments_app_api.post_merchants_merchant_id_stores_store_id_generate_payments_app_boarding_token(
    merchant_id,
    store_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Get-Merchants-Merchant Id-Payments Apps

Returns the list of Payments App instances for the merchant account identified in the path.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Adyen Payments App role

:information_source: **Note** This endpoint does not require authentication.

```python
def get_merchants_merchant_id_payments_apps(self,
                                           merchant_id,
                                           statuses=None,
                                           limit=10,
                                           offset=0)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account.<br><br>**Constraints**: *Minimum Length*: `1` |
| `statuses` | `str` | Query, Optional | The status of the Payments App. Comma-separated list of one or more values. If no value is provided, the list returns all statuses.<br><br>Possible values:<br><br>* **BOARDING**<br><br>* **BOARDED**<br><br>* **REVOKED** |
| `limit` | `int` | Query, Optional | The number of items to return.<br><br>**Default**: `10`<br><br>**Constraints**: `<= 100` |
| `offset` | `int` | Query, Optional | The number of items to skip.<br><br>**Default**: `0` |

## Response Type

**200**: OK - the request has succeeded.

[`PaymentsAppResponse`](../../doc/models/payments-app-response.md)

## Example Usage

```python
merchant_id = 'merchantId6'

limit = 10

offset = 0

result = payments_app_api.get_merchants_merchant_id_payments_apps(
    merchant_id,
    limit=limit,
    offset=offset
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Get-Merchants-Merchant Id-Stores-Store Id-Payments Apps

Returns the list of Payments App instances for the store identified in the path.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Adyen Payments App role

:information_source: **Note** This endpoint does not require authentication.

```python
def get_merchants_merchant_id_stores_store_id_payments_apps(self,
                                                           merchant_id,
                                                           store_id,
                                                           statuses=None,
                                                           limit=10,
                                                           offset=0)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account.<br><br>**Constraints**: *Minimum Length*: `1` |
| `store_id` | `str` | Template, Required | The unique identifier of the store.<br><br>**Constraints**: *Minimum Length*: `1` |
| `statuses` | `str` | Query, Optional | The status of the Payments App. Comma-separated list of one or more values. If no value is provided, the list returns all statuses.<br><br>Possible values:<br><br>* **BOARDING**<br><br>* **BOARDED**<br><br>* **REVOKED** |
| `limit` | `int` | Query, Optional | The number of items to return.<br><br>**Default**: `10`<br><br>**Constraints**: `<= 100` |
| `offset` | `int` | Query, Optional | The number of items to skip.<br><br>**Default**: `0` |

## Response Type

**200**: OK - the request has succeeded.

[`PaymentsAppResponse`](../../doc/models/payments-app-response.md)

## Example Usage

```python
merchant_id = 'merchantId6'

store_id = 'storeId6'

limit = 10

offset = 0

result = payments_app_api.get_merchants_merchant_id_stores_store_id_payments_apps(
    merchant_id,
    store_id,
    limit=limit,
    offset=offset
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Post-Merchants-Merchant Id-Payments Apps-Installation Id-Revoke

Revokes the authentication of the Payments App instance for the `installationId` and merchant account identified in the path. This call revokes the authentication of the Payments App instance with the `installationId` identified in the path for both merchant accounts and stores.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Adyen Payments App role

:information_source: **Note** This endpoint does not require authentication.

```python
def post_merchants_merchant_id_payments_apps_installation_id_revoke(self,
                                                                   merchant_id,
                                                                   installation_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account.<br><br>**Constraints**: *Minimum Length*: `1` |
| `installation_id` | `str` | Template, Required | The unique identifier of the Payments App instance on a device.<br><br>**Constraints**: *Minimum Length*: `1` |

## Response Type

**200**: OK - the request has succeeded.

`Any`

## Example Usage

```python
merchant_id = 'merchantId6'

installation_id = 'installationId4'

result = payments_app_api.post_merchants_merchant_id_payments_apps_installation_id_revoke(
    merchant_id,
    installation_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |

