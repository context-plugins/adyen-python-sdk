from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PostMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomainsErrorBody: TypeAlias = (
    RestServiceError | RawError
)


@dataclass(frozen=True, slots=True)
class _PostMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomainsError:
    def map(
        self, response: HttpResponse
    ) -> PostMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomainsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 429 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains_error_mapper: Final[
    ErrorMapper[PostMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomainsErrorBody]
] = _PostMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomainsError()
