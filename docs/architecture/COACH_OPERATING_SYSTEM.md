# Coach Operating System architecture

## Boundary

The product has three layers: canonical content (immutable JSON/MDX), coach domain state (stable references plus configuration), and persistence adapters. UI talks to the domain API, never directly to `localStorage` or a future vendor SDK.

## Domain records

`CoachProfile`, `SavedItem`, `RecentItem`, `WorkspaceSession`, `SessionItem`, `SessionConfiguration`, `SessionReflection`, `AssessmentRecord`, `OfflinePack`, and `EntitlementContext`. Records reserve optional `user_id` and `organization_id`; anonymous mode uses a local owner key. No child name, birth date, photo, health or parent field exists.

## Persistence port

The browser adapter implements `load`, `save`, `export`, `clear`, and monotonic revision metadata. A future cloud adapter must implement the same contract. User-facing logic consumes commands (`saveItem`, `addToSession`, `completeSession`) and selectors (`getContinueCard`, `getWorkspaceSession`), so provider replacement does not change components.

## Canonical reference rule

Personal state stores IDs and choices only. Rendering resolves IDs through existing canonical loaders and fails visibly when a reference is unavailable. Canonical sessions are saved or duplicated into personal plans; never mutated.

## Conflict and privacy rule

Reflection is append/update by stable record ID with `updated_at` and revision. A future sync conflict must retain both versions or request a choice; it may never silently discard reflection. Current anonymous data stays on-device and can be exported/cleared.

## Entitlement and organizations

Feature access is resolved by a central pure policy over feature, plan, role and optional organization. Safety content always resolves open. Organization and role fields are forward-compatible only; no Club UI or arbitrary permission matrix is implemented in Wave-4.
