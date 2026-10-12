from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.service_error1 import ServiceError1

DeleteBusinessLinesIdErrorBody: TypeAlias = ServiceError1 | RawError


@dataclass(frozen=True, slots=True)
class _DeleteBusinessLinesIdError:
    def map(self, status_code: int, content: bytes) -> DeleteBusinessLinesIdErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError1](content)
            case _:
                return RawError(status_code, content)


delete_business_lines_id_error_mapper: Final[
    ErrorMapper[DeleteBusinessLinesIdErrorBody]
] = _DeleteBusinessLinesIdError()
