from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

GetDynamicOffersErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _GetDynamicOffersError:
    def map(self, response: HttpResponse) -> GetDynamicOffersErrorBody:
        match response.status_code:
            case 422:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


get_dynamic_offers_error_mapper: Final[ErrorMapper[GetDynamicOffersErrorBody]] = _GetDynamicOffersError()
