from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.service_error import ServiceError

PostRetrieve3Ds2ResultErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostRetrieve3Ds2ResultError:
    def map(self, status_code: int, content: bytes) -> PostRetrieve3Ds2ResultErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError](content)
            case _:
                return RawError(status_code, content)


post_retrieve3_ds2_result_error_mapper: Final[
    ErrorMapper[PostRetrieve3Ds2ResultErrorBody]
] = _PostRetrieve3Ds2ResultError()
