from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostGrants2ErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostGrants2Error:
    def map(self, response: HttpResponse) -> PostGrants2ErrorBody:
        match response.status_code:
            case 422:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


post_grants2_error_mapper: Final[ErrorMapper[PostGrants2ErrorBody]] = _PostGrants2Error()
