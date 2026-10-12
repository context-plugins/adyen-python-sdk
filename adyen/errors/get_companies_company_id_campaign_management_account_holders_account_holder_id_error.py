from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

GetCompaniesCompanyIdCampaignManagementAccountHoldersAccountHolderIdErrorBody: TypeAlias = (
    DefaultErrorResponseEntity | RawError
)


@dataclass(frozen=True, slots=True)
class _GetCompaniesCompanyIdCampaignManagementAccountHoldersAccountHolderIdError:
    def map(
        self, status_code: int, content: bytes
    ) -> GetCompaniesCompanyIdCampaignManagementAccountHoldersAccountHolderIdErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


get_companies_company_id_campaign_management_account_holders_account_holder_id_error_mapper: Final[
    ErrorMapper[GetCompaniesCompanyIdCampaignManagementAccountHoldersAccountHolderIdErrorBody]
] = _GetCompaniesCompanyIdCampaignManagementAccountHoldersAccountHolderIdError()
