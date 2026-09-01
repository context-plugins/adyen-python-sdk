from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

GetGrantOffersErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _GetGrantOffersError:
    def map(self, response: HttpResponse) -> GetGrantOffersErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


get_grant_offers_error_mapper: Final[ErrorMapper[GetGrantOffersErrorBody]] = _GetGrantOffersError()
