from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostPaymentsDetails1ErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostPaymentsDetails1Error:
    def map(self, status_code: int, content: bytes) -> PostPaymentsDetails1ErrorBody:
        match status_code:
            case 400 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


post_payments_details1_error_mapper: Final[ErrorMapper[PostPaymentsDetails1ErrorBody]] = _PostPaymentsDetails1Error()
