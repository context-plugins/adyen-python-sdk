from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

DeletePaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody: TypeAlias = (
    DefaultErrorResponseEntity | RawError
)


@dataclass(frozen=True, slots=True)
class _DeletePaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersError:
    def map(
        self, status_code: int, content: bytes
    ) -> DeletePaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody:
        match status_code:
            case 401 | 403:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


delete_payment_instruments_payment_instrument_id_authorised_card_users_error_mapper: Final[
    ErrorMapper[DeletePaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody]
] = _DeletePaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersError()
