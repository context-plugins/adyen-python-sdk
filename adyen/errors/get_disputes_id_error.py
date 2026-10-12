from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

GetDisputesIdErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _GetDisputesIdError:
    def map(self, status_code: int, content: bytes) -> GetDisputesIdErrorBody:
        match status_code:
            case 401 | 403 | 422:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


get_disputes_id_error_mapper: Final[ErrorMapper[GetDisputesIdErrorBody]] = _GetDisputesIdError()
