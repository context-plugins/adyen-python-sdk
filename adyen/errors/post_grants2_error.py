from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostGrants2ErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostGrants2Error:
    def map(self, status_code: int, content: bytes) -> PostGrants2ErrorBody:
        match status_code:
            case 422:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


post_grants2_error_mapper: Final[ErrorMapper[PostGrants2ErrorBody]] = _PostGrants2Error()
