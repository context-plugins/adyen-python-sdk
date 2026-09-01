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
from ..errors.delete_merchants_merchant_id_split_configurations_split_configuration_id_error import (
    DeleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody,
    delete_merchants_merchant_id_split_configurations_split_configuration_id_error_mapper,
)
from ..errors.delete_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id_error import (
    DeleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdErrorBody,
    delete_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id_error_mapper,
)
from ..errors.get_merchants_merchant_id_split_configurations_error import (
    GetMerchantsMerchantIdSplitConfigurationsErrorBody,
    get_merchants_merchant_id_split_configurations_error_mapper,
)
from ..errors.get_merchants_merchant_id_split_configurations_split_configuration_id_error import (
    GetMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody,
    get_merchants_merchant_id_split_configurations_split_configuration_id_error_mapper,
)
from ..errors.patch_merchants_merchant_id_split_configurations_split_configuration_id_error import (
    PatchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody,
    patch_merchants_merchant_id_split_configurations_split_configuration_id_error_mapper,
)
from ..errors.patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id_error import (
    PatchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdErrorBody,
    patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id_error_mapper,
)
from ..errors.patch_merchants_split_configurations_rules_split_logic_error import (
    PatchMerchantsSplitConfigurationsRulesSplitLogicErrorBody,
    patch_merchants_split_configurations_rules_split_logic_error_mapper,
)
from ..errors.post_merchants_merchant_id_split_configurations_error import (
    PostMerchantsMerchantIdSplitConfigurationsErrorBody,
    post_merchants_merchant_id_split_configurations_error_mapper,
)
from ..errors.post_merchants_merchant_id_split_configurations_split_configuration_id_error import (
    PostMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody,
    post_merchants_merchant_id_split_configurations_split_configuration_id_error_mapper,
)
from ..models.split_configuration import SplitConfiguration, SplitConfigurationDict
from ..models.split_configuration_list import SplitConfigurationList
from ..models.split_configuration_rule import SplitConfigurationRule, SplitConfigurationRuleDict
from ..models.update_split_configuration_logic_request import (
    UpdateSplitConfigurationLogicRequest,
    UpdateSplitConfigurationLogicRequestDict,
)
from ..models.update_split_configuration_request import (
    UpdateSplitConfigurationRequest,
    UpdateSplitConfigurationRequestDict,
)
from ..models.update_split_configuration_rule_request import (
    UpdateSplitConfigurationRuleRequest,
    UpdateSplitConfigurationRuleRequestDict,
)
from ..server.server import Server


class SplitConfigurationMerchantLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SplitConfigurationMerchantLevelWithRawResponse(client, server, auth)

    def delete_merchants_merchant_id_split_configurations_split_configuration_id(
        self, merchant_id: str, split_configuration_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SplitConfiguration:
        """Deletes the split configuration profile specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.delete_merchants_merchant_id_split_configurations_split_configuration_id(
            merchant_id, split_configuration_id, request_options=request_options
        ).unwrap()

    def delete_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id(
        self,
        merchant_id: str,
        split_configuration_id: str,
        rule_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SplitConfiguration:
        """Deletes the rule specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            rule_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.delete_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id(
            merchant_id, split_configuration_id, rule_id, request_options=request_options
        ).unwrap()

    def get_merchants_merchant_id_split_configurations(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SplitConfigurationList:
        """Returns the list of split configuration profiles for the merchant account.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

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
        return self._with_raw_response.get_merchants_merchant_id_split_configurations(
            merchant_id, request_options=request_options
        ).unwrap()

    def get_merchants_merchant_id_split_configurations_split_configuration_id(
        self, merchant_id: str, split_configuration_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SplitConfiguration:
        """Returns the details of the split configuration profile specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_split_configurations_split_configuration_id(
            merchant_id, split_configuration_id, request_options=request_options
        ).unwrap()

    def patch_merchants_merchant_id_split_configurations_split_configuration_id(
        self,
        merchant_id: str,
        split_configuration_id: str,
        *,
        body: UpdateSplitConfigurationRequest | UpdateSplitConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SplitConfiguration:
        """Changes the description of the split configuration profile specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_merchants_merchant_id_split_configurations_split_configuration_id(
            merchant_id, split_configuration_id, body=body, request_options=request_options
        ).unwrap()

    def patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id(
        self,
        merchant_id: str,
        split_configuration_id: str,
        rule_id: str,
        *,
        body: UpdateSplitConfigurationRuleRequest | UpdateSplitConfigurationRuleRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SplitConfiguration:
        """Changes the `split conditions of the rule
        <https://docs.adyen.com/platforms/automatic-split-configuration/manage-split-configurations/api/#update-condition>`__
        specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The identifier of the split configuration.
            rule_id: The unique identifier of the split configuration rule.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id(
            merchant_id, split_configuration_id, rule_id, body=body, request_options=request_options
        ).unwrap()

    def patch_merchants_split_configurations_rules_split_logic(
        self,
        merchant_id: str,
        split_configuration_id: str,
        rule_id: str,
        split_logic_id: str,
        *,
        body: UpdateSplitConfigurationLogicRequest | UpdateSplitConfigurationLogicRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SplitConfiguration:
        """Changes the `split logic
        <https://docs.adyen.com/platforms/automatic-split-configuration/manage-split-configurations/api/#update-split-logic>`__
        specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            rule_id: The unique identifier of the split configuration rule.
            split_logic_id: The unique identifier of the split configuration split.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_merchants_split_configurations_rules_split_logic(
            merchant_id, split_configuration_id, rule_id, split_logic_id, body=body, request_options=request_options
        ).unwrap()

    def post_merchants_merchant_id_split_configurations(
        self,
        merchant_id: str,
        *,
        body: SplitConfiguration | SplitConfigurationDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SplitConfiguration:
        """Creates a split configuration profile to `split payments automatically
        <https://docs.adyen.com/platforms/automatic-split-configuration/>`__. After you `associate it with a store
        <https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId>`__/stores/(storeId)#request-splitConfiguration)
        in your merchant account, it splits the funds of all transactions processed through that store between your
        liable balance account and `your user's balance account
        <https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId>`__/stores/(storeId)#request-splitConfiguration-balanceAccountId).

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

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
        return self._with_raw_response.post_merchants_merchant_id_split_configurations(
            merchant_id, body=body, request_options=request_options
        ).unwrap()

    def post_merchants_merchant_id_split_configurations_split_configuration_id(
        self,
        merchant_id: str,
        split_configuration_id: str,
        *,
        body: SplitConfigurationRule | SplitConfigurationRuleDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SplitConfiguration:
        """`Creates a rule
        <https://docs.adyen.com/platforms/automatic-split-configuration/manage-split-configurations/api/#create-rule>`__
        in the split configuration profile specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_merchants_merchant_id_split_configurations_split_configuration_id(
            merchant_id, split_configuration_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SplitConfigurationMerchantLevelWithRawResponse:
        return self._with_raw_response


class AsyncSplitConfigurationMerchantLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSplitConfigurationMerchantLevelWithRawResponse(client, server, auth)

    async def delete_merchants_merchant_id_split_configurations_split_configuration_id(
        self, merchant_id: str, split_configuration_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SplitConfiguration:
        """Deletes the split configuration profile specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.delete_merchants_merchant_id_split_configurations_split_configuration_id(
                merchant_id, split_configuration_id, request_options=request_options
            )
        ).unwrap()

    async def delete_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id(
        self,
        merchant_id: str,
        split_configuration_id: str,
        rule_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SplitConfiguration:
        """Deletes the rule specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            rule_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.delete_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id(
                merchant_id, split_configuration_id, rule_id, request_options=request_options
            )
        ).unwrap()

    async def get_merchants_merchant_id_split_configurations(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SplitConfigurationList:
        """Returns the list of split configuration profiles for the merchant account.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

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
            await self._with_raw_response.get_merchants_merchant_id_split_configurations(
                merchant_id, request_options=request_options
            )
        ).unwrap()

    async def get_merchants_merchant_id_split_configurations_split_configuration_id(
        self, merchant_id: str, split_configuration_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SplitConfiguration:
        """Returns the details of the split configuration profile specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_merchants_merchant_id_split_configurations_split_configuration_id(
                merchant_id, split_configuration_id, request_options=request_options
            )
        ).unwrap()

    async def patch_merchants_merchant_id_split_configurations_split_configuration_id(
        self,
        merchant_id: str,
        split_configuration_id: str,
        *,
        body: UpdateSplitConfigurationRequest | UpdateSplitConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SplitConfiguration:
        """Changes the description of the split configuration profile specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
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
            await self._with_raw_response.patch_merchants_merchant_id_split_configurations_split_configuration_id(
                merchant_id, split_configuration_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id(
        self,
        merchant_id: str,
        split_configuration_id: str,
        rule_id: str,
        *,
        body: UpdateSplitConfigurationRuleRequest | UpdateSplitConfigurationRuleRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SplitConfiguration:
        """Changes the `split conditions of the rule
        <https://docs.adyen.com/platforms/automatic-split-configuration/manage-split-configurations/api/#update-condition>`__
        specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The identifier of the split configuration.
            rule_id: The unique identifier of the split configuration rule.
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
            await self._with_raw_response.patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id(
                merchant_id, split_configuration_id, rule_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def patch_merchants_split_configurations_rules_split_logic(
        self,
        merchant_id: str,
        split_configuration_id: str,
        rule_id: str,
        split_logic_id: str,
        *,
        body: UpdateSplitConfigurationLogicRequest | UpdateSplitConfigurationLogicRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SplitConfiguration:
        """Changes the `split logic
        <https://docs.adyen.com/platforms/automatic-split-configuration/manage-split-configurations/api/#update-split-logic>`__
        specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            rule_id: The unique identifier of the split configuration rule.
            split_logic_id: The unique identifier of the split configuration split.
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
            await self._with_raw_response.patch_merchants_split_configurations_rules_split_logic(
                merchant_id, split_configuration_id, rule_id, split_logic_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_merchants_merchant_id_split_configurations(
        self,
        merchant_id: str,
        *,
        body: SplitConfiguration | SplitConfigurationDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SplitConfiguration:
        """Creates a split configuration profile to `split payments automatically
        <https://docs.adyen.com/platforms/automatic-split-configuration/>`__. After you `associate it with a store
        <https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId>`__/stores/(storeId)#request-splitConfiguration)
        in your merchant account, it splits the funds of all transactions processed through that store between your
        liable balance account and `your user's balance account
        <https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId>`__/stores/(storeId)#request-splitConfiguration-balanceAccountId).

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

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
            await self._with_raw_response.post_merchants_merchant_id_split_configurations(
                merchant_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_merchants_merchant_id_split_configurations_split_configuration_id(
        self,
        merchant_id: str,
        split_configuration_id: str,
        *,
        body: SplitConfigurationRule | SplitConfigurationRuleDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SplitConfiguration:
        """`Creates a rule
        <https://docs.adyen.com/platforms/automatic-split-configuration/manage-split-configurations/api/#create-rule>`__
        in the split configuration profile specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
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
            await self._with_raw_response.post_merchants_merchant_id_split_configurations_split_configuration_id(
                merchant_id, split_configuration_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSplitConfigurationMerchantLevelWithRawResponse:
        return self._with_raw_response


class SplitConfigurationMerchantLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_merchants_merchant_id_split_configurations_split_configuration_id(
        self, merchant_id: str, split_configuration_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SplitConfiguration, DeleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody]:
        """Deletes the split configuration profile specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/merchants/{merchantId}/splitConfigurations/{splitConfigurationId}"),
            path_params=[
                param[str]("merchantId", merchant_id), param[str]("splitConfigurationId", split_configuration_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SplitConfiguration],
            error_mapper=delete_merchants_merchant_id_split_configurations_split_configuration_id_error_mapper,
            request_options=request_options,
        )

    def delete_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id(
        self,
        merchant_id: str,
        split_configuration_id: str,
        rule_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SplitConfiguration, DeleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdErrorBody
    ]:
        """Deletes the rule specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            rule_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9(
                "/merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId}"
            ),
            path_params=[
                param[str]("merchantId", merchant_id),
                param[str]("splitConfigurationId", split_configuration_id),
                param[str]("ruleId", rule_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SplitConfiguration],
            error_mapper=delete_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_split_configurations(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SplitConfigurationList, GetMerchantsMerchantIdSplitConfigurationsErrorBody]:
        """Returns the list of split configuration profiles for the merchant account.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/splitConfigurations"),
            path_params=[param[str]("merchantId", merchant_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SplitConfigurationList],
            error_mapper=get_merchants_merchant_id_split_configurations_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_split_configurations_split_configuration_id(
        self, merchant_id: str, split_configuration_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SplitConfiguration, GetMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody]:
        """Returns the details of the split configuration profile specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/splitConfigurations/{splitConfigurationId}"),
            path_params=[
                param[str]("merchantId", merchant_id), param[str]("splitConfigurationId", split_configuration_id)
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SplitConfiguration],
            error_mapper=get_merchants_merchant_id_split_configurations_split_configuration_id_error_mapper,
            request_options=request_options,
        )

    def patch_merchants_merchant_id_split_configurations_split_configuration_id(
        self,
        merchant_id: str,
        split_configuration_id: str,
        *,
        body: UpdateSplitConfigurationRequest | UpdateSplitConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SplitConfiguration, PatchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody]:
        """Changes the description of the split configuration profile specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/splitConfigurations/{splitConfigurationId}"),
            path_params=[
                param[str]("merchantId", merchant_id), param[str]("splitConfigurationId", split_configuration_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSplitConfigurationRequest | UpdateSplitConfigurationRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SplitConfiguration],
            error_mapper=patch_merchants_merchant_id_split_configurations_split_configuration_id_error_mapper,
            request_options=request_options,
        )

    def patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id(
        self,
        merchant_id: str,
        split_configuration_id: str,
        rule_id: str,
        *,
        body: UpdateSplitConfigurationRuleRequest | UpdateSplitConfigurationRuleRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SplitConfiguration, PatchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdErrorBody
    ]:
        """Changes the `split conditions of the rule
        <https://docs.adyen.com/platforms/automatic-split-configuration/manage-split-configurations/api/#update-condition>`__
        specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The identifier of the split configuration.
            rule_id: The unique identifier of the split configuration rule.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9(
                "/merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId}"
            ),
            path_params=[
                param[str]("merchantId", merchant_id),
                param[str]("splitConfigurationId", split_configuration_id),
                param[str]("ruleId", rule_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSplitConfigurationRuleRequest | UpdateSplitConfigurationRuleRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SplitConfiguration],
            error_mapper=patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id_error_mapper,
            request_options=request_options,
        )

    def patch_merchants_split_configurations_rules_split_logic(
        self,
        merchant_id: str,
        split_configuration_id: str,
        rule_id: str,
        split_logic_id: str,
        *,
        body: UpdateSplitConfigurationLogicRequest | UpdateSplitConfigurationLogicRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SplitConfiguration, PatchMerchantsSplitConfigurationsRulesSplitLogicErrorBody]:
        """Changes the `split logic
        <https://docs.adyen.com/platforms/automatic-split-configuration/manage-split-configurations/api/#update-split-logic>`__
        specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            rule_id: The unique identifier of the split configuration rule.
            split_logic_id: The unique identifier of the split configuration split.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9(
                "/merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId}/splitLogic/{splitLogicId}",
            ),
            path_params=[
                param[str]("merchantId", merchant_id),
                param[str]("splitConfigurationId", split_configuration_id),
                param[str]("ruleId", rule_id),
                param[str]("splitLogicId", split_logic_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSplitConfigurationLogicRequest | UpdateSplitConfigurationLogicRequestDict | None](
                body
            ),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SplitConfiguration],
            error_mapper=patch_merchants_split_configurations_rules_split_logic_error_mapper,
            request_options=request_options,
        )

    def post_merchants_merchant_id_split_configurations(
        self,
        merchant_id: str,
        *,
        body: SplitConfiguration | SplitConfigurationDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SplitConfiguration, PostMerchantsMerchantIdSplitConfigurationsErrorBody]:
        """Creates a split configuration profile to `split payments automatically
        <https://docs.adyen.com/platforms/automatic-split-configuration/>`__. After you `associate it with a store
        <https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId>`__/stores/(storeId)#request-splitConfiguration)
        in your merchant account, it splits the funds of all transactions processed through that store between your
        liable balance account and `your user's balance account
        <https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId>`__/stores/(storeId)#request-splitConfiguration-balanceAccountId).

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/splitConfigurations"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SplitConfiguration | SplitConfigurationDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SplitConfiguration],
            error_mapper=post_merchants_merchant_id_split_configurations_error_mapper,
            request_options=request_options,
        )

    def post_merchants_merchant_id_split_configurations_split_configuration_id(
        self,
        merchant_id: str,
        split_configuration_id: str,
        *,
        body: SplitConfigurationRule | SplitConfigurationRuleDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SplitConfiguration, PostMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody]:
        """`Creates a rule
        <https://docs.adyen.com/platforms/automatic-split-configuration/manage-split-configurations/api/#create-rule>`__
        in the split configuration profile specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/splitConfigurations/{splitConfigurationId}"),
            path_params=[
                param[str]("merchantId", merchant_id), param[str]("splitConfigurationId", split_configuration_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SplitConfigurationRule | SplitConfigurationRuleDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SplitConfiguration],
            error_mapper=post_merchants_merchant_id_split_configurations_split_configuration_id_error_mapper,
            request_options=request_options,
        )


class AsyncSplitConfigurationMerchantLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_merchants_merchant_id_split_configurations_split_configuration_id(
        self, merchant_id: str, split_configuration_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SplitConfiguration, DeleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody]:
        """Deletes the split configuration profile specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/merchants/{merchantId}/splitConfigurations/{splitConfigurationId}"),
            path_params=[
                param[str]("merchantId", merchant_id), param[str]("splitConfigurationId", split_configuration_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SplitConfiguration],
            error_mapper=delete_merchants_merchant_id_split_configurations_split_configuration_id_error_mapper,
            request_options=request_options,
        )

    async def delete_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id(
        self,
        merchant_id: str,
        split_configuration_id: str,
        rule_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SplitConfiguration, DeleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdErrorBody
    ]:
        """Deletes the rule specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            rule_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9(
                "/merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId}"
            ),
            path_params=[
                param[str]("merchantId", merchant_id),
                param[str]("splitConfigurationId", split_configuration_id),
                param[str]("ruleId", rule_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SplitConfiguration],
            error_mapper=delete_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_split_configurations(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SplitConfigurationList, GetMerchantsMerchantIdSplitConfigurationsErrorBody]:
        """Returns the list of split configuration profiles for the merchant account.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/splitConfigurations"),
            path_params=[param[str]("merchantId", merchant_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SplitConfigurationList],
            error_mapper=get_merchants_merchant_id_split_configurations_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_split_configurations_split_configuration_id(
        self, merchant_id: str, split_configuration_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SplitConfiguration, GetMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody]:
        """Returns the details of the split configuration profile specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/splitConfigurations/{splitConfigurationId}"),
            path_params=[
                param[str]("merchantId", merchant_id), param[str]("splitConfigurationId", split_configuration_id)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SplitConfiguration],
            error_mapper=get_merchants_merchant_id_split_configurations_split_configuration_id_error_mapper,
            request_options=request_options,
        )

    async def patch_merchants_merchant_id_split_configurations_split_configuration_id(
        self,
        merchant_id: str,
        split_configuration_id: str,
        *,
        body: UpdateSplitConfigurationRequest | UpdateSplitConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SplitConfiguration, PatchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody]:
        """Changes the description of the split configuration profile specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/splitConfigurations/{splitConfigurationId}"),
            path_params=[
                param[str]("merchantId", merchant_id), param[str]("splitConfigurationId", split_configuration_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSplitConfigurationRequest | UpdateSplitConfigurationRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SplitConfiguration],
            error_mapper=patch_merchants_merchant_id_split_configurations_split_configuration_id_error_mapper,
            request_options=request_options,
        )

    async def patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id(
        self,
        merchant_id: str,
        split_configuration_id: str,
        rule_id: str,
        *,
        body: UpdateSplitConfigurationRuleRequest | UpdateSplitConfigurationRuleRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        SplitConfiguration, PatchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdErrorBody
    ]:
        """Changes the `split conditions of the rule
        <https://docs.adyen.com/platforms/automatic-split-configuration/manage-split-configurations/api/#update-condition>`__
        specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The identifier of the split configuration.
            rule_id: The unique identifier of the split configuration rule.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9(
                "/merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId}"
            ),
            path_params=[
                param[str]("merchantId", merchant_id),
                param[str]("splitConfigurationId", split_configuration_id),
                param[str]("ruleId", rule_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSplitConfigurationRuleRequest | UpdateSplitConfigurationRuleRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SplitConfiguration],
            error_mapper=patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id_error_mapper,
            request_options=request_options,
        )

    async def patch_merchants_split_configurations_rules_split_logic(
        self,
        merchant_id: str,
        split_configuration_id: str,
        rule_id: str,
        split_logic_id: str,
        *,
        body: UpdateSplitConfigurationLogicRequest | UpdateSplitConfigurationLogicRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SplitConfiguration, PatchMerchantsSplitConfigurationsRulesSplitLogicErrorBody]:
        """Changes the `split logic
        <https://docs.adyen.com/platforms/automatic-split-configuration/manage-split-configurations/api/#update-split-logic>`__
        specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            rule_id: The unique identifier of the split configuration rule.
            split_logic_id: The unique identifier of the split configuration split.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9(
                "/merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId}/splitLogic/{splitLogicId}",
            ),
            path_params=[
                param[str]("merchantId", merchant_id),
                param[str]("splitConfigurationId", split_configuration_id),
                param[str]("ruleId", rule_id),
                param[str]("splitLogicId", split_logic_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSplitConfigurationLogicRequest | UpdateSplitConfigurationLogicRequestDict | None](
                body
            ),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SplitConfiguration],
            error_mapper=patch_merchants_split_configurations_rules_split_logic_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_id_split_configurations(
        self,
        merchant_id: str,
        *,
        body: SplitConfiguration | SplitConfigurationDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SplitConfiguration, PostMerchantsMerchantIdSplitConfigurationsErrorBody]:
        """Creates a split configuration profile to `split payments automatically
        <https://docs.adyen.com/platforms/automatic-split-configuration/>`__. After you `associate it with a store
        <https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId>`__/stores/(storeId)#request-splitConfiguration)
        in your merchant account, it splits the funds of all transactions processed through that store between your
        liable balance account and `your user's balance account
        <https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId>`__/stores/(storeId)#request-splitConfiguration-balanceAccountId).

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/splitConfigurations"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SplitConfiguration | SplitConfigurationDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SplitConfiguration],
            error_mapper=post_merchants_merchant_id_split_configurations_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_id_split_configurations_split_configuration_id(
        self,
        merchant_id: str,
        split_configuration_id: str,
        *,
        body: SplitConfigurationRule | SplitConfigurationRuleDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SplitConfiguration, PostMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdErrorBody]:
        """`Creates a rule
        <https://docs.adyen.com/platforms/automatic-split-configuration/manage-split-configurations/api/#create-rule>`__
        in the split configuration profile specified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API - SplitConfiguration read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            split_configuration_id: The unique identifier of the split configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/splitConfigurations/{splitConfigurationId}"),
            path_params=[
                param[str]("merchantId", merchant_id), param[str]("splitConfigurationId", split_configuration_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SplitConfigurationRule | SplitConfigurationRuleDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SplitConfiguration],
            error_mapper=post_merchants_merchant_id_split_configurations_split_configuration_id_error_mapper,
            request_options=request_options,
        )
