from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PatchPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody: TypeAlias = (
    DefaultErrorResponseEntity | RawError
)


@dataclass(frozen=True, slots=True)
class _PatchPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersError:
    def map(
        self, status_code: int, content: bytes
    ) -> PatchPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


patch_payment_instruments_payment_instrument_id_authorised_card_users_error_mapper: Final[
    ErrorMapper[PatchPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody]
] = _PatchPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersError()
