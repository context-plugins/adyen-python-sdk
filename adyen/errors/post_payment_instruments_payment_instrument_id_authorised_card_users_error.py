from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersError:
    def map(self, response: HttpResponse) -> PostPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


post_payment_instruments_payment_instrument_id_authorised_card_users_error_mapper: Final[
    ErrorMapper[PostPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody]
] = _PostPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersError()
