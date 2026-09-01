from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.service_error import ServiceError

PostRetrieve3Ds2ResultErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostRetrieve3Ds2ResultError:
    def map(self, response: HttpResponse) -> PostRetrieve3Ds2ResultErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError](response)
            case _:
                return RawError(response)


post_retrieve3_ds2_result_error_mapper: Final[
    ErrorMapper[PostRetrieve3Ds2ResultErrorBody]
] = _PostRetrieve3Ds2ResultError()
