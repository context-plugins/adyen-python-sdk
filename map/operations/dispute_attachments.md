<!-- Generated file — do not edit; regenerated with the SDK. -->

# DisputeAttachments — operations

Accessor: `client.dispute_attachments` · Source: `adyen/apis/dispute_attachments.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.dispute_attachments.delete_disputes_dispute_id_attachments_attachment_id

- **Route**: `DELETE /disputes/{disputeId}/attachments/{attachmentId}`
- **Server**: `default23`
- **Signature**: `def delete_disputes_dispute_id_attachments_attachment_id(dispute_id: str, attachment_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `dispute_id`, `attachment_id`
- **Params**: `dispute_id` — path `disputeId` · `attachment_id` — path `attachmentId`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteDisputesDisputeIdAttachmentsAttachmentIdErrorBody]`
- **Error**: `DeleteDisputesDisputeIdAttachmentsAttachmentIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteDisputesDisputeIdAttachmentsAttachmentIdErrorBody` | `adyen/errors/delete_disputes_dispute_id_attachments_attachment_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.dispute_attachments.get_disputes_dispute_id_attachments

- **Route**: `GET /disputes/{disputeId}/attachments`
- **Server**: `default23`
- **Signature**: `def get_disputes_dispute_id_attachments(dispute_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `dispute_id`
- **Params**: `dispute_id` — path `disputeId`
- **Returns (parsed)**: `list[DisputeAttachment]`
- **Returns (raw)**: `ApiResult[list[DisputeAttachment], GetDisputesDisputeIdAttachmentsErrorBody]`
- **Error**: `GetDisputesDisputeIdAttachmentsErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DisputeAttachment` | `adyen/models/dispute_attachment.py` |
| `GetDisputesDisputeIdAttachmentsErrorBody` | `adyen/errors/get_disputes_dispute_id_attachments_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.dispute_attachments.get_disputes_dispute_id_attachments_attachment_id

- **Route**: `GET /disputes/{disputeId}/attachments/{attachmentId}`
- **Server**: `default23`
- **Signature**: `def get_disputes_dispute_id_attachments_attachment_id(dispute_id: str, attachment_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `dispute_id`, `attachment_id`
- **Params**: `dispute_id` — path `disputeId` · `attachment_id` — path `attachmentId`
- **Returns (parsed)**: `DisputeAttachment`
- **Returns (raw)**: `ApiResult[DisputeAttachment, GetDisputesDisputeIdAttachmentsAttachmentIdErrorBody]`
- **Error**: `GetDisputesDisputeIdAttachmentsAttachmentIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DisputeAttachment` | `adyen/models/dispute_attachment.py` |
| `GetDisputesDisputeIdAttachmentsAttachmentIdErrorBody` | `adyen/errors/get_disputes_dispute_id_attachments_attachment_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.dispute_attachments.post_disputes_dispute_id_attachments

- **Route**: `POST /disputes/{disputeId}/attachments`
- **Server**: `default23`
- **Signature**: `def post_disputes_dispute_id_attachments(dispute_id: str, body: DisputeAttachment | DisputeAttachmentDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `dispute_id`, `body`
- **Params**: `dispute_id` — path `disputeId` · `body` — JSON body
- **Returns (parsed)**: `AttachDocumentResponse`
- **Returns (raw)**: `ApiResult[AttachDocumentResponse, PostDisputesDisputeIdAttachmentsErrorBody]`
- **Error**: `PostDisputesDisputeIdAttachmentsErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DisputeAttachment` | `adyen/models/dispute_attachment.py` |
| `DisputeAttachmentDict` | `adyen/models/dispute_attachment.py` |
| `AttachDocumentResponse` | `adyen/models/attach_document_response.py` |
| `PostDisputesDisputeIdAttachmentsErrorBody` | `adyen/errors/post_disputes_dispute_id_attachments_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

