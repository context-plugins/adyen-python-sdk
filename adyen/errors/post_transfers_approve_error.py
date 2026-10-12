from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.service_error1 import ServiceError1
from ..models.transfer_service_rest_service_error import TransferServiceRestServiceError

PostTransfersApproveErrorBody: TypeAlias = ServiceError1 | TransferServiceRestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostTransfersApproveError:
    def map(self, status_code: int, content: bytes) -> PostTransfersApproveErrorBody:
        match status_code:
            case 401:
                return decode_json[ServiceError1](content)
            case 403 | 422 | 500:
                return decode_json[TransferServiceRestServiceError](content)
            case _:
                return RawError(status_code, content)


post_transfers_approve_error_mapper: Final[ErrorMapper[PostTransfersApproveErrorBody]] = _PostTransfersApproveError()
