from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.service_error1 import ServiceError1

PostDeleteShareholdersErrorBody: TypeAlias = ServiceError1 | RawError


@dataclass(frozen=True, slots=True)
class _PostDeleteShareholdersError:
    def map(self, status_code: int, content: bytes) -> PostDeleteShareholdersErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError1](content)
            case _:
                return RawError(status_code, content)


post_delete_shareholders_error_mapper: Final[
    ErrorMapper[PostDeleteShareholdersErrorBody]
] = _PostDeleteShareholdersError()
