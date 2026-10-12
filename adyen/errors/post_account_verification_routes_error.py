from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostAccountVerificationRoutesErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostAccountVerificationRoutesError:
    def map(self, status_code: int, content: bytes) -> PostAccountVerificationRoutesErrorBody:
        match status_code:
            case 400 | 401 | 422 | 429 | 500:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


post_account_verification_routes_error_mapper: Final[
    ErrorMapper[PostAccountVerificationRoutesErrorBody]
] = _PostAccountVerificationRoutesError()
