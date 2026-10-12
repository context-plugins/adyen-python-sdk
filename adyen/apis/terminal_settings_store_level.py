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
from ..errors.get_merchants_merchant_id_stores_reference_terminal_logos_error import (
    GetMerchantsMerchantIdStoresReferenceTerminalLogosErrorBody,
    get_merchants_merchant_id_stores_reference_terminal_logos_error_mapper,
)
from ..errors.get_merchants_merchant_id_stores_reference_terminal_settings_error import (
    GetMerchantsMerchantIdStoresReferenceTerminalSettingsErrorBody,
    get_merchants_merchant_id_stores_reference_terminal_settings_error_mapper,
)
from ..errors.get_stores_store_id_terminal_logos_error import (
    GetStoresStoreIdTerminalLogosErrorBody,
    get_stores_store_id_terminal_logos_error_mapper,
)
from ..errors.get_stores_store_id_terminal_settings_error import (
    GetStoresStoreIdTerminalSettingsErrorBody,
    get_stores_store_id_terminal_settings_error_mapper,
)
from ..errors.patch_merchants_merchant_id_stores_reference_terminal_logos_error import (
    PatchMerchantsMerchantIdStoresReferenceTerminalLogosErrorBody,
    patch_merchants_merchant_id_stores_reference_terminal_logos_error_mapper,
)
from ..errors.patch_merchants_merchant_id_stores_reference_terminal_settings_error import (
    PatchMerchantsMerchantIdStoresReferenceTerminalSettingsErrorBody,
    patch_merchants_merchant_id_stores_reference_terminal_settings_error_mapper,
)
from ..errors.patch_stores_store_id_terminal_logos_error import (
    PatchStoresStoreIdTerminalLogosErrorBody,
    patch_stores_store_id_terminal_logos_error_mapper,
)
from ..errors.patch_stores_store_id_terminal_settings_error import (
    PatchStoresStoreIdTerminalSettingsErrorBody,
    patch_stores_store_id_terminal_settings_error_mapper,
)
from ..models.logo import Logo, LogoDict
from ..models.terminal_settings import TerminalSettings, TerminalSettingsDict
from ..server.server import Server


class TerminalSettingsStoreLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TerminalSettingsStoreLevelWithRawResponse(client, server, auth)

    def get_merchants_merchant_id_stores_reference_terminal_logos(
        self, merchant_id: str, reference: str, model: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Logo:
        """Returns the logo that is configured for a specific payment terminal model at the store identified in the
        path. The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual
        image file. This logo applies to all terminals of the specified model under the store, unless a different logo
        is configured for an individual terminal.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            reference: The reference that identifies the store.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
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
            self._with_raw_response.get_merchants_merchant_id_stores_reference_terminal_logos(
                merchant_id, reference, model, request_options=request_options
            ),
        )

    def get_merchants_merchant_id_stores_reference_terminal_settings(
        self, merchant_id: str, reference: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TerminalSettings:
        """Returns the payment terminal settings that are configured for the store identified in the path. These
        settings apply to all terminals under the store unless different values are configured for an individual
        terminal.

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
            reference: The reference that identifies the store.
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
            self._with_raw_response.get_merchants_merchant_id_stores_reference_terminal_settings(
                merchant_id, reference, request_options=request_options
            ),
        )

    def get_stores_store_id_terminal_logos(
        self, store_id: str, model: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Logo:
        """Returns the logo that is configured for a specific payment terminal model at the store identified in the
        path. The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual
        image file. This logo applies to all terminals of that model under the store unless a different logo is
        configured for an individual terminal.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            store_id: The unique identifier of the store.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
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
            self._with_raw_response.get_stores_store_id_terminal_logos(store_id, model, request_options=request_options)
        )

    def get_stores_store_id_terminal_settings(
        self, store_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TerminalSettings:
        """Returns the payment terminal settings that are configured for the store identified in the path. These
        settings apply to all terminals under the store unless different values are configured for an individual
        terminal.

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
            store_id: The unique identifier of the store.
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
            self._with_raw_response.get_stores_store_id_terminal_settings(store_id, request_options=request_options)
        )

    def patch_merchants_merchant_id_stores_reference_terminal_logos(
        self,
        merchant_id: str,
        reference: str,
        model: str,
        *,
        body: Logo | LogoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Logo:
        """Updates the logo that is configured for a specific payment terminal model at the store identified in the
        path. You can update the logo for only one terminal model at a time. This logo applies to all terminals of the
        specified model under the store, unless a different logo is configured for an individual terminal.

        * To change the logo, specify the image file as a Base64-encoded string.
        * To restore the logo inherited from a higher level (merchant or company account), specify an empty logo value.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            reference: The reference that identifies the store.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T
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
            self._with_raw_response.patch_merchants_merchant_id_stores_reference_terminal_logos(
                merchant_id, reference, model, body=body, request_options=request_options
            ),
        )

    def patch_merchants_merchant_id_stores_reference_terminal_settings(
        self,
        merchant_id: str,
        reference: str,
        *,
        body: TerminalSettings | TerminalSettingsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalSettings:
        """Updates payment terminal settings for the store identified in the path. These settings apply to all terminals
        under the store, unless different values are configured for an individual terminal.

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
            reference: The reference that identifies the store.
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
            self._with_raw_response.patch_merchants_merchant_id_stores_reference_terminal_settings(
                merchant_id, reference, body=body, request_options=request_options
            ),
        )

    def patch_stores_store_id_terminal_logos(
        self,
        store_id: str,
        model: str,
        *,
        body: Logo | LogoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Logo:
        """Updates the logo that is configured for a specific payment terminal model at the store identified in the
        path. You can update the logo for only one terminal model at a time. This logo applies to all terminals of the
        specified model under the store, unless a different logo is configured for an individual terminal.

        * To change the logo, specify the image file as a Base64-encoded string.
        * To restore the logo inherited from a higher level (merchant or company account), specify an empty logo value.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            store_id: The unique identifier of the store.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
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
            self._with_raw_response.patch_stores_store_id_terminal_logos(
                store_id, model, body=body, request_options=request_options
            ),
        )

    def patch_stores_store_id_terminal_settings(
        self,
        store_id: str,
        *,
        body: TerminalSettings | TerminalSettingsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalSettings:
        """Updates payment terminal settings for the store identified in the path. These settings apply to all terminals
        under the store, unless different values are configured for an individual terminal.

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
            store_id: The unique identifier of the store.
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
            self._with_raw_response.patch_stores_store_id_terminal_settings(
                store_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> TerminalSettingsStoreLevelWithRawResponse:
        return self._with_raw_response


class AsyncTerminalSettingsStoreLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTerminalSettingsStoreLevelWithRawResponse(client, server, auth)

    async def get_merchants_merchant_id_stores_reference_terminal_logos(
        self, merchant_id: str, reference: str, model: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Logo:
        """Returns the logo that is configured for a specific payment terminal model at the store identified in the
        path. The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual
        image file. This logo applies to all terminals of the specified model under the store, unless a different logo
        is configured for an individual terminal.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            reference: The reference that identifies the store.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
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
            await self._with_raw_response.get_merchants_merchant_id_stores_reference_terminal_logos(
                merchant_id, reference, model, request_options=request_options
            ),
        )

    async def get_merchants_merchant_id_stores_reference_terminal_settings(
        self, merchant_id: str, reference: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TerminalSettings:
        """Returns the payment terminal settings that are configured for the store identified in the path. These
        settings apply to all terminals under the store unless different values are configured for an individual
        terminal.

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
            reference: The reference that identifies the store.
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
            await self._with_raw_response.get_merchants_merchant_id_stores_reference_terminal_settings(
                merchant_id, reference, request_options=request_options
            ),
        )

    async def get_stores_store_id_terminal_logos(
        self, store_id: str, model: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Logo:
        """Returns the logo that is configured for a specific payment terminal model at the store identified in the
        path. The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual
        image file. This logo applies to all terminals of that model under the store unless a different logo is
        configured for an individual terminal.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            store_id: The unique identifier of the store.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
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
            await self._with_raw_response.get_stores_store_id_terminal_logos(
                store_id, model, request_options=request_options
            ),
        )

    async def get_stores_store_id_terminal_settings(
        self, store_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TerminalSettings:
        """Returns the payment terminal settings that are configured for the store identified in the path. These
        settings apply to all terminals under the store unless different values are configured for an individual
        terminal.

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
            store_id: The unique identifier of the store.
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
            await self._with_raw_response.get_stores_store_id_terminal_settings(
                store_id, request_options=request_options
            ),
        )

    async def patch_merchants_merchant_id_stores_reference_terminal_logos(
        self,
        merchant_id: str,
        reference: str,
        model: str,
        *,
        body: Logo | LogoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Logo:
        """Updates the logo that is configured for a specific payment terminal model at the store identified in the
        path. You can update the logo for only one terminal model at a time. This logo applies to all terminals of the
        specified model under the store, unless a different logo is configured for an individual terminal.

        * To change the logo, specify the image file as a Base64-encoded string.
        * To restore the logo inherited from a higher level (merchant or company account), specify an empty logo value.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            reference: The reference that identifies the store.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T
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
            await self._with_raw_response.patch_merchants_merchant_id_stores_reference_terminal_logos(
                merchant_id, reference, model, body=body, request_options=request_options
            ),
        )

    async def patch_merchants_merchant_id_stores_reference_terminal_settings(
        self,
        merchant_id: str,
        reference: str,
        *,
        body: TerminalSettings | TerminalSettingsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalSettings:
        """Updates payment terminal settings for the store identified in the path. These settings apply to all terminals
        under the store, unless different values are configured for an individual terminal.

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
            reference: The reference that identifies the store.
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
            await self._with_raw_response.patch_merchants_merchant_id_stores_reference_terminal_settings(
                merchant_id, reference, body=body, request_options=request_options
            ),
        )

    async def patch_stores_store_id_terminal_logos(
        self,
        store_id: str,
        model: str,
        *,
        body: Logo | LogoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Logo:
        """Updates the logo that is configured for a specific payment terminal model at the store identified in the
        path. You can update the logo for only one terminal model at a time. This logo applies to all terminals of the
        specified model under the store, unless a different logo is configured for an individual terminal.

        * To change the logo, specify the image file as a Base64-encoded string.
        * To restore the logo inherited from a higher level (merchant or company account), specify an empty logo value.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            store_id: The unique identifier of the store.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
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
            await self._with_raw_response.patch_stores_store_id_terminal_logos(
                store_id, model, body=body, request_options=request_options
            ),
        )

    async def patch_stores_store_id_terminal_settings(
        self,
        store_id: str,
        *,
        body: TerminalSettings | TerminalSettingsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TerminalSettings:
        """Updates payment terminal settings for the store identified in the path. These settings apply to all terminals
        under the store, unless different values are configured for an individual terminal.

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
            store_id: The unique identifier of the store.
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
            await self._with_raw_response.patch_stores_store_id_terminal_settings(
                store_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncTerminalSettingsStoreLevelWithRawResponse:
        return self._with_raw_response


class TerminalSettingsStoreLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_merchants_merchant_id_stores_reference_terminal_logos(
        self, merchant_id: str, reference: str, model: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Logo, GetMerchantsMerchantIdStoresReferenceTerminalLogosErrorBody]:
        """Returns the logo that is configured for a specific payment terminal model at the store identified in the
        path. The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual
        image file. This logo applies to all terminals of the specified model under the store, unless a different logo
        is configured for an individual terminal.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            reference: The reference that identifies the store.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/stores/{reference}/terminalLogos"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("reference", reference)],
            query_params=[param[str]("model", model)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Logo],
            error_mapper=get_merchants_merchant_id_stores_reference_terminal_logos_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_stores_reference_terminal_settings(
        self, merchant_id: str, reference: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalSettings, GetMerchantsMerchantIdStoresReferenceTerminalSettingsErrorBody]:
        """Returns the payment terminal settings that are configured for the store identified in the path. These
        settings apply to all terminals under the store unless different values are configured for an individual
        terminal.

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
            reference: The reference that identifies the store.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/stores/{reference}/terminalSettings"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("reference", reference)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalSettings],
            error_mapper=get_merchants_merchant_id_stores_reference_terminal_settings_error_mapper,
            request_options=request_options,
        )

    def get_stores_store_id_terminal_logos(
        self, store_id: str, model: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Logo, GetStoresStoreIdTerminalLogosErrorBody]:
        """Returns the logo that is configured for a specific payment terminal model at the store identified in the
        path. The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual
        image file. This logo applies to all terminals of that model under the store unless a different logo is
        configured for an individual terminal.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            store_id: The unique identifier of the store.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/stores/{storeId}/terminalLogos"),
            path_params=[param[str]("storeId", store_id)],
            query_params=[param[str]("model", model)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Logo],
            error_mapper=get_stores_store_id_terminal_logos_error_mapper,
            request_options=request_options,
        )

    def get_stores_store_id_terminal_settings(
        self, store_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalSettings, GetStoresStoreIdTerminalSettingsErrorBody]:
        """Returns the payment terminal settings that are configured for the store identified in the path. These
        settings apply to all terminals under the store unless different values are configured for an individual
        terminal.

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
            store_id: The unique identifier of the store.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/stores/{storeId}/terminalSettings"),
            path_params=[param[str]("storeId", store_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalSettings],
            error_mapper=get_stores_store_id_terminal_settings_error_mapper,
            request_options=request_options,
        )

    def patch_merchants_merchant_id_stores_reference_terminal_logos(
        self,
        merchant_id: str,
        reference: str,
        model: str,
        *,
        body: Logo | LogoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Logo, PatchMerchantsMerchantIdStoresReferenceTerminalLogosErrorBody]:
        """Updates the logo that is configured for a specific payment terminal model at the store identified in the
        path. You can update the logo for only one terminal model at a time. This logo applies to all terminals of the
        specified model under the store, unless a different logo is configured for an individual terminal.

        * To change the logo, specify the image file as a Base64-encoded string.
        * To restore the logo inherited from a higher level (merchant or company account), specify an empty logo value.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            reference: The reference that identifies the store.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/stores/{reference}/terminalLogos"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("reference", reference)],
            query_params=[param[str]("model", model)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Logo | LogoDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Logo],
            error_mapper=patch_merchants_merchant_id_stores_reference_terminal_logos_error_mapper,
            request_options=request_options,
        )

    def patch_merchants_merchant_id_stores_reference_terminal_settings(
        self,
        merchant_id: str,
        reference: str,
        *,
        body: TerminalSettings | TerminalSettingsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalSettings, PatchMerchantsMerchantIdStoresReferenceTerminalSettingsErrorBody]:
        """Updates payment terminal settings for the store identified in the path. These settings apply to all terminals
        under the store, unless different values are configured for an individual terminal.

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
            reference: The reference that identifies the store.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/stores/{reference}/terminalSettings"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("reference", reference)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TerminalSettings | TerminalSettingsDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalSettings],
            error_mapper=patch_merchants_merchant_id_stores_reference_terminal_settings_error_mapper,
            request_options=request_options,
        )

    def patch_stores_store_id_terminal_logos(
        self,
        store_id: str,
        model: str,
        *,
        body: Logo | LogoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Logo, PatchStoresStoreIdTerminalLogosErrorBody]:
        """Updates the logo that is configured for a specific payment terminal model at the store identified in the
        path. You can update the logo for only one terminal model at a time. This logo applies to all terminals of the
        specified model under the store, unless a different logo is configured for an individual terminal.

        * To change the logo, specify the image file as a Base64-encoded string.
        * To restore the logo inherited from a higher level (merchant or company account), specify an empty logo value.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            store_id: The unique identifier of the store.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/stores/{storeId}/terminalLogos"),
            path_params=[param[str]("storeId", store_id)],
            query_params=[param[str]("model", model)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Logo | LogoDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Logo],
            error_mapper=patch_stores_store_id_terminal_logos_error_mapper,
            request_options=request_options,
        )

    def patch_stores_store_id_terminal_settings(
        self,
        store_id: str,
        *,
        body: TerminalSettings | TerminalSettingsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalSettings, PatchStoresStoreIdTerminalSettingsErrorBody]:
        """Updates payment terminal settings for the store identified in the path. These settings apply to all terminals
        under the store, unless different values are configured for an individual terminal.

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
            store_id: The unique identifier of the store.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/stores/{storeId}/terminalSettings"),
            path_params=[param[str]("storeId", store_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TerminalSettings | TerminalSettingsDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TerminalSettings],
            error_mapper=patch_stores_store_id_terminal_settings_error_mapper,
            request_options=request_options,
        )


class AsyncTerminalSettingsStoreLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_merchants_merchant_id_stores_reference_terminal_logos(
        self, merchant_id: str, reference: str, model: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Logo, GetMerchantsMerchantIdStoresReferenceTerminalLogosErrorBody]:
        """Returns the logo that is configured for a specific payment terminal model at the store identified in the
        path. The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual
        image file. This logo applies to all terminals of the specified model under the store, unless a different logo
        is configured for an individual terminal.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            reference: The reference that identifies the store.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/stores/{reference}/terminalLogos"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("reference", reference)],
            query_params=[param[str]("model", model)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[Logo],
            error_mapper=get_merchants_merchant_id_stores_reference_terminal_logos_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_stores_reference_terminal_settings(
        self, merchant_id: str, reference: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalSettings, GetMerchantsMerchantIdStoresReferenceTerminalSettingsErrorBody]:
        """Returns the payment terminal settings that are configured for the store identified in the path. These
        settings apply to all terminals under the store unless different values are configured for an individual
        terminal.

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
            reference: The reference that identifies the store.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/stores/{reference}/terminalSettings"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("reference", reference)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[TerminalSettings],
            error_mapper=get_merchants_merchant_id_stores_reference_terminal_settings_error_mapper,
            request_options=request_options,
        )

    async def get_stores_store_id_terminal_logos(
        self, store_id: str, model: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Logo, GetStoresStoreIdTerminalLogosErrorBody]:
        """Returns the logo that is configured for a specific payment terminal model at the store identified in the
        path. The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual
        image file. This logo applies to all terminals of that model under the store unless a different logo is
        configured for an individual terminal.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            store_id: The unique identifier of the store.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/stores/{storeId}/terminalLogos"),
            path_params=[param[str]("storeId", store_id)],
            query_params=[param[str]("model", model)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[Logo],
            error_mapper=get_stores_store_id_terminal_logos_error_mapper,
            request_options=request_options,
        )

    async def get_stores_store_id_terminal_settings(
        self, store_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TerminalSettings, GetStoresStoreIdTerminalSettingsErrorBody]:
        """Returns the payment terminal settings that are configured for the store identified in the path. These
        settings apply to all terminals under the store unless different values are configured for an individual
        terminal.

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
            store_id: The unique identifier of the store.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/stores/{storeId}/terminalSettings"),
            path_params=[param[str]("storeId", store_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[TerminalSettings],
            error_mapper=get_stores_store_id_terminal_settings_error_mapper,
            request_options=request_options,
        )

    async def patch_merchants_merchant_id_stores_reference_terminal_logos(
        self,
        merchant_id: str,
        reference: str,
        model: str,
        *,
        body: Logo | LogoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Logo, PatchMerchantsMerchantIdStoresReferenceTerminalLogosErrorBody]:
        """Updates the logo that is configured for a specific payment terminal model at the store identified in the
        path. You can update the logo for only one terminal model at a time. This logo applies to all terminals of the
        specified model under the store, unless a different logo is configured for an individual terminal.

        * To change the logo, specify the image file as a Base64-encoded string.
        * To restore the logo inherited from a higher level (merchant or company account), specify an empty logo value.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            merchant_id: The unique identifier of the merchant account.
            reference: The reference that identifies the store.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/stores/{reference}/terminalLogos"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("reference", reference)],
            query_params=[param[str]("model", model)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Logo | LogoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[Logo],
            error_mapper=patch_merchants_merchant_id_stores_reference_terminal_logos_error_mapper,
            request_options=request_options,
        )

    async def patch_merchants_merchant_id_stores_reference_terminal_settings(
        self,
        merchant_id: str,
        reference: str,
        *,
        body: TerminalSettings | TerminalSettingsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalSettings, PatchMerchantsMerchantIdStoresReferenceTerminalSettingsErrorBody]:
        """Updates payment terminal settings for the store identified in the path. These settings apply to all terminals
        under the store, unless different values are configured for an individual terminal.

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
            reference: The reference that identifies the store.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/stores/{reference}/terminalSettings"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("reference", reference)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TerminalSettings | TerminalSettingsDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[TerminalSettings],
            error_mapper=patch_merchants_merchant_id_stores_reference_terminal_settings_error_mapper,
            request_options=request_options,
        )

    async def patch_stores_store_id_terminal_logos(
        self,
        store_id: str,
        model: str,
        *,
        body: Logo | LogoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Logo, PatchStoresStoreIdTerminalLogosErrorBody]:
        """Updates the logo that is configured for a specific payment terminal model at the store identified in the
        path. You can update the logo for only one terminal model at a time. This logo applies to all terminals of the
        specified model under the store, unless a different logo is configured for an individual terminal.

        * To change the logo, specify the image file as a Base64-encoded string.
        * To restore the logo inherited from a higher level (merchant or company account), specify an empty logo value.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal settings read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            store_id: The unique identifier of the store.
            model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925,
                P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L,
                S1U, S7T.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/stores/{storeId}/terminalLogos"),
            path_params=[param[str]("storeId", store_id)],
            query_params=[param[str]("model", model)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Logo | LogoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[Logo],
            error_mapper=patch_stores_store_id_terminal_logos_error_mapper,
            request_options=request_options,
        )

    async def patch_stores_store_id_terminal_settings(
        self,
        store_id: str,
        *,
        body: TerminalSettings | TerminalSettingsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TerminalSettings, PatchStoresStoreIdTerminalSettingsErrorBody]:
        """Updates payment terminal settings for the store identified in the path. These settings apply to all terminals
        under the store, unless different values are configured for an individual terminal.

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
            store_id: The unique identifier of the store.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/stores/{storeId}/terminalSettings"),
            path_params=[param[str]("storeId", store_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TerminalSettings | TerminalSettingsDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[TerminalSettings],
            error_mapper=patch_stores_store_id_terminal_settings_error_mapper,
            request_options=request_options,
        )
