from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.service_error import ServiceError

PostPaymentsPaymentPspReferenceRefundsErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostPaymentsPaymentPspReferenceRefundsError:
    def map(self, response: HttpResponse) -> PostPaymentsPaymentPspReferenceRefundsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError](response)
            case _:
                return RawError(response)


post_payments_payment_psp_reference_refunds_error_mapper: Final[
    ErrorMapper[PostPaymentsPaymentPspReferenceRefundsErrorBody]
] = _PostPaymentsPaymentPspReferenceRefundsError()
