from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

GetGrantAccountsIdErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _GetGrantAccountsIdError:
    def map(self, response: HttpResponse) -> GetGrantAccountsIdErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


get_grant_accounts_id_error_mapper: Final[ErrorMapper[GetGrantAccountsIdErrorBody]] = _GetGrantAccountsIdError()
