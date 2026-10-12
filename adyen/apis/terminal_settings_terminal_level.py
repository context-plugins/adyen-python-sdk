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
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.get_terminals_terminal_id_terminal_logos_error import (
    GetTerminalsTerminalIdTerminalLogosErrorBody,
    get_terminals_terminal_id_terminal_logos_error_mapper,
)
from ..errors.get_terminals_terminal_id_terminal_settings_error import (
    GetTerminalsTerminalIdTerminalSettingsErrorBody,
    get_terminals_terminal_id_terminal_settings_error_mapper,
)
from ..errors.patch_terminals_terminal_id_terminal_logos_error import (
    PatchTerminalsTerminalIdTerminalLogosErrorBody,
    patch_terminals_terminal_id_terminal_logos_error_mapper,
)
from ..errors.patch_terminals_terminal_id_terminal_settings_error import (
    PatchTerminalsTerminalIdTerminalSettingsErrorBody,
    patch_terminals_terminal_id_terminal_settings_error_mapper,
)
from ..models.logo import Logo, LogoDict
from ..models.terminal_settings import TerminalSettings, TerminalSettingsDict
from ..server.server import Server


class TerminalSettingsTerminalLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TerminalSettingsTerminalLevelWithRawResponse(client, server, auth)

    def get_terminals_terminal_id_terminal_logos(
        self, terminal_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Logo:
        """Returns the logo that is configured for the payment terminal identified in the path. The logo is returned as
        a Base64-encoded string. You need to Base64-decode the string to get the actual image file.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            terminal_id: The unique identifier of the payment terminal.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.get_terminals_terminal_id_terminal_logos(
                terminal_id, request_options=request_options
            ),
        )

    def get_terminals_terminal_id_terminal_settings(
        self, terminal_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TerminalSettings:
        """Returns the settings that are configured for the payment terminal identified in the path.

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
            terminal_id: The unique identifier of the payment terminal.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.get_terminals_terminal_id_terminal_settings(
                terminal_id, request_options=request_options
            ),
        )

    def patch_terminals_terminal_id_terminal_logos(
        self,
        terminal_id: str,
        *,
        body: Logo | LogoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Logo:
        """Updates the logo for the payment terminal identified in the path.

        * To change the logo, specify the image file as a Base64-encoded string.
        * To restore the logo inherited from a higher level (store, merchant account, or company account), specify an
            empty logo value.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            terminal_id: The unique identifier of the payment terminal.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.patch_terminals_terminal_id_terminal_logos(
                terminal_id, body=body, request_options=request_options
            ),
        )

    def patch_terminals_terminal_id_terminal_settings(
        self,
        terminal_id: str,
        *,
        body: TerminalSettings | TerminalSettingsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalSettings:
        """Updates the settings that are configured for the payment terminal identified in the path.

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
            terminal_id: The unique identifier of the payment terminal.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.patch_terminals_terminal_id_terminal_settings(
                terminal_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> TerminalSettingsTerminalLevelWithRawResponse:
        return self._with_raw_response


class AsyncTerminalSettingsTerminalLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTerminalSettingsTerminalLevelWithRawResponse(client, server, auth)

    async def get_terminals_terminal_id_terminal_logos(
        self, terminal_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Logo:
        """Returns the logo that is configured for the payment terminal identified in the path. The logo is returned as
        a Base64-encoded string. You need to Base64-decode the string to get the actual image file.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            terminal_id: The unique identifier of the payment terminal.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_terminals_terminal_id_terminal_logos(
                terminal_id, request_options=request_options
            ),
        )

    async def get_terminals_terminal_id_terminal_settings(
        self, terminal_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TerminalSettings:
        """Returns the settings that are configured for the payment terminal identified in the path.

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
            terminal_id: The unique identifier of the payment terminal.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_terminals_terminal_id_terminal_settings(
                terminal_id, request_options=request_options
            ),
        )

    async def patch_terminals_terminal_id_terminal_logos(
        self,
        terminal_id: str,
        *,
        body: Logo | LogoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Logo:
        """Updates the logo for the payment terminal identified in the path.

        * To change the logo, specify the image file as a Base64-encoded string.
        * To restore the logo inherited from a higher level (store, merchant account, or company account), specify an
            empty logo value.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            terminal_id: The unique identifier of the payment terminal.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.patch_terminals_terminal_id_terminal_logos(
                terminal_id, body=body, request_options=request_options
            ),
        )

    async def patch_terminals_terminal_id_terminal_settings(
        self,
        terminal_id: str,
        *,
        body: TerminalSettings | TerminalSettingsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalSettings:
        """Updates the settings that are configured for the payment terminal identified in the path.

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
            terminal_id: The unique identifier of the payment terminal.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.patch_terminals_terminal_id_terminal_settings(
                terminal_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncTerminalSettingsTerminalLevelWithRawResponse:
        return self._with_raw_response


class TerminalSettingsTerminalLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_terminals_terminal_id_terminal_logos(
        self, terminal_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Logo, GetTerminalsTerminalIdTerminalLogosErrorBody]:
        """Returns the logo that is configured for the payment terminal identified in the path. The logo is returned as
        a Base64-encoded string. You need to Base64-decode the string to get the actual image file.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            terminal_id: The unique identifier of the payment terminal.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/terminals/{terminalId}/terminalLogos"),
            path_params=[param[str]("terminalId", terminal_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Logo],
            error_mapper=get_terminals_terminal_id_terminal_logos_error_mapper,
            request_options=request_options,
        )

    def get_terminals_terminal_id_terminal_settings(
        self, terminal_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalSettings, GetTerminalsTerminalIdTerminalSettingsErrorBody]:
        """Returns the settings that are configured for the payment terminal identified in the path.

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
            terminal_id: The unique identifier of the payment terminal.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/terminals/{terminalId}/terminalSettings"),
            path_params=[param[str]("terminalId", terminal_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalSettings],
            error_mapper=get_terminals_terminal_id_terminal_settings_error_mapper,
            request_options=request_options,
        )

    def patch_terminals_terminal_id_terminal_logos(
        self,
        terminal_id: str,
        *,
        body: Logo | LogoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Logo, PatchTerminalsTerminalIdTerminalLogosErrorBody]:
        """Updates the logo for the payment terminal identified in the path.

        * To change the logo, specify the image file as a Base64-encoded string.
        * To restore the logo inherited from a higher level (store, merchant account, or company account), specify an
            empty logo value.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            terminal_id: The unique identifier of the payment terminal.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/terminals/{terminalId}/terminalLogos"),
            path_params=[param[str]("terminalId", terminal_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Logo | LogoDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Logo],
            error_mapper=patch_terminals_terminal_id_terminal_logos_error_mapper,
            request_options=request_options,
        )

    def patch_terminals_terminal_id_terminal_settings(
        self,
        terminal_id: str,
        *,
        body: TerminalSettings | TerminalSettingsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalSettings, PatchTerminalsTerminalIdTerminalSettingsErrorBody]:
        """Updates the settings that are configured for the payment terminal identified in the path.

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
            terminal_id: The unique identifier of the payment terminal.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/terminals/{terminalId}/terminalSettings"),
            path_params=[param[str]("terminalId", terminal_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TerminalSettings | TerminalSettingsDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalSettings],
            error_mapper=patch_terminals_terminal_id_terminal_settings_error_mapper,
            request_options=request_options,
        )


class AsyncTerminalSettingsTerminalLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_terminals_terminal_id_terminal_logos(
        self, terminal_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Logo, GetTerminalsTerminalIdTerminalLogosErrorBody]:
        """Returns the logo that is configured for the payment terminal identified in the path. The logo is returned as
        a Base64-encoded string. You need to Base64-decode the string to get the actual image file.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            terminal_id: The unique identifier of the payment terminal.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/terminals/{terminalId}/terminalLogos"),
            path_params=[param[str]("terminalId", terminal_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[Logo],
            error_mapper=get_terminals_terminal_id_terminal_logos_error_mapper,
            request_options=request_options,
        )

    async def get_terminals_terminal_id_terminal_settings(
        self, terminal_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalSettings, GetTerminalsTerminalIdTerminalSettingsErrorBody]:
        """Returns the settings that are configured for the payment terminal identified in the path.

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
            terminal_id: The unique identifier of the payment terminal.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/terminals/{terminalId}/terminalSettings"),
            path_params=[param[str]("terminalId", terminal_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[TerminalSettings],
            error_mapper=get_terminals_terminal_id_terminal_settings_error_mapper,
            request_options=request_options,
        )

    async def patch_terminals_terminal_id_terminal_logos(
        self,
        terminal_id: str,
        *,
        body: Logo | LogoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Logo, PatchTerminalsTerminalIdTerminalLogosErrorBody]:
        """Updates the logo for the payment terminal identified in the path.

        * To change the logo, specify the image file as a Base64-encoded string.
        * To restore the logo inherited from a higher level (store, merchant account, or company account), specify an
            empty logo value.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            terminal_id: The unique identifier of the payment terminal.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/terminals/{terminalId}/terminalLogos"),
            path_params=[param[str]("terminalId", terminal_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Logo | LogoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[Logo],
            error_mapper=patch_terminals_terminal_id_terminal_logos_error_mapper,
            request_options=request_options,
        )

    async def patch_terminals_terminal_id_terminal_settings(
        self,
        terminal_id: str,
        *,
        body: TerminalSettings | TerminalSettingsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalSettings, PatchTerminalsTerminalIdTerminalSettingsErrorBody]:
        """Updates the settings that are configured for the payment terminal identified in the path.

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
            terminal_id: The unique identifier of the payment terminal.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/terminals/{terminalId}/terminalSettings"),
            path_params=[param[str]("terminalId", terminal_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TerminalSettings | TerminalSettingsDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[TerminalSettings],
            error_mapper=patch_terminals_terminal_id_terminal_settings_error_mapper,
            request_options=request_options,
        )
