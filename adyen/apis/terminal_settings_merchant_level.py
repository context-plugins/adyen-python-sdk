from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
)
from ..errors.get_merchants_merchant_id_terminal_logos_error import (
    GetMerchantsMerchantIdTerminalLogosErrorBody,
    get_merchants_merchant_id_terminal_logos_error_mapper,
)
from ..errors.get_merchants_merchant_id_terminal_settings_error import (
    GetMerchantsMerchantIdTerminalSettingsErrorBody,
    get_merchants_merchant_id_terminal_settings_error_mapper,
)
from ..errors.patch_merchants_merchant_id_terminal_logos_error import (
    PatchMerchantsMerchantIdTerminalLogosErrorBody,
    patch_merchants_merchant_id_terminal_logos_error_mapper,
)
from ..errors.patch_merchants_merchant_id_terminal_settings_error import (
    PatchMerchantsMerchantIdTerminalSettingsErrorBody,
    patch_merchants_merchant_id_terminal_settings_error_mapper,
)
from ..models.logo import Logo, LogoDict
from ..models.terminal_settings import TerminalSettings, TerminalSettingsDict
from ..server.server import Server


class TerminalSettingsMerchantLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TerminalSettingsMerchantLevelWithRawResponse(client, server, auth)

    def get_merchants_merchant_id_terminal_logos(
        self, merchant_id: str, model: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Logo:
        """Returns the logo that is configured for a specific payment terminal model at the merchant account identified
        in the path. The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the
        actual image file. This logo applies to all terminals of the specified model under the merchant account, unless
        a different logo is configured at a lower level (store or individual terminal).

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_terminal_logos(
            merchant_id, model, request_options=request_options
        ).unwrap()

    def get_merchants_merchant_id_terminal_settings(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TerminalSettings:
        """Returns the payment terminal settings that are configured for the merchant account identified in the path.
        These settings apply to all terminals under the merchant account unless different values are configured at a
        lower level (store or individual terminal).

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        For `sensitive terminal settings
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings>`__,
        your API credential must have the following role:
        * Management API—Terminal settings Advanced read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_terminal_settings(
            merchant_id, request_options=request_options
        ).unwrap()

    def patch_merchants_merchant_id_terminal_logos(
        self,
        merchant_id: str,
        model: str,
        *,
        body: Logo | LogoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Logo:
        """Updates the logo for a specific payment terminal model at the merchant account identified in the path. You
        can update the logo for only one terminal model at a time. This logo applies to all terminals of the specified
        model under the merchant account, unless a different logo is configured at a lower level (store or individual
        terminal).

        * To change the logo, specify the image file as a Base64-encoded string.
        * To restore the logo inherited from the company account, specify an empty logo value.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            model: The terminal model. Allowed values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_merchants_merchant_id_terminal_logos(
            merchant_id, model, body=body, request_options=request_options
        ).unwrap()

    def patch_merchants_merchant_id_terminal_settings(
        self,
        merchant_id: str,
        *,
        body: TerminalSettings | TerminalSettingsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalSettings:
        """Updates payment terminal settings for the merchant account identified in the path. These settings apply to
        all terminals under the merchant account, unless different values are configured at a lower level (store or
        individual terminal).

        * To change a parameter value, include the full object that contains the parameter, even if you don't want to
            change all parameters in the object.
        * To restore a parameter value inherited from a higher level, include the full object that contains the
            parameter, and specify an empty value for the parameter or omit the parameter.
        * Objects that are not included in the request are not updated.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write



        For `sensitive terminal settings
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings>`__,
        your API credential must have the following role:
        * Management API—Terminal settings Advanced read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_merchants_merchant_id_terminal_settings(
            merchant_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TerminalSettingsMerchantLevelWithRawResponse:
        return self._with_raw_response


class AsyncTerminalSettingsMerchantLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTerminalSettingsMerchantLevelWithRawResponse(client, server, auth)

    async def get_merchants_merchant_id_terminal_logos(
        self, merchant_id: str, model: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Logo:
        """Returns the logo that is configured for a specific payment terminal model at the merchant account identified
        in the path. The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the
        actual image file. This logo applies to all terminals of the specified model under the merchant account, unless
        a different logo is configured at a lower level (store or individual terminal).

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_merchants_merchant_id_terminal_logos(
                merchant_id, model, request_options=request_options
            )
        ).unwrap()

    async def get_merchants_merchant_id_terminal_settings(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TerminalSettings:
        """Returns the payment terminal settings that are configured for the merchant account identified in the path.
        These settings apply to all terminals under the merchant account unless different values are configured at a
        lower level (store or individual terminal).

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        For `sensitive terminal settings
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings>`__,
        your API credential must have the following role:
        * Management API—Terminal settings Advanced read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_merchants_merchant_id_terminal_settings(
                merchant_id, request_options=request_options
            )
        ).unwrap()

    async def patch_merchants_merchant_id_terminal_logos(
        self,
        merchant_id: str,
        model: str,
        *,
        body: Logo | LogoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Logo:
        """Updates the logo for a specific payment terminal model at the merchant account identified in the path. You
        can update the logo for only one terminal model at a time. This logo applies to all terminals of the specified
        model under the merchant account, unless a different logo is configured at a lower level (store or individual
        terminal).

        * To change the logo, specify the image file as a Base64-encoded string.
        * To restore the logo inherited from the company account, specify an empty logo value.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            model: The terminal model. Allowed values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.patch_merchants_merchant_id_terminal_logos(
                merchant_id, model, body=body, request_options=request_options
            )
        ).unwrap()

    async def patch_merchants_merchant_id_terminal_settings(
        self,
        merchant_id: str,
        *,
        body: TerminalSettings | TerminalSettingsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalSettings:
        """Updates payment terminal settings for the merchant account identified in the path. These settings apply to
        all terminals under the merchant account, unless different values are configured at a lower level (store or
        individual terminal).

        * To change a parameter value, include the full object that contains the parameter, even if you don't want to
            change all parameters in the object.
        * To restore a parameter value inherited from a higher level, include the full object that contains the
            parameter, and specify an empty value for the parameter or omit the parameter.
        * Objects that are not included in the request are not updated.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write



        For `sensitive terminal settings
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings>`__,
        your API credential must have the following role:
        * Management API—Terminal settings Advanced read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.patch_merchants_merchant_id_terminal_settings(
                merchant_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTerminalSettingsMerchantLevelWithRawResponse:
        return self._with_raw_response


class TerminalSettingsMerchantLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_merchants_merchant_id_terminal_logos(
        self, merchant_id: str, model: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Logo, GetMerchantsMerchantIdTerminalLogosErrorBody]:
        """Returns the logo that is configured for a specific payment terminal model at the merchant account identified
        in the path. The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the
        actual image file. This logo applies to all terminals of the specified model under the merchant account, unless
        a different logo is configured at a lower level (store or individual terminal).

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/terminalLogos"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[param[str]("model", model)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Logo],
            error_mapper=get_merchants_merchant_id_terminal_logos_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_terminal_settings(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalSettings, GetMerchantsMerchantIdTerminalSettingsErrorBody]:
        """Returns the payment terminal settings that are configured for the merchant account identified in the path.
        These settings apply to all terminals under the merchant account unless different values are configured at a
        lower level (store or individual terminal).

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        For `sensitive terminal settings
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings>`__,
        your API credential must have the following role:
        * Management API—Terminal settings Advanced read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/terminalSettings"),
            path_params=[param[str]("merchantId", merchant_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalSettings],
            error_mapper=get_merchants_merchant_id_terminal_settings_error_mapper,
            request_options=request_options,
        )

    def patch_merchants_merchant_id_terminal_logos(
        self,
        merchant_id: str,
        model: str,
        *,
        body: Logo | LogoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Logo, PatchMerchantsMerchantIdTerminalLogosErrorBody]:
        """Updates the logo for a specific payment terminal model at the merchant account identified in the path. You
        can update the logo for only one terminal model at a time. This logo applies to all terminals of the specified
        model under the merchant account, unless a different logo is configured at a lower level (store or individual
        terminal).

        * To change the logo, specify the image file as a Base64-encoded string.
        * To restore the logo inherited from the company account, specify an empty logo value.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            model: The terminal model. Allowed values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/terminalLogos"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[param[str]("model", model)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Logo | LogoDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Logo],
            error_mapper=patch_merchants_merchant_id_terminal_logos_error_mapper,
            request_options=request_options,
        )

    def patch_merchants_merchant_id_terminal_settings(
        self,
        merchant_id: str,
        *,
        body: TerminalSettings | TerminalSettingsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalSettings, PatchMerchantsMerchantIdTerminalSettingsErrorBody]:
        """Updates payment terminal settings for the merchant account identified in the path. These settings apply to
        all terminals under the merchant account, unless different values are configured at a lower level (store or
        individual terminal).

        * To change a parameter value, include the full object that contains the parameter, even if you don't want to
            change all parameters in the object.
        * To restore a parameter value inherited from a higher level, include the full object that contains the
            parameter, and specify an empty value for the parameter or omit the parameter.
        * Objects that are not included in the request are not updated.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write



        For `sensitive terminal settings
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings>`__,
        your API credential must have the following role:
        * Management API—Terminal settings Advanced read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/terminalSettings"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TerminalSettings | TerminalSettingsDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalSettings],
            error_mapper=patch_merchants_merchant_id_terminal_settings_error_mapper,
            request_options=request_options,
        )


class AsyncTerminalSettingsMerchantLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_merchants_merchant_id_terminal_logos(
        self, merchant_id: str, model: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Logo, GetMerchantsMerchantIdTerminalLogosErrorBody]:
        """Returns the logo that is configured for a specific payment terminal model at the merchant account identified
        in the path. The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the
        actual image file. This logo applies to all terminals of the specified model under the merchant account, unless
        a different logo is configured at a lower level (store or individual terminal).

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/terminalLogos"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[param[str]("model", model)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Logo],
            error_mapper=get_merchants_merchant_id_terminal_logos_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_terminal_settings(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalSettings, GetMerchantsMerchantIdTerminalSettingsErrorBody]:
        """Returns the payment terminal settings that are configured for the merchant account identified in the path.
        These settings apply to all terminals under the merchant account unless different values are configured at a
        lower level (store or individual terminal).

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        For `sensitive terminal settings
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings>`__,
        your API credential must have the following role:
        * Management API—Terminal settings Advanced read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/terminalSettings"),
            path_params=[param[str]("merchantId", merchant_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalSettings],
            error_mapper=get_merchants_merchant_id_terminal_settings_error_mapper,
            request_options=request_options,
        )

    async def patch_merchants_merchant_id_terminal_logos(
        self,
        merchant_id: str,
        model: str,
        *,
        body: Logo | LogoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Logo, PatchMerchantsMerchantIdTerminalLogosErrorBody]:
        """Updates the logo for a specific payment terminal model at the merchant account identified in the path. You
        can update the logo for only one terminal model at a time. This logo applies to all terminals of the specified
        model under the merchant account, unless a different logo is configured at a lower level (store or individual
        terminal).

        * To change the logo, specify the image file as a Base64-encoded string.
        * To restore the logo inherited from the company account, specify an empty logo value.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            model: The terminal model. Allowed values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/terminalLogos"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[param[str]("model", model)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Logo | LogoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Logo],
            error_mapper=patch_merchants_merchant_id_terminal_logos_error_mapper,
            request_options=request_options,
        )

    async def patch_merchants_merchant_id_terminal_settings(
        self,
        merchant_id: str,
        *,
        body: TerminalSettings | TerminalSettingsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalSettings, PatchMerchantsMerchantIdTerminalSettingsErrorBody]:
        """Updates payment terminal settings for the merchant account identified in the path. These settings apply to
        all terminals under the merchant account, unless different values are configured at a lower level (store or
        individual terminal).

        * To change a parameter value, include the full object that contains the parameter, even if you don't want to
            change all parameters in the object.
        * To restore a parameter value inherited from a higher level, include the full object that contains the
            parameter, and specify an empty value for the parameter or omit the parameter.
        * Objects that are not included in the request are not updated.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write



        For `sensitive terminal settings
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings>`__,
        your API credential must have the following role:
        * Management API—Terminal settings Advanced read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/terminalSettings"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TerminalSettings | TerminalSettingsDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalSettings],
            error_mapper=patch_merchants_merchant_id_terminal_settings_error_mapper,
            request_options=request_options,
        )
