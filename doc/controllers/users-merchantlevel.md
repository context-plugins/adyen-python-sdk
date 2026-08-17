# Users-Merchantlevel

```python
users_merchantlevel_api = client.users_merchantlevel
```

## Class Name

`UsersMerchantlevelApi`

## Methods

* [Get-Merchants-Merchant Id-Users](../../doc/controllers/users-merchantlevel.md#get-merchants-merchant-id-users)
* [Post-Merchants-Merchant Id-Users](../../doc/controllers/users-merchantlevel.md#post-merchants-merchant-id-users)
* [Get-Merchants-Merchant Id-Users-User Id](../../doc/controllers/users-merchantlevel.md#get-merchants-merchant-id-users-user-id)
* [Patch-Merchants-Merchant Id-Users-User Id](../../doc/controllers/users-merchantlevel.md#patch-merchants-merchant-id-users-user-id)


# Get-Merchants-Merchant Id-Users

Returns a list of users associated with the `merchantId` specified in the path.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Users read and write

```python
def get_merchants_merchant_id_users(self,
                                   merchant_id,
                                   page_number=None,
                                   page_size=None,
                                   username=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | Unique identifier of the merchant. |
| `page_number` | `int` | Query, Optional | The number of the page to fetch. |
| `page_size` | `int` | Query, Optional | The number of items to have on a page. Maximum value is **100**. The default is **10** items on a page. |
| `username` | `str` | Query, Optional | The partial or complete username to select all users that match. |

## Response Type

**200**: OK - the request has succeeded.

[`ListMerchantUsersResponse`](../../doc/models/list-merchant-users-response.md)

## Example Usage

```python
merchant_id = 'merchantId6'

result = users_merchant_level_api.get_merchants_merchant_id_users(merchant_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Post-Merchants-Merchant Id-Users

Creates a user for the `merchantId` specified in the path.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Users read and write

```python
def post_merchants_merchant_id_users(self,
                                    merchant_id,
                                    body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | Unique identifier of the merchant. |
| `body` | [`CreateMerchantUserRequest`](../../doc/models/create-merchant-user-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`CreateUserResponse`](../../doc/models/create-user-response.md)

## Example Usage

```python
merchant_id = 'merchantId6'

body = CreateMerchantUserRequest(
    email='john.smith@example.com',
    name=Name(
        first_name='John',
        last_name='Smith'
    ),
    username='johnsmith',
    login_method='Email',
    roles=[
        'Merchant standard role'
    ],
    time_zone_code='Europe/Amsterdam'
)

result = users_merchant_level_api.post_merchants_merchant_id_users(
    merchant_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "S2-3B3C3C3B22",
  "name": {
    "firstName": "John",
    "lastName": "Smith"
  },
  "email": "john.smith@example.com",
  "timeZoneCode": "Europe/Amsterdam",
  "username": "johnsmith",
  "roles": [
    "Merchant standard role"
  ],
  "active": true,
  "_links": {
    "self": {
      "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/users/S2-3B3C3C3B22"
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Get-Merchants-Merchant Id-Users-User Id

Returns user details for the `userId` and the `merchantId` specified in the path.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Users read and write

```python
def get_merchants_merchant_id_users_user_id(self,
                                           merchant_id,
                                           user_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | Unique identifier of the merchant. |
| `user_id` | `str` | Template, Required | Unique identifier of the user. |

## Response Type

**200**: OK - the request has succeeded.

[`User`](../../doc/models/user.md)

## Example Usage

```python
merchant_id = 'merchantId6'

user_id = 'userId0'

result = users_merchant_level_api.get_merchants_merchant_id_users_user_id(
    merchant_id,
    user_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Patch-Merchants-Merchant Id-Users-User Id

Updates user details for the `userId` and the `merchantId` specified in the path.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Users read and write

```python
def patch_merchants_merchant_id_users_user_id(self,
                                             merchant_id,
                                             user_id,
                                             body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | Unique identifier of the merchant. |
| `user_id` | `str` | Template, Required | Unique identifier of the user. |
| `body` | [`UpdateMerchantUserRequest`](../../doc/models/update-merchant-user-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`User`](../../doc/models/user.md)

## Example Usage

```python
merchant_id = 'merchantId6'

user_id = 'userId0'

result = users_merchant_level_api.patch_merchants_merchant_id_users_user_id(
    merchant_id,
    user_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |

