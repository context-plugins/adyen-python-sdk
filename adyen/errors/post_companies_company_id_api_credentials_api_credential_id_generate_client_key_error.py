from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PostCompaniesCompanyIdApiCredentialsApiCredentialIdGenerateClientKeyErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostCompaniesCompanyIdApiCredentialsApiCredentialIdGenerateClientKeyError:
    def map(
        self, response: HttpResponse
    ) -> PostCompaniesCompanyIdApiCredentialsApiCredentialIdGenerateClientKeyErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


post_companies_company_id_api_credentials_api_credential_id_generate_client_key_error_mapper: Final[
    ErrorMapper[PostCompaniesCompanyIdApiCredentialsApiCredentialIdGenerateClientKeyErrorBody]
] = _PostCompaniesCompanyIdApiCredentialsApiCredentialIdGenerateClientKeyError()
