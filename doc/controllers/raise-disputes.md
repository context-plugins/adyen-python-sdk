# Raise Disputes

```python
raise_disputes_api = client.raise_disputes
```

## Class Name

`RaiseDisputesApi`

## Methods

* [Get-Disputes](../../doc/controllers/raise-disputes.md#get-disputes)
* [Post-Disputes](../../doc/controllers/raise-disputes.md#post-disputes)
* [Get-Disputes-Id](../../doc/controllers/raise-disputes.md#get-disputes-id)
* [Patch-Disputes-Id](../../doc/controllers/raise-disputes.md#patch-disputes-id)


# Get-Disputes

Returns a list of raised disputes that match the query parameters.

This endpoint supports cursor-based pagination. The response returns the first page of results, and returns links to the next page when applicable. You can use the links to page through the results. The response also returns links to the previous page when applicable.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_disputes(self,
                status=None,
                payment_instrument=None,
                created_since=None,
                created_until=None,
                offset=None,
                limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Query, Optional | The current status of the dispute.<br><br>Possible values: **draft**, **submitted**, **closed**, **won**, **chargeback**, **secondPresentment**. |
| `payment_instrument` | `str` | Query, Optional | The unique identifier of the payment instrument. |
| `created_since` | `str` | Query, Optional | Only include disputes that have been created on or after this point in time. The value must be in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601\)  format. For example, 2021-05-30T15:07:40Z. |
| `created_until` | `str` | Query, Optional | Only include disputes that have been created on or before this point in time. The value must be in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601\) format. For example, **2021-05-30T15:07:40Z**. |
| `offset` | `str` | Query, Optional | The number of items that you want to skip. |
| `limit` | `str` | Query, Optional | The number of items returned per page, maximum of 500 items. By default, the response returns 100 items per page. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[DisputeResponse]`](../../doc/models/dispute-response.md).

## Example Usage

```python
result = raise_disputes_api.get_disputes()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Authentication required. | [`Disputes401ErrorException`](../../doc/models/disputes-401-error-exception.md) |
| 403 | Insufficient permissions to process the request. | [`Disputes403ErrorException`](../../doc/models/disputes-403-error-exception.md) |
| 422 | A request validation error. | [`Disputes422ErrorException`](../../doc/models/disputes-422-error-exception.md) |


# Post-Disputes

Raise a dispute for an underlying transaction, providing a dispute type and the amount you want to dispute.

Raising a dispute returns a dispute ID, which you can use to update details about the dispute, provide supporting documentation, close the dispute, or submit the dispute for a chargeback. You can also use the dispute ID to view the status of the dispute.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_disputes(self,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DisputeRequest`](../../doc/models/dispute-request.md) | Body, Required | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DisputeResponse`](../../doc/models/dispute-response.md).

## Example Usage

```python
body = DisputeRequest(
    transaction_id='transactionId6',
    mtype='type4'
)

result = raise_disputes_api.post_disputes(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Authentication required. | [`Disputes401ErrorException`](../../doc/models/disputes-401-error-exception.md) |
| 403 | Insufficient permissions to process the request. | [`Disputes403ErrorException`](../../doc/models/disputes-403-error-exception.md) |
| 422 | A request validation error. | [`Disputes422ErrorException`](../../doc/models/disputes-422-error-exception.md) |


# Get-Disputes-Id

Get a raised dispute by ID.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_disputes_id(self,
                   id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the raised dispute. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DisputeResponse`](../../doc/models/dispute-response.md).

## Example Usage

```python
id = 'id0'

result = raise_disputes_api.get_disputes_id(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Authentication required. | [`Disputes401ErrorException`](../../doc/models/disputes-401-error-exception.md) |
| 403 | Insufficient permissions to process the request. | [`Disputes403ErrorException`](../../doc/models/disputes-403-error-exception.md) |
| 422 | A request validation error. | [`Disputes422ErrorException`](../../doc/models/disputes-422-error-exception.md) |


# Patch-Disputes-Id

Update information related to a raised dispute, or change a dispute's status from **draft** to **submitted** or **closed**.

**Note:** Changing the status of a dispute to **submitted** or **closed** is a final action. You cannot make updates to a **submitted** or **closed** dispute. Make sure to upload all supporting attachments using the `POST /disputes/{id}/attachments` endpoint before you submit a dispute. When you update a dispute to **submitted**, Adyen sends the raised dispute to the card scheme for review and acquirer defense. When you update a raised dispute to **closed**, Adyen closes the dispute, and the dispute is no longer eligible for review by the card scheme.

:information_source: **Note** This endpoint does not require authentication.

```python
def patch_disputes_id(self,
                     id,
                     body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the raised dispute. |
| `body` | [`PatchableDisputeRequest`](../../doc/models/patchable-dispute-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DisputeResponse`](../../doc/models/dispute-response.md).

## Example Usage

```python
id = 'id0'

result = raise_disputes_api.patch_disputes_id(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Authentication required. | [`Disputes401ErrorException`](../../doc/models/disputes-401-error-exception.md) |
| 403 | Insufficient permissions to process the request. | [`Disputes403ErrorException`](../../doc/models/disputes-403-error-exception.md) |
| 422 | A request validation error. | [`Disputes422ErrorException`](../../doc/models/disputes-422-error-exception.md) |

