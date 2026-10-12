from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .checkout_network_token_option2 import CheckoutNetworkTokenOption2, CheckoutNetworkTokenOption2Dict


class CheckoutForwardRequestOptions2(SdkBaseModel):
    """The customizations that can be applied when making a forward request."""

    account_update: Optional[bool] = Field(default=UNSET, alias="accountUpdate")
    """Whether to check for a card account update (true) or not (false)"""

    dry_run: Optional[bool] = Field(default=UNSET, alias="dryRun")
    """Set to **true** to receive a copy of the request Adyen is making to the third party in the response. Any
    sensitive information will be masked in the response you receive. This functionality is only available in the test
    environment."""

    network_token: Optional[CheckoutNetworkTokenOption2] = Field(default=UNSET, alias="networkToken")
    """The object that contains the details for forwarding a network token."""

    network_tx_reference_paths: Optional[list[str]] = Field(default=UNSET, alias="networkTxReferencePaths")
    """Set in tokenize:true case when forwarding PAN. Addresses to the possible location(s) of networkTxReference in the
    incoming 3rd party response"""

    tokenize: Optional[bool] = UNSET
    """Set to **true**, the payment details are `tokenized <https://docs.adyen.com/online-payments/tokenization>`__."""

    transaction_link_id_paths: Optional[list[str]] = Field(default=UNSET, alias="transactionLinkIdPaths")
    """Set in tokenize:true case when forwarding PAN. Addresses to the possible location(s) of transactionLinkId in the
    incoming 3rd party response"""


class CheckoutForwardRequestOptions2Dict(TypedDict):
    account_update: NotRequired[bool]
    dry_run: NotRequired[bool]
    network_token: NotRequired[CheckoutNetworkTokenOption2Dict]
    network_tx_reference_paths: NotRequired[list[str]]
    tokenize: NotRequired[bool]
    transaction_link_id_paths: NotRequired[list[str]]
