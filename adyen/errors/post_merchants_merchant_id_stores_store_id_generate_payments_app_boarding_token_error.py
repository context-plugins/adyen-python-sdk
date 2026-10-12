from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostMerchantsMerchantIdStoresStoreIdGeneratePaymentsAppBoardingTokenErrorBody: TypeAlias = (
    DefaultErrorResponseEntity | RawError
)


@dataclass(frozen=True, slots=True)
class _PostMerchantsMerchantIdStoresStoreIdGeneratePaymentsAppBoardingTokenError:
    def map(
        self, status_code: int, content: bytes
    ) -> PostMerchantsMerchantIdStoresStoreIdGeneratePaymentsAppBoardingTokenErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


post_merchants_merchant_id_stores_store_id_generate_payments_app_boarding_token_error_mapper: Final[
    ErrorMapper[PostMerchantsMerchantIdStoresStoreIdGeneratePaymentsAppBoardingTokenErrorBody]
] = _PostMerchantsMerchantIdStoresStoreIdGeneratePaymentsAppBoardingTokenError()
