from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostCompaniesCompanyIdCampaignManagementErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostCompaniesCompanyIdCampaignManagementError:
    def map(self, response: HttpResponse) -> PostCompaniesCompanyIdCampaignManagementErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


post_companies_company_id_campaign_management_error_mapper: Final[
    ErrorMapper[PostCompaniesCompanyIdCampaignManagementErrorBody]
] = _PostCompaniesCompanyIdCampaignManagementError()
