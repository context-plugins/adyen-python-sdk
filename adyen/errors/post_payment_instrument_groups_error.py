from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PostPaymentInstrumentGroupsErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostPaymentInstrumentGroupsError:
    def map(self, response: HttpResponse) -> PostPaymentInstrumentGroupsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


post_payment_instrument_groups_error_mapper: Final[
    ErrorMapper[PostPaymentInstrumentGroupsErrorBody]
] = _PostPaymentInstrumentGroupsError()
