from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InstalmentType(str, Enum):
    """Type of instalment transaction. For requesting an instalment payment transaction. Possible values:
    * **DeferredInstalments**
    * **EqualInstalments**
    * **InequalInstalments**"""

    DEFERRED_INSTALMENTS = "DeferredInstalments"
    EQUAL_INSTALMENTS = "EqualInstalments"
    INEQUAL_INSTALMENTS = "InequalInstalments"

    __str__ = str.__str__


InstalmentTypeOrStr: TypeAlias = Annotated[InstalmentType | str, open_enum_validator(InstalmentType)]
