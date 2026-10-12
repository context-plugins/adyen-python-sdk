from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.service_error import ServiceError

PostGet3DsAvailabilityErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostGet3DsAvailabilityError:
    def map(self, status_code: int, content: bytes) -> PostGet3DsAvailabilityErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError](content)
            case _:
                return RawError(status_code, content)


post_get3_ds_availability_error_mapper: Final[
    ErrorMapper[PostGet3DsAvailabilityErrorBody]
] = _PostGet3DsAvailabilityError()
