from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.rest_service_error import RestServiceError

GetMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomainsErrorBody: TypeAlias = (
    RestServiceError | RawError
)


@dataclass(frozen=True, slots=True)
class _GetMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomainsError:
    def map(
        self, status_code: int, content: bytes
    ) -> GetMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomainsErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](content)
            case _:
                return RawError(status_code, content)


get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains_error_mapper: Final[
    ErrorMapper[GetMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomainsErrorBody]
] = _GetMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomainsError()
