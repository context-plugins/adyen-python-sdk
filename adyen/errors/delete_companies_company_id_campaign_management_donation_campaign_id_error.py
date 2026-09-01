from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

DeleteCompaniesCompanyIdCampaignManagementDonationCampaignIdErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _DeleteCompaniesCompanyIdCampaignManagementDonationCampaignIdError:
    def map(self, response: HttpResponse) -> DeleteCompaniesCompanyIdCampaignManagementDonationCampaignIdErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


delete_companies_company_id_campaign_management_donation_campaign_id_error_mapper: Final[
    ErrorMapper[DeleteCompaniesCompanyIdCampaignManagementDonationCampaignIdErrorBody]
] = _DeleteCompaniesCompanyIdCampaignManagementDonationCampaignIdError()
