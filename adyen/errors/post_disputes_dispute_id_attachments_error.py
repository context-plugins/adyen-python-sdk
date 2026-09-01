from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostDisputesDisputeIdAttachmentsErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostDisputesDisputeIdAttachmentsError:
    def map(self, response: HttpResponse) -> PostDisputesDisputeIdAttachmentsErrorBody:
        match response.status_code:
            case 401 | 403 | 422:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


post_disputes_dispute_id_attachments_error_mapper: Final[
    ErrorMapper[PostDisputesDisputeIdAttachmentsErrorBody]
] = _PostDisputesDisputeIdAttachmentsError()
