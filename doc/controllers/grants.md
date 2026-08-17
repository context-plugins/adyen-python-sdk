# Grants

```python
grants_api = client.grants
```

## Class Name

`GrantsApi`

## Methods

* [Get-Grants](../../doc/controllers/grants.md#get-grants)
* [Post-Grants](../../doc/controllers/grants.md#post-grants)
* [Get-Grants-Grant Id](../../doc/controllers/grants.md#get-grants-grant-id)
* [Get-Grants-Grant Id-Disbursements](../../doc/controllers/grants.md#get-grants-grant-id-disbursements)
* [Get-Grants-Grant Id-Disbursements-Disbursement Id](../../doc/controllers/grants.md#get-grants-grant-id-disbursements-disbursement-id)
* [Patch-Grants-Grant Id-Disbursements-Disbursement Id](../../doc/controllers/grants.md#patch-grants-grant-id-disbursements-disbursement-id)


# Get-Grants

Returns a list of all the grants of a specific account holder.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_grants(self,
              counterparty_account_holder_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `counterparty_account_holder_id` | `str` | Query, Required | The unique identifier of the account holder that received the grants. |

## Response Type

**200**: OK - The request has succeeded.

[`Grants`](../../doc/models/grants.md)

## Example Usage

```python
counterparty_account_holder_id = 'counterpartyAccountHolderId8'

result = grants_api.get_grants(counterparty_account_holder_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found - The entity was not found. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Post-Grants

Make a request for a grant on behalf of an account holder.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_grants(self,
               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CapitalGrantInfo`](../../doc/models/capital-grant-info.md) | Body, Optional | - |

## Response Type

**200**: OK - The request has succeeded.

[`Grant`](../../doc/models/grant.md)

## Example Usage

```python
result = grants_api.post_grants()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Get-Grants-Grant Id

Returns the details of the specified grant.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_grants_grant_id(self,
                       grant_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grant_id` | `str` | Template, Required | The unique identifier of the grant reference. |

## Response Type

**200**: OK - The request has succeeded.

[`Grant`](../../doc/models/grant.md)

## Example Usage

```python
grant_id = 'grantId8'

result = grants_api.get_grants_grant_id(grant_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found - The entity was not found. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Get-Grants-Grant Id-Disbursements

Returns the disbursements of a specified grant.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_grants_grant_id_disbursements(self,
                                     grant_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grant_id` | `str` | Template, Required | The unique identifier of the grant reference. |

## Response Type

**200**: OK - The request has succeeded.

[`Disbursements`](../../doc/models/disbursements.md)

## Example Usage

```python
grant_id = 'grantId8'

result = grants_api.get_grants_grant_id_disbursements(grant_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found - The entity was not found. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Get-Grants-Grant Id-Disbursements-Disbursement Id

Returns the details of a disbursement specified in the path.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_grants_grant_id_disbursements_disbursement_id(self,
                                                     grant_id,
                                                     disbursement_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grant_id` | `str` | Template, Required | The unique identifier of the grant reference. |
| `disbursement_id` | `str` | Template, Required | The unique identifier of the disbursement. |

## Response Type

**200**: OK - The request has succeeded.

[`Disbursement`](../../doc/models/disbursement.md)

## Example Usage

```python
grant_id = 'grantId8'

disbursement_id = 'disbursementId8'

result = grants_api.get_grants_grant_id_disbursements_disbursement_id(
    grant_id,
    disbursement_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found - The entity was not found. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Patch-Grants-Grant Id-Disbursements-Disbursement Id

Update the percentage of your user's net income that is deducted for repaying the grant.

:information_source: **Note** This endpoint does not require authentication.

```python
def patch_grants_grant_id_disbursements_disbursement_id(self,
                                                       grant_id,
                                                       disbursement_id,
                                                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grant_id` | `str` | Template, Required | The unique identifier of the grant reference.<br><br>**Constraints**: *Minimum Length*: `1` |
| `disbursement_id` | `str` | Template, Required | The unique identifier of the disbursement.<br><br>**Constraints**: *Minimum Length*: `1` |
| `body` | [`DisbursementInfoUpdate`](../../doc/models/disbursement-info-update.md) | Body, Required | - |

## Response Type

**200**: OK - The request has succeeded.

[`Disbursement`](../../doc/models/disbursement.md)

## Example Usage

```python
grant_id = 'grantId8'

disbursement_id = 'disbursementId8'

body = DisbursementInfoUpdate()

result = grants_api.patch_grants_grant_id_disbursements_disbursement_id(
    grant_id,
    disbursement_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found - The entity was not found. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |

