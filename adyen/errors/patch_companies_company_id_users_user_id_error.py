from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PatchCompaniesCompanyIdUsersUserIdErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PatchCompaniesCompanyIdUsersUserIdError:
    def map(self, response: HttpResponse) -> PatchCompaniesCompanyIdUsersUserIdErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


patch_companies_company_id_users_user_id_error_mapper: Final[
    ErrorMapper[PatchCompaniesCompanyIdUsersUserIdErrorBody]
] = _PatchCompaniesCompanyIdUsersUserIdError()
