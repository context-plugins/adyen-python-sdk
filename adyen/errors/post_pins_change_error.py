from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PostPinsChangeErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostPinsChangeError:
    def map(self, response: HttpResponse) -> PostPinsChangeErrorBody:
        match response.status_code:
            case 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


post_pins_change_error_mapper: Final[ErrorMapper[PostPinsChangeErrorBody]] = _PostPinsChangeError()
