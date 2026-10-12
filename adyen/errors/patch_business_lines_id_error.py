from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.service_error1 import ServiceError1

PatchBusinessLinesIdErrorBody: TypeAlias = ServiceError1 | RawError


@dataclass(frozen=True, slots=True)
class _PatchBusinessLinesIdError:
    def map(self, status_code: int, content: bytes) -> PatchBusinessLinesIdErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError1](content)
            case _:
                return RawError(status_code, content)


patch_business_lines_id_error_mapper: Final[ErrorMapper[PatchBusinessLinesIdErrorBody]] = _PatchBusinessLinesIdError()
