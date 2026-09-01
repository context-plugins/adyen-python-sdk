from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

DeletePaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody: TypeAlias = (
    DefaultErrorResponseEntity | RawError
)


@dataclass(frozen=True, slots=True)
class _DeletePaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersError:
    def map(self, response: HttpResponse) -> DeletePaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody:
        match response.status_code:
            case 401 | 403:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


delete_payment_instruments_payment_instrument_id_authorised_card_users_error_mapper: Final[
    ErrorMapper[DeletePaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody]
] = _DeletePaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersError()
