from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PatchMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PatchMerchantsMerchantIdPayoutSettingsPayoutSettingsIdError:
    def map(self, status_code: int, content: bytes) -> PatchMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](content)
            case _:
                return RawError(status_code, content)


patch_merchants_merchant_id_payout_settings_payout_settings_id_error_mapper: Final[
    ErrorMapper[PatchMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody]
] = _PatchMerchantsMerchantIdPayoutSettingsPayoutSettingsIdError()
