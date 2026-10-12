from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

GetGrantsGrantIdDisbursementsErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _GetGrantsGrantIdDisbursementsError:
    def map(self, status_code: int, content: bytes) -> GetGrantsGrantIdDisbursementsErrorBody:
        match status_code:
            case 404 | 422:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


get_grants_grant_id_disbursements_error_mapper: Final[
    ErrorMapper[GetGrantsGrantIdDisbursementsErrorBody]
] = _GetGrantsGrantIdDisbursementsError()
