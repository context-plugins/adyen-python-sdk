from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.service_error import ServiceError

PostAuthorise3Ds2ErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostAuthorise3Ds2Error:
    def map(self, status_code: int, content: bytes) -> PostAuthorise3Ds2ErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError](content)
            case _:
                return RawError(status_code, content)


post_authorise3_ds2_error_mapper: Final[ErrorMapper[PostAuthorise3Ds2ErrorBody]] = _PostAuthorise3Ds2Error()
