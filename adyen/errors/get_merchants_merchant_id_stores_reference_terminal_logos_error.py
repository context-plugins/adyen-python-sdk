from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

GetMerchantsMerchantIdStoresReferenceTerminalLogosErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _GetMerchantsMerchantIdStoresReferenceTerminalLogosError:
    def map(self, response: HttpResponse) -> GetMerchantsMerchantIdStoresReferenceTerminalLogosErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


get_merchants_merchant_id_stores_reference_terminal_logos_error_mapper: Final[
    ErrorMapper[GetMerchantsMerchantIdStoresReferenceTerminalLogosErrorBody]
] = _GetMerchantsMerchantIdStoresReferenceTerminalLogosError()
