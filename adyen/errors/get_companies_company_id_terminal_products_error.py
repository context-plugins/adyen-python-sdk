from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

GetCompaniesCompanyIdTerminalProductsErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _GetCompaniesCompanyIdTerminalProductsError:
    def map(self, response: HttpResponse) -> GetCompaniesCompanyIdTerminalProductsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


get_companies_company_id_terminal_products_error_mapper: Final[
    ErrorMapper[GetCompaniesCompanyIdTerminalProductsErrorBody]
] = _GetCompaniesCompanyIdTerminalProductsError()
