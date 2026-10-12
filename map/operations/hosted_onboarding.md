<!-- Generated file — do not edit; regenerated with the SDK. -->

# HostedOnboarding — operations

Accessor: `client.hosted_onboarding` · Source: `adyen/apis/hosted_onboarding.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.hosted_onboarding.get_themes

- **Route**: `GET /themes`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def get_themes(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `OnboardingThemes`
- **Returns (raw)**: `ApiResult[OnboardingThemes, GetThemesErrorBody]`
- **Error**: `GetThemesErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OnboardingThemes` | `adyen/models/onboarding_themes.py` |
| `GetThemesErrorBody` | `adyen/errors/get_themes_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.hosted_onboarding.get_themes_id

- **Route**: `GET /themes/{id}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def get_themes_id(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `OnboardingTheme`
- **Returns (raw)**: `ApiResult[OnboardingTheme, GetThemesIdErrorBody]`
- **Error**: `GetThemesIdErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OnboardingTheme` | `adyen/models/onboarding_theme.py` |
| `GetThemesIdErrorBody` | `adyen/errors/get_themes_id_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.hosted_onboarding.post_legal_entities_id_onboarding_links

- **Route**: `POST /legalEntities/{id}/onboardingLinks`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def post_legal_entities_id_onboarding_links(id_: str, *, body: OnboardingLinkInfo | OnboardingLinkInfoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `OnboardingLink`
- **Returns (raw)**: `ApiResult[OnboardingLink, PostLegalEntitiesIdOnboardingLinksErrorBody]`
- **Error**: `PostLegalEntitiesIdOnboardingLinksErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OnboardingLinkInfo` | `adyen/models/onboarding_link_info.py` |
| `OnboardingLinkInfoDict` | `adyen/models/onboarding_link_info.py` |
| `OnboardingLink` | `adyen/models/onboarding_link.py` |
| `PostLegalEntitiesIdOnboardingLinksErrorBody` | `adyen/errors/post_legal_entities_id_onboarding_links_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

