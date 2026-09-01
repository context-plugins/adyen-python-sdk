from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.transfer_service_rest_service_error import TransferServiceRestServiceError

PostTransfersTransferIdReturnsErrorBody: TypeAlias = TransferServiceRestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostTransfersTransferIdReturnsError:
    def map(self, response: HttpResponse) -> PostTransfersTransferIdReturnsErrorBody:
        match response.status_code:
            case 401 | 403 | 422 | 500:
                return decode_json[TransferServiceRestServiceError](response)
            case _:
                return RawError(response)


post_transfers_transfer_id_returns_error_mapper: Final[
    ErrorMapper[PostTransfersTransferIdReturnsErrorBody]
] = _PostTransfersTransferIdReturnsError()
