from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostDynamicOffersIdGrantOfferErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostDynamicOffersIdGrantOfferError:
    def map(self, status_code: int, content: bytes) -> PostDynamicOffersIdGrantOfferErrorBody:
        match status_code:
            case 422:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


post_dynamic_offers_id_grant_offer_error_mapper: Final[
    ErrorMapper[PostDynamicOffersIdGrantOfferErrorBody]
] = _PostDynamicOffersIdGrantOfferError()
