from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.rest_service_error import RestServiceError

GetPaymentInstrumentsIdRevealErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _GetPaymentInstrumentsIdRevealError:
    def map(self, status_code: int, content: bytes) -> GetPaymentInstrumentsIdRevealErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](content)
            case _:
                return RawError(status_code, content)


get_payment_instruments_id_reveal_error_mapper: Final[
    ErrorMapper[GetPaymentInstrumentsIdRevealErrorBody]
] = _GetPaymentInstrumentsIdRevealError()
