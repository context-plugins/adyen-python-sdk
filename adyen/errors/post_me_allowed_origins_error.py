from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PostMeAllowedOriginsErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostMeAllowedOriginsError:
    def map(self, response: HttpResponse) -> PostMeAllowedOriginsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


post_me_allowed_origins_error_mapper: Final[ErrorMapper[PostMeAllowedOriginsErrorBody]] = _PostMeAllowedOriginsError()
