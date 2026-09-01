from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.service_error import ServiceError

PostCancelOrRefundErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostCancelOrRefundError:
    def map(self, response: HttpResponse) -> PostCancelOrRefundErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError](response)
            case _:
                return RawError(response)


post_cancel_or_refund_error_mapper: Final[ErrorMapper[PostCancelOrRefundErrorBody]] = _PostCancelOrRefundError()
