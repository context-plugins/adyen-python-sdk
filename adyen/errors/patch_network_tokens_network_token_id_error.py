from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PatchNetworkTokensNetworkTokenIdErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PatchNetworkTokensNetworkTokenIdError:
    def map(self, response: HttpResponse) -> PatchNetworkTokensNetworkTokenIdErrorBody:
        match response.status_code:
            case 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


patch_network_tokens_network_token_id_error_mapper: Final[
    ErrorMapper[PatchNetworkTokensNetworkTokenIdErrorBody]
] = _PatchNetworkTokensNetworkTokenIdError()
