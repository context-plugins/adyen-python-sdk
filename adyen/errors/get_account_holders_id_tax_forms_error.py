from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.rest_service_error import RestServiceError

GetAccountHoldersIdTaxFormsErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _GetAccountHoldersIdTaxFormsError:
    def map(self, status_code: int, content: bytes) -> GetAccountHoldersIdTaxFormsErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404 | 422 | 500:
                return decode_json[RestServiceError](content)
            case _:
                return RawError(status_code, content)


get_account_holders_id_tax_forms_error_mapper: Final[
    ErrorMapper[GetAccountHoldersIdTaxFormsErrorBody]
] = _GetAccountHoldersIdTaxFormsError()
