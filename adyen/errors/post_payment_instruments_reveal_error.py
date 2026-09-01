from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PostPaymentInstrumentsRevealErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostPaymentInstrumentsRevealError:
    def map(self, response: HttpResponse) -> PostPaymentInstrumentsRevealErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


post_payment_instruments_reveal_error_mapper: Final[
    ErrorMapper[PostPaymentInstrumentsRevealErrorBody]
] = _PostPaymentInstrumentsRevealError()
