from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

GetAccountVerificationReportsCodeErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _GetAccountVerificationReportsCodeError:
    def map(self, response: HttpResponse) -> GetAccountVerificationReportsCodeErrorBody:
        match response.status_code:
            case 400 | 401 | 404 | 422 | 429 | 500:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


get_account_verification_reports_code_error_mapper: Final[
    ErrorMapper[GetAccountVerificationReportsCodeErrorBody]
] = _GetAccountVerificationReportsCodeError()
