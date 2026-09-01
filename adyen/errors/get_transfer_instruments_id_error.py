from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.service_error1 import ServiceError1

GetTransferInstrumentsIdErrorBody: TypeAlias = ServiceError1 | RawError


@dataclass(frozen=True, slots=True)
class _GetTransferInstrumentsIdError:
    def map(self, response: HttpResponse) -> GetTransferInstrumentsIdErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError1](response)
            case _:
                return RawError(response)


get_transfer_instruments_id_error_mapper: Final[
    ErrorMapper[GetTransferInstrumentsIdErrorBody]
] = _GetTransferInstrumentsIdError()
