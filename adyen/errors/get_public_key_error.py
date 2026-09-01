from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

GetPublicKeyErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _GetPublicKeyError:
    def map(self, response: HttpResponse) -> GetPublicKeyErrorBody:
        match response.status_code:
            case 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


get_public_key_error_mapper: Final[ErrorMapper[GetPublicKeyErrorBody]] = _GetPublicKeyError()
