from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.service_error1 import ServiceError1

DeleteTransferInstrumentsIdErrorBody: TypeAlias = ServiceError1 | RawError


@dataclass(frozen=True, slots=True)
class _DeleteTransferInstrumentsIdError:
    def map(self, response: HttpResponse) -> DeleteTransferInstrumentsIdErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError1](response)
            case _:
                return RawError(response)


delete_transfer_instruments_id_error_mapper: Final[
    ErrorMapper[DeleteTransferInstrumentsIdErrorBody]
] = _DeleteTransferInstrumentsIdError()
