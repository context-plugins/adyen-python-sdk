from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

GetGrantOffers1ErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _GetGrantOffers1Error:
    def map(self, response: HttpResponse) -> GetGrantOffers1ErrorBody:
        match response.status_code:
            case 404 | 422:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


get_grant_offers1_error_mapper: Final[ErrorMapper[GetGrantOffers1ErrorBody]] = _GetGrantOffers1Error()
