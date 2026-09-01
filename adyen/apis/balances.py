from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RequestOptionsOrDict,
    json_body,
    json_decoder,
    param,
)
from ..errors.delete_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id_error import (
    DeleteBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody,
    delete_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id_error_mapper,
)
from ..errors.get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_error import (
    GetBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsErrorBody,
    get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_error_mapper,
)
from ..errors.get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id_error import (
    GetBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody,
    get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id_error_mapper,
)
from ..errors.patch_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id_error import (
    PatchBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody,
    patch_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id_error_mapper,
)
from ..errors.post_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_error import (
    PostBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsErrorBody,
    post_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_error_mapper,
)
from ..models.balance_webhook_setting_info import BalanceWebhookSettingInfo, BalanceWebhookSettingInfoDict
from ..models.balance_webhook_setting_info_update import (
    BalanceWebhookSettingInfoUpdate,
    BalanceWebhookSettingInfoUpdateDict,
)
from ..models.unions.webhook_setting import WebhookSetting
from ..models.webhook_settings import WebhookSettings
from ..server.server import Server


class Balances:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = BalancesWithRawResponse(client, server)

    def delete_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
        self,
        balance_platform_id: str,
        webhook_id: str,
        setting_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Deletes a balance webhook setting that contains the conditions for triggering `balance webhooks
        <https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated>`__.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            setting_id: The unique identifier of the balance webhook setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - the request has been successfully processed, but there is no additional content.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Not Found - the payment was not
                found Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.delete_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
            balance_platform_id, webhook_id, setting_id, request_options=request_options
        ).unwrap()

    def get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings(
        self, balance_platform_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> WebhookSettings:
        """Returns all balance webhook settings configured for triggering `balance webhooks
        <https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated>`__.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Not Found - the payment was not
                found Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings(
            balance_platform_id, webhook_id, request_options=request_options
        ).unwrap()

    def get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
        self,
        balance_platform_id: str,
        webhook_id: str,
        setting_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WebhookSetting:
        """Returns the details of a specific balance webhook setting configured for triggering `balance webhooks
        <https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated>`__.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            setting_id: The unique identifier of the balance webhook setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Not Found - the payment was not
                found Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
            balance_platform_id, webhook_id, setting_id, request_options=request_options
        ).unwrap()

    def patch_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
        self,
        balance_platform_id: str,
        webhook_id: str,
        setting_id: str,
        body: BalanceWebhookSettingInfoUpdate | BalanceWebhookSettingInfoUpdateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WebhookSetting:
        """Updates the conditions the balance change needs to meet for Adyen to send a `balance webhook
        <https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated>`__.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            setting_id: The unique identifier of the balance webhook setting.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Not Found - the payment was not
                found Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.patch_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
            balance_platform_id, webhook_id, setting_id, body, request_options=request_options
        ).unwrap()

    def post_balance_platforms_balance_platform_id_webhooks_webhook_id_settings(
        self,
        balance_platform_id: str,
        webhook_id: str,
        body: BalanceWebhookSettingInfo | BalanceWebhookSettingInfoDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WebhookSetting:
        """Configures the criteria for triggering `balance webhooks
        <https://docs.adyen.com/api-explorer/balance-webhooks/1/post/balancePlatform.balanceAccount.balance.updated>`__.

        Adyen sends balance webhooks to notify you of balance changes in your balance platform. They can be triggered
        when the balance reaches, exceeds, or drops below a specific value in a specific currency.

        You can get notified about balance changes in your entire balance platform, in the balance accounts of a
        specific user, or a specific balance account. The hierarchy between the webhook settings are based on the
        following business logic:

        * Settings on a higher level apply to all lower level resources (balance platform > account holder > balance
            acocunt).

        * The most granular setting overrides higher level settings (balance account > account holder > balance
            platform).

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Not Found - the payment was not
                found Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.post_balance_platforms_balance_platform_id_webhooks_webhook_id_settings(
            balance_platform_id, webhook_id, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> BalancesWithRawResponse:
        return self._with_raw_response


class AsyncBalances:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncBalancesWithRawResponse(client, server)

    async def delete_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
        self,
        balance_platform_id: str,
        webhook_id: str,
        setting_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Deletes a balance webhook setting that contains the conditions for triggering `balance webhooks
        <https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated>`__.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            setting_id: The unique identifier of the balance webhook setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - the request has been successfully processed, but there is no additional content.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Not Found - the payment was not
                found Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.delete_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
                balance_platform_id, webhook_id, setting_id, request_options=request_options
            )
        ).unwrap()

    async def get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings(
        self, balance_platform_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> WebhookSettings:
        """Returns all balance webhook settings configured for triggering `balance webhooks
        <https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated>`__.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Not Found - the payment was not
                found Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings(
                balance_platform_id, webhook_id, request_options=request_options
            )
        ).unwrap()

    async def get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
        self,
        balance_platform_id: str,
        webhook_id: str,
        setting_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WebhookSetting:
        """Returns the details of a specific balance webhook setting configured for triggering `balance webhooks
        <https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated>`__.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            setting_id: The unique identifier of the balance webhook setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Not Found - the payment was not
                found Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
                balance_platform_id, webhook_id, setting_id, request_options=request_options
            )
        ).unwrap()

    async def patch_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
        self,
        balance_platform_id: str,
        webhook_id: str,
        setting_id: str,
        body: BalanceWebhookSettingInfoUpdate | BalanceWebhookSettingInfoUpdateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WebhookSetting:
        """Updates the conditions the balance change needs to meet for Adyen to send a `balance webhook
        <https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated>`__.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            setting_id: The unique identifier of the balance webhook setting.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Not Found - the payment was not
                found Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.patch_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
                balance_platform_id, webhook_id, setting_id, body, request_options=request_options
            )
        ).unwrap()

    async def post_balance_platforms_balance_platform_id_webhooks_webhook_id_settings(
        self,
        balance_platform_id: str,
        webhook_id: str,
        body: BalanceWebhookSettingInfo | BalanceWebhookSettingInfoDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WebhookSetting:
        """Configures the criteria for triggering `balance webhooks
        <https://docs.adyen.com/api-explorer/balance-webhooks/1/post/balancePlatform.balanceAccount.balance.updated>`__.

        Adyen sends balance webhooks to notify you of balance changes in your balance platform. They can be triggered
        when the balance reaches, exceeds, or drops below a specific value in a specific currency.

        You can get notified about balance changes in your entire balance platform, in the balance accounts of a
        specific user, or a specific balance account. The hierarchy between the webhook settings are based on the
        following business logic:

        * Settings on a higher level apply to all lower level resources (balance platform > account holder > balance
            acocunt).

        * The most granular setting overrides higher level settings (balance account > account holder > balance
            platform).

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Not Found - the payment was not
                found Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.post_balance_platforms_balance_platform_id_webhooks_webhook_id_settings(
                balance_platform_id, webhook_id, body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncBalancesWithRawResponse:
        return self._with_raw_response


class BalancesWithRawResponse(BaseRawResponse[RawClient, Server]):
    def delete_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
        self,
        balance_platform_id: str,
        webhook_id: str,
        setting_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, DeleteBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody]:
        """Deletes a balance webhook setting that contains the conditions for triggering `balance webhooks
        <https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated>`__.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            setting_id: The unique identifier of the balance webhook setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13(
                "/balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId}"
            ),
            path_params=[
                param[str]("balancePlatformId", balance_platform_id),
                param[str]("webhookId", webhook_id),
                param[str]("settingId", setting_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=json_decoder[Any],
            error_mapper=delete_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id_error_mapper,
            request_options=request_options,
        )

    def get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings(
        self, balance_platform_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[WebhookSettings, GetBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsErrorBody]:
        """Returns all balance webhook settings configured for triggering `balance webhooks
        <https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated>`__.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings"),
            path_params=[param[str]("balancePlatformId", balance_platform_id), param[str]("webhookId", webhook_id)],
            decoder=json_decoder[WebhookSettings],
            error_mapper=get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_error_mapper,
            request_options=request_options,
        )

    def get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
        self,
        balance_platform_id: str,
        webhook_id: str,
        setting_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WebhookSetting, GetBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody]:
        """Returns the details of a specific balance webhook setting configured for triggering `balance webhooks
        <https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated>`__.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            setting_id: The unique identifier of the balance webhook setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13(
                "/balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId}"
            ),
            path_params=[
                param[str]("balancePlatformId", balance_platform_id),
                param[str]("webhookId", webhook_id),
                param[str]("settingId", setting_id),
            ],
            decoder=json_decoder[WebhookSetting],
            error_mapper=get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id_error_mapper,
            request_options=request_options,
        )

    def patch_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
        self,
        balance_platform_id: str,
        webhook_id: str,
        setting_id: str,
        body: BalanceWebhookSettingInfoUpdate | BalanceWebhookSettingInfoUpdateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WebhookSetting, PatchBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody]:
        """Updates the conditions the balance change needs to meet for Adyen to send a `balance webhook
        <https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated>`__.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            setting_id: The unique identifier of the balance webhook setting.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13(
                "/balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId}"
            ),
            path_params=[
                param[str]("balancePlatformId", balance_platform_id),
                param[str]("webhookId", webhook_id),
                param[str]("settingId", setting_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BalanceWebhookSettingInfoUpdate | BalanceWebhookSettingInfoUpdateDict](body),
            decoder=json_decoder[WebhookSetting],
            error_mapper=patch_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id_error_mapper,
            request_options=request_options,
        )

    def post_balance_platforms_balance_platform_id_webhooks_webhook_id_settings(
        self,
        balance_platform_id: str,
        webhook_id: str,
        body: BalanceWebhookSettingInfo | BalanceWebhookSettingInfoDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WebhookSetting, PostBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsErrorBody]:
        """Configures the criteria for triggering `balance webhooks
        <https://docs.adyen.com/api-explorer/balance-webhooks/1/post/balancePlatform.balanceAccount.balance.updated>`__.

        Adyen sends balance webhooks to notify you of balance changes in your balance platform. They can be triggered
        when the balance reaches, exceeds, or drops below a specific value in a specific currency.

        You can get notified about balance changes in your entire balance platform, in the balance accounts of a
        specific user, or a specific balance account. The hierarchy between the webhook settings are based on the
        following business logic:

        * Settings on a higher level apply to all lower level resources (balance platform > account holder > balance
            acocunt).

        * The most granular setting overrides higher level settings (balance account > account holder > balance
            platform).

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings"),
            path_params=[param[str]("balancePlatformId", balance_platform_id), param[str]("webhookId", webhook_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BalanceWebhookSettingInfo | BalanceWebhookSettingInfoDict](body),
            decoder=json_decoder[WebhookSetting],
            error_mapper=post_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_error_mapper,
            request_options=request_options,
        )


class AsyncBalancesWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def delete_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
        self,
        balance_platform_id: str,
        webhook_id: str,
        setting_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, DeleteBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody]:
        """Deletes a balance webhook setting that contains the conditions for triggering `balance webhooks
        <https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated>`__.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            setting_id: The unique identifier of the balance webhook setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13(
                "/balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId}"
            ),
            path_params=[
                param[str]("balancePlatformId", balance_platform_id),
                param[str]("webhookId", webhook_id),
                param[str]("settingId", setting_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=json_decoder[Any],
            error_mapper=delete_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id_error_mapper,
            request_options=request_options,
        )

    async def get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings(
        self, balance_platform_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[WebhookSettings, GetBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsErrorBody]:
        """Returns all balance webhook settings configured for triggering `balance webhooks
        <https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated>`__.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings"),
            path_params=[param[str]("balancePlatformId", balance_platform_id), param[str]("webhookId", webhook_id)],
            decoder=json_decoder[WebhookSettings],
            error_mapper=get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_error_mapper,
            request_options=request_options,
        )

    async def get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
        self,
        balance_platform_id: str,
        webhook_id: str,
        setting_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WebhookSetting, GetBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody]:
        """Returns the details of a specific balance webhook setting configured for triggering `balance webhooks
        <https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated>`__.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            setting_id: The unique identifier of the balance webhook setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13(
                "/balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId}"
            ),
            path_params=[
                param[str]("balancePlatformId", balance_platform_id),
                param[str]("webhookId", webhook_id),
                param[str]("settingId", setting_id),
            ],
            decoder=json_decoder[WebhookSetting],
            error_mapper=get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id_error_mapper,
            request_options=request_options,
        )

    async def patch_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
        self,
        balance_platform_id: str,
        webhook_id: str,
        setting_id: str,
        body: BalanceWebhookSettingInfoUpdate | BalanceWebhookSettingInfoUpdateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WebhookSetting, PatchBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsSettingIdErrorBody]:
        """Updates the conditions the balance change needs to meet for Adyen to send a `balance webhook
        <https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated>`__.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            setting_id: The unique identifier of the balance webhook setting.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13(
                "/balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId}"
            ),
            path_params=[
                param[str]("balancePlatformId", balance_platform_id),
                param[str]("webhookId", webhook_id),
                param[str]("settingId", setting_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BalanceWebhookSettingInfoUpdate | BalanceWebhookSettingInfoUpdateDict](body),
            decoder=json_decoder[WebhookSetting],
            error_mapper=patch_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id_error_mapper,
            request_options=request_options,
        )

    async def post_balance_platforms_balance_platform_id_webhooks_webhook_id_settings(
        self,
        balance_platform_id: str,
        webhook_id: str,
        body: BalanceWebhookSettingInfo | BalanceWebhookSettingInfoDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WebhookSetting, PostBalancePlatformsBalancePlatformIdWebhooksWebhookIdSettingsErrorBody]:
        """Configures the criteria for triggering `balance webhooks
        <https://docs.adyen.com/api-explorer/balance-webhooks/1/post/balancePlatform.balanceAccount.balance.updated>`__.

        Adyen sends balance webhooks to notify you of balance changes in your balance platform. They can be triggered
        when the balance reaches, exceeds, or drops below a specific value in a specific currency.

        You can get notified about balance changes in your entire balance platform, in the balance accounts of a
        specific user, or a specific balance account. The hierarchy between the webhook settings are based on the
        following business logic:

        * Settings on a higher level apply to all lower level resources (balance platform > account holder > balance
            acocunt).

        * The most granular setting overrides higher level settings (balance account > account holder > balance
            platform).

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            webhook_id: The unique identifier of the balance webhook.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings"),
            path_params=[param[str]("balancePlatformId", balance_platform_id), param[str]("webhookId", webhook_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BalanceWebhookSettingInfo | BalanceWebhookSettingInfoDict](body),
            decoder=json_decoder[WebhookSetting],
            error_mapper=post_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_error_mapper,
            request_options=request_options,
        )
