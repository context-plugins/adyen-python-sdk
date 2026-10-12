from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostMandatesMandateIdCancelErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostMandatesMandateIdCancelError:
    def map(self, status_code: int, content: bytes) -> PostMandatesMandateIdCancelErrorBody:
        match status_code:
            case 401 | 403 | 404 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


post_mandates_mandate_id_cancel_error_mapper: Final[
    ErrorMapper[PostMandatesMandateIdCancelErrorBody]
] = _PostMandatesMandateIdCancelError()
