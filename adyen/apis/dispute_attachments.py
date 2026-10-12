from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RequestOptionsOrDict,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.delete_disputes_dispute_id_attachments_attachment_id_error import (
    DeleteDisputesDisputeIdAttachmentsAttachmentIdErrorBody,
    delete_disputes_dispute_id_attachments_attachment_id_error_mapper,
)
from ..errors.get_disputes_dispute_id_attachments_attachment_id_error import (
    GetDisputesDisputeIdAttachmentsAttachmentIdErrorBody,
    get_disputes_dispute_id_attachments_attachment_id_error_mapper,
)
from ..errors.get_disputes_dispute_id_attachments_error import (
    GetDisputesDisputeIdAttachmentsErrorBody,
    get_disputes_dispute_id_attachments_error_mapper,
)
from ..errors.post_disputes_dispute_id_attachments_error import (
    PostDisputesDisputeIdAttachmentsErrorBody,
    post_disputes_dispute_id_attachments_error_mapper,
)
from ..models.attach_document_response import AttachDocumentResponse
from ..models.dispute_attachment import DisputeAttachment, DisputeAttachmentDict
from ..server.server import Server


class DisputeAttachments:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = DisputeAttachmentsWithRawResponse(client, server)

    def delete_disputes_dispute_id_attachments_attachment_id(
        self, dispute_id: str, attachment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Removes the attachment from the raised dispute. Adyen may keep this file for compliance purposes.

        Args:
            dispute_id: The unique identifier of the raised dispute.
            attachment_id: The unique identifier of the attachment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The attachment was successfully removed

        Raises:
            ApiError: Authentication required. Insufficient permissions to process the request. A request validation
                error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.delete_disputes_dispute_id_attachments_attachment_id(
                dispute_id, attachment_id, request_options=request_options
            ),
        )

    def get_disputes_dispute_id_attachments(
        self, dispute_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DisputeAttachment]:
        """Get a list of attachments associated with a dispute ID.

        Args:
            dispute_id: The unique identifier of the raised dispute.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Authentication required. Insufficient permissions to process the request. A request validation
                error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.get_disputes_dispute_id_attachments(dispute_id, request_options=request_options)
        )

    def get_disputes_dispute_id_attachments_attachment_id(
        self, dispute_id: str, attachment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DisputeAttachment:
        """Search for a single attachment, providing the specific dispute ID and attachment ID.

        Args:
            dispute_id: The unique identifier of the raised dispute.
            attachment_id: The unique identifier of the attachment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Authentication required. Insufficient permissions to process the request. A request validation
                error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.get_disputes_dispute_id_attachments_attachment_id(
                dispute_id, attachment_id, request_options=request_options
            ),
        )

    def post_disputes_dispute_id_attachments(
        self,
        dispute_id: str,
        body: DisputeAttachment | DisputeAttachmentDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AttachDocumentResponse:
        """Add supporting information as an attachment for the raised dispute. Upload receipts, communication, or any
        other documentation to support the dispute.

        Args:
            dispute_id: The unique identifier of the raised dispute.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Authentication required. Insufficient permissions to process the request. A request validation
                error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.post_disputes_dispute_id_attachments(
                dispute_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> DisputeAttachmentsWithRawResponse:
        return self._with_raw_response


class AsyncDisputeAttachments:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncDisputeAttachmentsWithRawResponse(client, server)

    async def delete_disputes_dispute_id_attachments_attachment_id(
        self, dispute_id: str, attachment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Removes the attachment from the raised dispute. Adyen may keep this file for compliance purposes.

        Args:
            dispute_id: The unique identifier of the raised dispute.
            attachment_id: The unique identifier of the attachment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The attachment was successfully removed

        Raises:
            ApiError: Authentication required. Insufficient permissions to process the request. A request validation
                error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_disputes_dispute_id_attachments_attachment_id(
                dispute_id, attachment_id, request_options=request_options
            ),
        )

    async def get_disputes_dispute_id_attachments(
        self, dispute_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DisputeAttachment]:
        """Get a list of attachments associated with a dispute ID.

        Args:
            dispute_id: The unique identifier of the raised dispute.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Authentication required. Insufficient permissions to process the request. A request validation
                error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.get_disputes_dispute_id_attachments(
                dispute_id, request_options=request_options
            ),
        )

    async def get_disputes_dispute_id_attachments_attachment_id(
        self, dispute_id: str, attachment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DisputeAttachment:
        """Search for a single attachment, providing the specific dispute ID and attachment ID.

        Args:
            dispute_id: The unique identifier of the raised dispute.
            attachment_id: The unique identifier of the attachment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Authentication required. Insufficient permissions to process the request. A request validation
                error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.get_disputes_dispute_id_attachments_attachment_id(
                dispute_id, attachment_id, request_options=request_options
            ),
        )

    async def post_disputes_dispute_id_attachments(
        self,
        dispute_id: str,
        body: DisputeAttachment | DisputeAttachmentDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AttachDocumentResponse:
        """Add supporting information as an attachment for the raised dispute. Upload receipts, communication, or any
        other documentation to support the dispute.

        Args:
            dispute_id: The unique identifier of the raised dispute.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Authentication required. Insufficient permissions to process the request. A request validation
                error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.post_disputes_dispute_id_attachments(
                dispute_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncDisputeAttachmentsWithRawResponse:
        return self._with_raw_response


class DisputeAttachmentsWithRawResponse(BaseRawResponse[RawClient, Server]):
    def delete_disputes_dispute_id_attachments_attachment_id(
        self, dispute_id: str, attachment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteDisputesDisputeIdAttachmentsAttachmentIdErrorBody]:
        """Removes the attachment from the raised dispute. Adyen may keep this file for compliance purposes.

        Args:
            dispute_id: The unique identifier of the raised dispute.
            attachment_id: The unique identifier of the attachment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default23("/disputes/{disputeId}/attachments/{attachmentId}"),
            path_params=[param[str]("disputeId", dispute_id), param[str]("attachmentId", attachment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=empty_response,
            error_mapper=delete_disputes_dispute_id_attachments_attachment_id_error_mapper,
            request_options=request_options,
        )

    def get_disputes_dispute_id_attachments(
        self, dispute_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DisputeAttachment], GetDisputesDisputeIdAttachmentsErrorBody]:
        """Get a list of attachments associated with a dispute ID.

        Args:
            dispute_id: The unique identifier of the raised dispute.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default23("/disputes/{disputeId}/attachments"),
            path_params=[param[str]("disputeId", dispute_id)],
            decoder=json_decoder[list[DisputeAttachment]],
            error_mapper=get_disputes_dispute_id_attachments_error_mapper,
            request_options=request_options,
        )

    def get_disputes_dispute_id_attachments_attachment_id(
        self, dispute_id: str, attachment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DisputeAttachment, GetDisputesDisputeIdAttachmentsAttachmentIdErrorBody]:
        """Search for a single attachment, providing the specific dispute ID and attachment ID.

        Args:
            dispute_id: The unique identifier of the raised dispute.
            attachment_id: The unique identifier of the attachment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default23("/disputes/{disputeId}/attachments/{attachmentId}"),
            path_params=[param[str]("disputeId", dispute_id), param[str]("attachmentId", attachment_id)],
            decoder=json_decoder[DisputeAttachment],
            error_mapper=get_disputes_dispute_id_attachments_attachment_id_error_mapper,
            request_options=request_options,
        )

    def post_disputes_dispute_id_attachments(
        self,
        dispute_id: str,
        body: DisputeAttachment | DisputeAttachmentDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AttachDocumentResponse, PostDisputesDisputeIdAttachmentsErrorBody]:
        """Add supporting information as an attachment for the raised dispute. Upload receipts, communication, or any
        other documentation to support the dispute.

        Args:
            dispute_id: The unique identifier of the raised dispute.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default23("/disputes/{disputeId}/attachments"),
            path_params=[param[str]("disputeId", dispute_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DisputeAttachment | DisputeAttachmentDict](body),
            decoder=json_decoder[AttachDocumentResponse],
            error_mapper=post_disputes_dispute_id_attachments_error_mapper,
            request_options=request_options,
        )


class AsyncDisputeAttachmentsWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def delete_disputes_dispute_id_attachments_attachment_id(
        self, dispute_id: str, attachment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteDisputesDisputeIdAttachmentsAttachmentIdErrorBody]:
        """Removes the attachment from the raised dispute. Adyen may keep this file for compliance purposes.

        Args:
            dispute_id: The unique identifier of the raised dispute.
            attachment_id: The unique identifier of the attachment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default23("/disputes/{disputeId}/attachments/{attachmentId}"),
            path_params=[param[str]("disputeId", dispute_id), param[str]("attachmentId", attachment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=async_empty_response,
            error_mapper=delete_disputes_dispute_id_attachments_attachment_id_error_mapper,
            request_options=request_options,
        )

    async def get_disputes_dispute_id_attachments(
        self, dispute_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DisputeAttachment], GetDisputesDisputeIdAttachmentsErrorBody]:
        """Get a list of attachments associated with a dispute ID.

        Args:
            dispute_id: The unique identifier of the raised dispute.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default23("/disputes/{disputeId}/attachments"),
            path_params=[param[str]("disputeId", dispute_id)],
            decoder=async_json_decoder[list[DisputeAttachment]],
            error_mapper=get_disputes_dispute_id_attachments_error_mapper,
            request_options=request_options,
        )

    async def get_disputes_dispute_id_attachments_attachment_id(
        self, dispute_id: str, attachment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DisputeAttachment, GetDisputesDisputeIdAttachmentsAttachmentIdErrorBody]:
        """Search for a single attachment, providing the specific dispute ID and attachment ID.

        Args:
            dispute_id: The unique identifier of the raised dispute.
            attachment_id: The unique identifier of the attachment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default23("/disputes/{disputeId}/attachments/{attachmentId}"),
            path_params=[param[str]("disputeId", dispute_id), param[str]("attachmentId", attachment_id)],
            decoder=async_json_decoder[DisputeAttachment],
            error_mapper=get_disputes_dispute_id_attachments_attachment_id_error_mapper,
            request_options=request_options,
        )

    async def post_disputes_dispute_id_attachments(
        self,
        dispute_id: str,
        body: DisputeAttachment | DisputeAttachmentDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AttachDocumentResponse, PostDisputesDisputeIdAttachmentsErrorBody]:
        """Add supporting information as an attachment for the raised dispute. Upload receipts, communication, or any
        other documentation to support the dispute.

        Args:
            dispute_id: The unique identifier of the raised dispute.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default23("/disputes/{disputeId}/attachments"),
            path_params=[param[str]("disputeId", dispute_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DisputeAttachment | DisputeAttachmentDict](body),
            decoder=async_json_decoder[AttachDocumentResponse],
            error_mapper=post_disputes_dispute_id_attachments_error_mapper,
            request_options=request_options,
        )
