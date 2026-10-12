from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.service_error import ServiceError

PostPaymentMethodsBalanceErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostPaymentMethodsBalanceError:
    def map(self, status_code: int, content: bytes) -> PostPaymentMethodsBalanceErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError](content)
            case _:
                return RawError(status_code, content)


post_payment_methods_balance_error_mapper: Final[
    ErrorMapper[PostPaymentMethodsBalanceErrorBody]
] = _PostPaymentMethodsBalanceError()
