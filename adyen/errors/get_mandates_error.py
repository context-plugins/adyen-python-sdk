from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

GetMandatesErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _GetMandatesError:
    def map(self, response: HttpResponse) -> GetMandatesErrorBody:
        match response.status_code:
            case 401 | 403 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


get_mandates_error_mapper: Final[ErrorMapper[GetMandatesErrorBody]] = _GetMandatesError()
