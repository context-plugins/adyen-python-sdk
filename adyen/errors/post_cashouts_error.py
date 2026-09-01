from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostCashoutsErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostCashoutsError:
    def map(self, response: HttpResponse) -> PostCashoutsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 422 | 429 | 500:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


post_cashouts_error_mapper: Final[ErrorMapper[PostCashoutsErrorBody]] = _PostCashoutsError()
