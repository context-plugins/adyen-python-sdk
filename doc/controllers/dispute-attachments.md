# Dispute Attachments

```python
dispute_attachments_api = client.dispute_attachments
```

## Class Name

`DisputeAttachmentsApi`

## Methods

* [Get-Disputes-Dispute Id-Attachments](../../doc/controllers/dispute-attachments.md#get-disputes-dispute-id-attachments)
* [Post-Disputes-Dispute Id-Attachments](../../doc/controllers/dispute-attachments.md#post-disputes-dispute-id-attachments)
* [Delete-Disputes-Dispute Id-Attachments-Attachment Id](../../doc/controllers/dispute-attachments.md#delete-disputes-dispute-id-attachments-attachment-id)
* [Get-Disputes-Dispute Id-Attachments-Attachment Id](../../doc/controllers/dispute-attachments.md#get-disputes-dispute-id-attachments-attachment-id)


# Get-Disputes-Dispute Id-Attachments

Get a list of attachments associated with a dispute ID.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_disputes_dispute_id_attachments(self,
                                       dispute_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `str` | Template, Required | The unique identifier of the raised dispute. |

## Response Type

**200**: OK - the request has succeeded.

[`List[DisputeAttachment]`](../../doc/models/dispute-attachment.md)

## Example Usage

```python
dispute_id = 'disputeId4'

result = dispute_attachments_api.get_disputes_dispute_id_attachments(dispute_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Post-Disputes-Dispute Id-Attachments

Add supporting information as an attachment for the raised dispute. Upload receipts, communication, or any other documentation to support the dispute.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_disputes_dispute_id_attachments(self,
                                        dispute_id,
                                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `str` | Template, Required | The unique identifier of the raised dispute. |
| `body` | [`DisputeAttachment`](../../doc/models/dispute-attachment.md) | Body, Required | - |

## Response Type

**200**: OK - the request has succeeded.

[`AttachDocumentResponse`](../../doc/models/attach-document-response.md)

## Example Usage

```python
dispute_id = 'disputeId4'

body = DisputeAttachment(
    attachment_type=AttachmentType1Enum.CORRESPONDENCE,
    content='content0',
    file_name='fileName0'
)

result = dispute_attachments_api.post_disputes_dispute_id_attachments(
    dispute_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Delete-Disputes-Dispute Id-Attachments-Attachment Id

Removes the attachment from the raised dispute. Adyen may keep this file for compliance purposes.

:information_source: **Note** This endpoint does not require authentication.

```python
def delete_disputes_dispute_id_attachments_attachment_id(self,
                                                        dispute_id,
                                                        attachment_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `str` | Template, Required | The unique identifier of the raised dispute. |
| `attachment_id` | `str` | Template, Required | The unique identifier of the attachment. |

## Response Type

**204**: The attachment was successfully removed

`void`

## Example Usage

```python
dispute_id = 'disputeId4'

attachment_id = 'attachmentId8'

dispute_attachments_api.delete_disputes_dispute_id_attachments_attachment_id(
    dispute_id,
    attachment_id
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Get-Disputes-Dispute Id-Attachments-Attachment Id

Search for a single attachment, providing the specific dispute ID and attachment ID.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_disputes_dispute_id_attachments_attachment_id(self,
                                                     dispute_id,
                                                     attachment_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `str` | Template, Required | The unique identifier of the raised dispute. |
| `attachment_id` | `str` | Template, Required | The unique identifier of the attachment. |

## Response Type

**200**: OK - the request has succeeded.

[`DisputeAttachment`](../../doc/models/dispute-attachment.md)

## Example Usage

```python
dispute_id = 'disputeId4'

attachment_id = 'attachmentId8'

result = dispute_attachments_api.get_disputes_dispute_id_attachments_attachment_id(
    dispute_id,
    attachment_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |

