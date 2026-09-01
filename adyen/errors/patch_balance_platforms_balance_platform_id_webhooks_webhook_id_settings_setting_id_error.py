from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PatchBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody: TypeAlias = (
    DefaultErrorResponseEntity | RawError
)


@dataclass(frozen=True, slots=True)
class _PatchBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdError:
    def map(
        self, response: HttpResponse
    ) -> PatchBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


patch_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id_error_mapper: Final[
    ErrorMapper[PatchBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody]
] = _PatchBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdError()
