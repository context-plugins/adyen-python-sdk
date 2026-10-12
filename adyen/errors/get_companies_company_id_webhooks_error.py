from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.rest_service_error import RestServiceError

GetCompaniesCompanyIdWebhooksErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _GetCompaniesCompanyIdWebhooksError:
    def map(self, status_code: int, content: bytes) -> GetCompaniesCompanyIdWebhooksErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](content)
            case _:
                return RawError(status_code, content)


get_companies_company_id_webhooks_error_mapper: Final[
    ErrorMapper[GetCompaniesCompanyIdWebhooksErrorBody]
] = _GetCompaniesCompanyIdWebhooksError()
