from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PatchMerchantsMerchantIdApiCredentialsApiCredentialIdErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PatchMerchantsMerchantIdApiCredentialsApiCredentialIdError:
    def map(self, status_code: int, content: bytes) -> PatchMerchantsMerchantIdApiCredentialsApiCredentialIdErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](content)
            case _:
                return RawError(status_code, content)


patch_merchants_merchant_id_api_credentials_api_credential_id_error_mapper: Final[
    ErrorMapper[PatchMerchantsMerchantIdApiCredentialsApiCredentialIdErrorBody]
] = _PatchMerchantsMerchantIdApiCredentialsApiCredentialIdError()
