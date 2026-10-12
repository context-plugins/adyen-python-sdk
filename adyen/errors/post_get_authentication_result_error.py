from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.service_error import ServiceError

PostGetAuthenticationResultErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostGetAuthenticationResultError:
    def map(self, status_code: int, content: bytes) -> PostGetAuthenticationResultErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError](content)
            case _:
                return RawError(status_code, content)


post_get_authentication_result_error_mapper: Final[
    ErrorMapper[PostGetAuthenticationResultErrorBody]
] = _PostGetAuthenticationResultError()
