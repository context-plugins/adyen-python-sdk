from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostDynamicOffersIdCalculateErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostDynamicOffersIdCalculateError:
    def map(self, response: HttpResponse) -> PostDynamicOffersIdCalculateErrorBody:
        match response.status_code:
            case 422:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


post_dynamic_offers_id_calculate_error_mapper: Final[
    ErrorMapper[PostDynamicOffersIdCalculateErrorBody]
] = _PostDynamicOffersIdCalculateError()
