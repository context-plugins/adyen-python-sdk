from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostMerchantsMerchantIdPaymentsAppsInstallationIdRevokeErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostMerchantsMerchantIdPaymentsAppsInstallationIdRevokeError:
    def map(self, status_code: int, content: bytes) -> PostMerchantsMerchantIdPaymentsAppsInstallationIdRevokeErrorBody:
        match status_code:
            case 400 | 401 | 500:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


post_merchants_merchant_id_payments_apps_installation_id_revoke_error_mapper: Final[
    ErrorMapper[PostMerchantsMerchantIdPaymentsAppsInstallationIdRevokeErrorBody]
] = _PostMerchantsMerchantIdPaymentsAppsInstallationIdRevokeError()
