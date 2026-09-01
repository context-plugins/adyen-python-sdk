from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

DeleteMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody: TypeAlias = (
    RestServiceError | RawError
)


@dataclass(frozen=True, slots=True)
class _DeleteMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdError:
    def map(
        self, response: HttpResponse
    ) -> DeleteMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id_error_mapper: Final[
    ErrorMapper[DeleteMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody]
] = _DeleteMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdError()
