from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.service_error import ServiceError

PostPaypalUpdateOrderErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostPaypalUpdateOrderError:
    def map(self, response: HttpResponse) -> PostPaypalUpdateOrderErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError](response)
            case _:
                return RawError(response)


post_paypal_update_order_error_mapper: Final[
    ErrorMapper[PostPaypalUpdateOrderErrorBody]
] = _PostPaypalUpdateOrderError()
