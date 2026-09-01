from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

DeleteDisputesDisputeIdAttachmentsAttachmentIdErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _DeleteDisputesDisputeIdAttachmentsAttachmentIdError:
    def map(self, response: HttpResponse) -> DeleteDisputesDisputeIdAttachmentsAttachmentIdErrorBody:
        match response.status_code:
            case 401 | 403 | 422:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


delete_disputes_dispute_id_attachments_attachment_id_error_mapper: Final[
    ErrorMapper[DeleteDisputesDisputeIdAttachmentsAttachmentIdErrorBody]
] = _DeleteDisputesDisputeIdAttachmentsAttachmentIdError()
