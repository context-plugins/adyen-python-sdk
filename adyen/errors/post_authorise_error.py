from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.service_error import ServiceError

PostAuthoriseErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostAuthoriseError:
    def map(self, status_code: int, content: bytes) -> PostAuthoriseErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError](content)
            case _:
                return RawError(status_code, content)


post_authorise_error_mapper: Final[ErrorMapper[PostAuthoriseErrorBody]] = _PostAuthoriseError()
