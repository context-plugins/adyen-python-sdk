from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PostGrantsErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostGrantsError:
    def map(self, response: HttpResponse) -> PostGrantsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


post_grants_error_mapper: Final[ErrorMapper[PostGrantsErrorBody]] = _PostGrantsError()
