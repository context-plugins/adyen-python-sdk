from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PostCompaniesCompanyIdWebhooksWebhookIdGenerateHmacErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostCompaniesCompanyIdWebhooksWebhookIdGenerateHmacError:
    def map(self, response: HttpResponse) -> PostCompaniesCompanyIdWebhooksWebhookIdGenerateHmacErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


post_companies_company_id_webhooks_webhook_id_generate_hmac_error_mapper: Final[
    ErrorMapper[PostCompaniesCompanyIdWebhooksWebhookIdGenerateHmacErrorBody]
] = _PostCompaniesCompanyIdWebhooksWebhookIdGenerateHmacError()
