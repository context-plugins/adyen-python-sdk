from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

GetStoresStoreIdTerminalSettingsErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _GetStoresStoreIdTerminalSettingsError:
    def map(self, response: HttpResponse) -> GetStoresStoreIdTerminalSettingsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


get_stores_store_id_terminal_settings_error_mapper: Final[
    ErrorMapper[GetStoresStoreIdTerminalSettingsErrorBody]
] = _GetStoresStoreIdTerminalSettingsError()
