from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PatchNetworkTokensNetworkTokenIdErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PatchNetworkTokensNetworkTokenIdError:
    def map(self, status_code: int, content: bytes) -> PatchNetworkTokensNetworkTokenIdErrorBody:
        match status_code:
            case 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](content)
            case _:
                return RawError(status_code, content)


patch_network_tokens_network_token_id_error_mapper: Final[
    ErrorMapper[PatchNetworkTokensNetworkTokenIdErrorBody]
] = _PatchNetworkTokensNetworkTokenIdError()
