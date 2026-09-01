from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

GetNetworkTokensNetworkTokenIdErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _GetNetworkTokensNetworkTokenIdError:
    def map(self, response: HttpResponse) -> GetNetworkTokensNetworkTokenIdErrorBody:
        match response.status_code:
            case 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


get_network_tokens_network_token_id_error_mapper: Final[
    ErrorMapper[GetNetworkTokensNetworkTokenIdErrorBody]
] = _GetNetworkTokensNetworkTokenIdError()
