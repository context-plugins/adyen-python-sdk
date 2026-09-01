from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PostMerchantsMerchantIdWebhooksErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostMerchantsMerchantIdWebhooksError:
    def map(self, response: HttpResponse) -> PostMerchantsMerchantIdWebhooksErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


post_merchants_merchant_id_webhooks_error_mapper: Final[
    ErrorMapper[PostMerchantsMerchantIdWebhooksErrorBody]
] = _PostMerchantsMerchantIdWebhooksError()
