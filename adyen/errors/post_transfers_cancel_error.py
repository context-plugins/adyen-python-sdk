from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.transfer_service_rest_service_error import TransferServiceRestServiceError

PostTransfersCancelErrorBody: TypeAlias = TransferServiceRestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostTransfersCancelError:
    def map(self, status_code: int, content: bytes) -> PostTransfersCancelErrorBody:
        match status_code:
            case 401 | 403 | 422 | 500:
                return decode_json[TransferServiceRestServiceError](content)
            case _:
                return RawError(status_code, content)


post_transfers_cancel_error_mapper: Final[ErrorMapper[PostTransfersCancelErrorBody]] = _PostTransfersCancelError()
