from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostDynamicOffersIdCalculateErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostDynamicOffersIdCalculateError:
    def map(self, status_code: int, content: bytes) -> PostDynamicOffersIdCalculateErrorBody:
        match status_code:
            case 422:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


post_dynamic_offers_id_calculate_error_mapper: Final[
    ErrorMapper[PostDynamicOffersIdCalculateErrorBody]
] = _PostDynamicOffersIdCalculateError()
