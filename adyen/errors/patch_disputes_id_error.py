from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PatchDisputesIdErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PatchDisputesIdError:
    def map(self, status_code: int, content: bytes) -> PatchDisputesIdErrorBody:
        match status_code:
            case 401 | 403 | 422:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


patch_disputes_id_error_mapper: Final[ErrorMapper[PatchDisputesIdErrorBody]] = _PatchDisputesIdError()
