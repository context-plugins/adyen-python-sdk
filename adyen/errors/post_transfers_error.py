from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.service_error1 import ServiceError1
from ..models.transfer_service_rest_service_error import TransferServiceRestServiceError

PostTransfersErrorBody: TypeAlias = ServiceError1 | TransferServiceRestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostTransfersError:
    def map(self, response: HttpResponse) -> PostTransfersErrorBody:
        match response.status_code:
            case 401:
                return decode_json[ServiceError1](response)
            case 403 | 422 | 500:
                return decode_json[TransferServiceRestServiceError](response)
            case _:
                return RawError(response)


post_transfers_error_mapper: Final[ErrorMapper[PostTransfersErrorBody]] = _PostTransfersError()
