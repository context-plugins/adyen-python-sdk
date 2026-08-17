# Users-Companylevel

```python
users_companylevel_api = client.users_companylevel
```

## Class Name

`UsersCompanylevelApi`

## Methods

* [Get-Companies-Company Id-Users](../../doc/controllers/users-companylevel.md#get-companies-company-id-users)
* [Post-Companies-Company Id-Users](../../doc/controllers/users-companylevel.md#post-companies-company-id-users)
* [Get-Companies-Company Id-Users-User Id](../../doc/controllers/users-companylevel.md#get-companies-company-id-users-user-id)
* [Patch-Companies-Company Id-Users-User Id](../../doc/controllers/users-companylevel.md#patch-companies-company-id-users-user-id)


# Get-Companies-Company Id-Users

Returns the list of users for the `companyId` identified in the path.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Users read and write

```python
def get_companies_company_id_users(self,
                                  company_id,
                                  page_number=None,
                                  page_size=None,
                                  username=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_id` | `str` | Template, Required | The unique identifier of the company account. |
| `page_number` | `int` | Query, Optional | The number of the page to return. |
| `page_size` | `int` | Query, Optional | The number of items to have on a page. Maximum value is **100**. The default is **10** items on a page. |
| `username` | `str` | Query, Optional | The partial or complete username to select all users that match. |

## Response Type

**200**: OK - the request has succeeded.

[`ListCompanyUsersResponse`](../../doc/models/list-company-users-response.md)

## Example Usage

```python
company_id = 'companyId0'

result = users_company_level_api.get_companies_company_id_users(company_id)
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


# Post-Companies-Company Id-Users

Creates the user for the `companyId` identified in the path.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Users read and write

```python
def post_companies_company_id_users(self,
                                   company_id,
                                   body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_id` | `str` | Template, Required | The unique identifier of the company account. |
| `body` | [`CreateCompanyUserRequest`](../../doc/models/create-company-user-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`CreateCompanyUserResponse`](../../doc/models/create-company-user-response.md)

## Example Usage

```python
company_id = 'companyId0'

body = CreateCompanyUserRequest(
    email='john.smith@example.com',
    name=Name(
        first_name='John',
        last_name='Smith'
    ),
    username='johnsmith',
    associated_merchant_accounts=[
        'YOUR_MERCHANT_ACCOUNT'
    ],
    login_method='Email',
    roles=[
        'Merchant standard role',
        'Merchant admin'
    ],
    time_zone_code='Europe/Amsterdam'
)

result = users_company_level_api.post_companies_company_id_users(
    company_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "S2-5C334C6770",
  "name": {
    "firstName": "John",
    "lastName": "Smith"
  },
  "email": "john.smith@example.com",
  "timeZoneCode": "Europe/Amsterdam",
  "username": "johnsmith",
  "roles": [
    "Merchant standard role",
    "Merchant admin"
  ],
  "active": true,
  "_links": {
    "self": {
      "href": "https://management-test.adyen.com/v1/companies/YOUR_COMPANY_ACCOUNT/users/S2-5C334C6770"
    }
  },
  "associatedMerchantAccounts": [
    "YOUR_MERCHANT_ACCOUNT"
  ]
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


# Get-Companies-Company Id-Users-User Id

Returns user details for the `userId` and the `companyId` identified in the path.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Users read and write

```python
def get_companies_company_id_users_user_id(self,
                                          company_id,
                                          user_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_id` | `str` | Template, Required | The unique identifier of the company account. |
| `user_id` | `str` | Template, Required | The unique identifier of the user. |

## Response Type

**200**: OK - the request has succeeded.

[`CompanyUser`](../../doc/models/company-user.md)

## Example Usage

```python
company_id = 'companyId0'

user_id = 'userId0'

result = users_company_level_api.get_companies_company_id_users_user_id(
    company_id,
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


# Patch-Companies-Company Id-Users-User Id

Updates user details for the `userId` and the `companyId` identified in the path.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Users read and write

```python
def patch_companies_company_id_users_user_id(self,
                                            company_id,
                                            user_id,
                                            body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_id` | `str` | Template, Required | The unique identifier of the company account. |
| `user_id` | `str` | Template, Required | The unique identifier of the user. |
| `body` | [`UpdateCompanyUserRequest`](../../doc/models/update-company-user-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`CompanyUser`](../../doc/models/company-user.md)

## Example Usage

```python
company_id = 'companyId0'

user_id = 'userId0'

result = users_company_level_api.patch_companies_company_id_users_user_id(
    company_id,
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

