from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

GetMerchantsMerchantIdStoresStoreIdPaymentsAppsErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _GetMerchantsMerchantIdStoresStoreIdPaymentsAppsError:
    def map(self, status_code: int, content: bytes) -> GetMerchantsMerchantIdStoresStoreIdPaymentsAppsErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


get_merchants_merchant_id_stores_store_id_payments_apps_error_mapper: Final[
    ErrorMapper[GetMerchantsMerchantIdStoresStoreIdPaymentsAppsErrorBody]
] = _GetMerchantsMerchantIdStoresStoreIdPaymentsAppsError()
