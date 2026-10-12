from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PostValidateBankAccountIdentificationErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostValidateBankAccountIdentificationError:
    def map(self, status_code: int, content: bytes) -> PostValidateBankAccountIdentificationErrorBody:
        match status_code:
            case 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](content)
            case _:
                return RawError(status_code, content)


post_validate_bank_account_identification_error_mapper: Final[
    ErrorMapper[PostValidateBankAccountIdentificationErrorBody]
] = _PostValidateBankAccountIdentificationError()
