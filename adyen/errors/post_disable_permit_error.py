from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.service_error import ServiceError

PostDisablePermitErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostDisablePermitError:
    def map(self, status_code: int, content: bytes) -> PostDisablePermitErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError](content)
            case _:
                return RawError(status_code, content)


post_disable_permit_error_mapper: Final[ErrorMapper[PostDisablePermitErrorBody]] = _PostDisablePermitError()
