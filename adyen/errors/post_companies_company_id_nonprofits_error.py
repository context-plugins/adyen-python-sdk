from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostCompaniesCompanyIdNonprofitsErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostCompaniesCompanyIdNonprofitsError:
    def map(self, response: HttpResponse) -> PostCompaniesCompanyIdNonprofitsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


post_companies_company_id_nonprofits_error_mapper: Final[
    ErrorMapper[PostCompaniesCompanyIdNonprofitsErrorBody]
] = _PostCompaniesCompanyIdNonprofitsError()
