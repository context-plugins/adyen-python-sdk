from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PatchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdErrorBody: TypeAlias = (
    RestServiceError | RawError
)


@dataclass(frozen=True, slots=True)
class _PatchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdError:
    def map(
        self, response: HttpResponse
    ) -> PatchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id_error_mapper: Final[
    ErrorMapper[PatchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdErrorBody]
] = _PatchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdError()
