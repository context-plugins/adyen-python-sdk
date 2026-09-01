from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostPaymentsDetails1ErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostPaymentsDetails1Error:
    def map(self, response: HttpResponse) -> PostPaymentsDetails1ErrorBody:
        match response.status_code:
            case 400 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


post_payments_details1_error_mapper: Final[ErrorMapper[PostPaymentsDetails1ErrorBody]] = _PostPaymentsDetails1Error()
