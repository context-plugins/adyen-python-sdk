from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.rest_service_error import RestServiceError

DeleteCompaniesCompanyIdWebhooksWebhookIdErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteCompaniesCompanyIdWebhooksWebhookIdError:
    def map(self, status_code: int, content: bytes) -> DeleteCompaniesCompanyIdWebhooksWebhookIdErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](content)
            case _:
                return RawError(status_code, content)


delete_companies_company_id_webhooks_webhook_id_error_mapper: Final[
    ErrorMapper[DeleteCompaniesCompanyIdWebhooksWebhookIdErrorBody]
] = _DeleteCompaniesCompanyIdWebhooksWebhookIdError()
