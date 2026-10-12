from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsErrorBody: TypeAlias = (
    DefaultErrorResponseEntity | RawError
)


@dataclass(frozen=True, slots=True)
class _PostBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsError:
    def map(
        self, status_code: int, content: bytes
    ) -> PostBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


post_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_error_mapper: Final[
    ErrorMapper[PostBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsErrorBody]
] = _PostBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsError()
