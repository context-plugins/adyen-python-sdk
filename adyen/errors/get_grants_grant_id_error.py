from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

GetGrantsGrantIdErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _GetGrantsGrantIdError:
    def map(self, response: HttpResponse) -> GetGrantsGrantIdErrorBody:
        match response.status_code:
            case 404 | 422:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


get_grants_grant_id_error_mapper: Final[ErrorMapper[GetGrantsGrantIdErrorBody]] = _GetGrantsGrantIdError()
