from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

GetPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _GetPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersError:
    def map(self, response: HttpResponse) -> GetPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody:
        match response.status_code:
            case 401 | 403 | 404 | 422:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


get_payment_instruments_payment_instrument_id_authorised_card_users_error_mapper: Final[
    ErrorMapper[GetPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody]
] = _GetPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersError()
