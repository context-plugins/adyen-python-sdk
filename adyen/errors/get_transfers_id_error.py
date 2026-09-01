from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.transfer_service_rest_service_error import TransferServiceRestServiceError

GetTransfersIdErrorBody: TypeAlias = TransferServiceRestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _GetTransfersIdError:
    def map(self, response: HttpResponse) -> GetTransfersIdErrorBody:
        match response.status_code:
            case 401 | 403 | 422 | 500:
                return decode_json[TransferServiceRestServiceError](response)
            case _:
                return RawError(response)


get_transfers_id_error_mapper: Final[ErrorMapper[GetTransfersIdErrorBody]] = _GetTransfersIdError()
