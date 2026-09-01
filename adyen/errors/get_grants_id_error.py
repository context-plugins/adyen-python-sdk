from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

GetGrantsIdErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _GetGrantsIdError:
    def map(self, response: HttpResponse) -> GetGrantsIdErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


get_grants_id_error_mapper: Final[ErrorMapper[GetGrantsIdErrorBody]] = _GetGrantsIdError()
