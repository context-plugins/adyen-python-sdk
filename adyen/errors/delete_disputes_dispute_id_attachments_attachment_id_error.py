from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

DeleteDisputesDisputeIdAttachmentsAttachmentIdErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _DeleteDisputesDisputeIdAttachmentsAttachmentIdError:
    def map(self, status_code: int, content: bytes) -> DeleteDisputesDisputeIdAttachmentsAttachmentIdErrorBody:
        match status_code:
            case 401 | 403 | 422:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


delete_disputes_dispute_id_attachments_attachment_id_error_mapper: Final[
    ErrorMapper[DeleteDisputesDisputeIdAttachmentsAttachmentIdErrorBody]
] = _DeleteDisputesDisputeIdAttachmentsAttachmentIdError()
