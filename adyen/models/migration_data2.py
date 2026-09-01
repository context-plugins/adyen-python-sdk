from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .migrated_accounts import MigratedAccounts, MigratedAccountsDict
from .migrated_shareholders import MigratedShareholders, MigratedShareholdersDict
from .migrated_stores import MigratedStores, MigratedStoresDict


class MigrationData2(SdkBaseModel):
    """Details of the account holder migrated to the balance platform."""

    account_holder_id: Optional[str] = Field(default=UNSET, alias="accountHolderId")
    """The unique identifier of the account holder in the balance platform."""

    balance_platform: Optional[str] = Field(default=UNSET, alias="balancePlatform")
    """The unique identifier of the balance platfrom to which the account holder was migrated."""

    migrated: Optional[bool] = UNSET
    """Set to **true** if the account holder has been migrated."""

    migrated_accounts: Optional[list[MigratedAccounts]] = Field(default=UNSET, alias="migratedAccounts")
    """Contains the mapping of virtual account codes (classic integration) to the balance account codes (balance
    platform) associated with the migrated account holder."""

    migrated_shareholders: Optional[list[MigratedShareholders]] = Field(default=UNSET, alias="migratedShareholders")
    """Contains the mapping of shareholders associated with the migrated legal entities."""

    migrated_stores: Optional[list[MigratedStores]] = Field(default=UNSET, alias="migratedStores")
    """Contains the mapping of business lines and stores associated with the migrated account holder."""

    migration_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="migrationDate")
    """The date when account holder was migrated."""


class MigrationData2Dict(TypedDict):
    account_holder_id: NotRequired[str]
    balance_platform: NotRequired[str]
    migrated: NotRequired[bool]
    migrated_accounts: NotRequired[list[MigratedAccounts | MigratedAccountsDict]]
    migrated_shareholders: NotRequired[list[MigratedShareholders | MigratedShareholdersDict]]
    migrated_stores: NotRequired[list[MigratedStores | MigratedStoresDict]]
    migration_date: NotRequired[RFC3339DateTime]
