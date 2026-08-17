# Documents

```python
documents_api = client.documents
```

## Class Name

`DocumentsApi`

## Methods

* [Post-Documents](../../doc/controllers/documents.md#post-documents)
* [Get-Documents-Id](../../doc/controllers/documents.md#get-documents-id)
* [Delete-Documents-Id](../../doc/controllers/documents.md#delete-documents-id)
* [Patch-Documents-Id](../../doc/controllers/documents.md#patch-documents-id)


# Post-Documents

Uploads a document for verification checks.

Adyen uses the information from the [legal entity](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities) to run automated verification checks. If these checks fail, you will be notified to provide additional documents.

You should only upload documents when Adyen requests additional information for the legal entity.

> You can upload a maximum of 15 pages for photo IDs.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def post_documents(self,
                  x_requested_verification_code=None,
                  body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `x_requested_verification_code` | `str` | Header, Optional | Use a suberror code as your requested verification code. You can include one code at a time in your request header. Requested verification codes can only be used in your test environment. |
| `body` | [`Document`](../../doc/models/document.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`Document`](../../doc/models/document.md)

## Example Usage

```python
body = Document(
    description='Registration doc for Example Company',
    mtype=Type84Enum.REGISTRATIONDOCUMENT,
    attachments=[
        Attachment(
            content='JVBERi0xLjQKJcOkw7zDtsOfCjIgMCBv+f/ub0j6JPRX+E3EmC=='
        )
    ],
    owner=OwnerEntity2(
        id='LE00000000000000000000001',
        mtype='legalEntity'
    )
)

result = documents_api.post_documents(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "type": "registrationDocument",
  "attachments": [
    {
      "content": "JVBERi0xLjQKJcOkw7zDtsOfCjIgMCBv+f/ub0j6JPRX+E3EmC=="
    }
  ],
  "description": "Registration doc for Example Company",
  "fileName": "Registration doc for Example Company",
  "owner": {
    "id": "LE00000000000000000000001",
    "type": "legalEntity"
  },
  "id": "SE322JV223222F5GV2N9L8GDK"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Get-Documents-Id

Returns a document.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def get_documents_id(self,
                    id,
                    skip_content=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the document. |
| `skip_content` | `bool` | Query, Optional | Do not load document content while fetching the document. |

## Response Type

**200**: OK - the request has succeeded.

[`Document`](../../doc/models/document.md)

## Example Usage

```python
id = 'id0'

result = documents_api.get_documents_id(id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "type": "registrationDocument",
  "attachments": [
    {
      "content": "JVBERi0xLjQKJcOkw7zDtsOfCjIgMCBv+f/ub0j6JPRX+E3EmC=="
    }
  ],
  "description": "Registration doc for Example Company",
  "fileName": "Registration doc for Example Company",
  "owner": {
    "id": "LE00000000000000000000001",
    "type": "legalEntity"
  },
  "id": "SE322JV223222F5GV2N9L8GDK"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Delete-Documents-Id

Deletes a document.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def delete_documents_id(self,
                       id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the document to be deleted. |

## Response Type

**204**: No Content - look at the actual response code for the status of the request.

`void`

## Example Usage

```python
id = 'id0'

documents_api.delete_documents_id(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Patch-Documents-Id

Updates a document.

> You can upload a maximum of 15 pages for photo IDs.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def patch_documents_id(self,
                      id,
                      x_requested_verification_code=None,
                      body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the document to be updated. |
| `x_requested_verification_code` | `str` | Header, Optional | Use the requested verification code 0_0001 to resolve any suberrors associated with the document. Requested verification codes can only be used in your test environment. |
| `body` | [`Document`](../../doc/models/document.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`Document`](../../doc/models/document.md)

## Example Usage

```python
id = 'id0'

body = Document(
    description='Proof of industry doc for Example Company',
    mtype=Type84Enum.PROOFOFINDUSTRY
)

result = documents_api.patch_documents_id(
    id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "type": "proofOfIndustry",
  "attachments": [
    {
      "content": "JVBERi0xLjQKJcOkw7zDtsOfCjIgMCBv+f/ub0j6JPRX+E3EmC=="
    }
  ],
  "description": "Proof of industry for Example Company",
  "fileName": "Proof of industry for Example Company",
  "owner": {
    "id": "LE00000000000000000000001",
    "type": "legalEntity"
  },
  "id": "SE322JV223222F5GV2N9L8GDK"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |

