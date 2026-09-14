# Project Phoenix — Architecture Decision Record

**Owner:** Elena Vasquez, Solution Architect
**Version:** 1.3

Decisions are recorded when a choice could reasonably have been made differently. Each entry states the decision, the options considered, the rationale and the accepted trade-off.

---

## ADR-001 — Software as a service rather than managed hosting

**Date:** 26 June 2026
**Status:** Approved
**Decision maker:** Amara Okonkwo

**Decision.** Northwind Service Cloud will be consumed as a multi-tenant software as a service product rather than as a single-tenant managed instance.

**Options considered.** Multi-tenant SaaS; single-tenant managed hosting by Northwind; self-hosted deployment in Cavendish infrastructure.

**Rationale.** Multi-tenant carries the lowest total cost, removes platform patching from Cavendish, and provides upgrades without project effort. Self-hosting was discounted early as it reproduces the support burden that CaseTrack 7 created.

**Trade-off accepted.** Less control over upgrade timing. Northwind applies platform releases on a published quarterly schedule and Cavendish cannot defer them beyond one cycle.

---

## ADR-002 — Real-time billing integration rather than nightly synchronisation

**Date:** 3 July 2026
**Status:** Approved
**Decision maker:** Elena Vasquez

**Decision.** Account status will be retrieved from the billing platform in real time by REST API at the point the agent opens the customer record, rather than replicated nightly into the case platform.

**Options considered.** Real-time API call; nightly batch replication; hybrid with cached values refreshed hourly.

**Rationale.** BR-02 requires agents to see current billing status. A nightly copy would show stale balances, which is the main complaint agents raise about CaseTrack 7 today.

**Trade-off accepted.** A dependency on billing platform availability during contact centre hours. If billing is unavailable the case platform remains usable but account status is shown as unavailable. This dependency is the basis of RISK-005, which concerns behaviour under production transaction volumes.

---

## ADR-003 — UK South deployment region

**Date:** 21 August 2026
**Status:** Approved
**Decision maker:** Marcus Chen

**Decision.** The production and non-production tenants will be deployed in the UK South region.

**Options considered.** Northwind's default Ireland region; UK South; UK West.

**Rationale.** TR-04 requires all customer data to be stored within the United Kingdom. The Ireland default does not satisfy this. UK South was selected over UK West on the basis of lower latency to the Cavendish network and broader service availability.

**Trade-off accepted.** UK South carries a premium of approximately 8 per cent on platform hosting compared with Ireland. This was accepted and is reflected in the budget.

**Consequence.** This decision closed RISK-012 on 21 August 2026.

---

## ADR-004 — Retrieval-based knowledge assistant rather than a fine-tuned model

**Date:** 28 August 2026
**Status:** Approved
**Decision maker:** Elena Vasquez

**Decision.** The Aurora Knowledge Assistant will answer agent queries by retrieving from the knowledge article set and citing the source article, rather than by fine-tuning a model on Cavendish content.

**Options considered.** Retrieval over the article set; fine-tuning a model on historic cases and articles; a rules-based decision tree.

**Rationale.** TR-09 requires every suggestion to cite its source article, which retrieval supports directly and fine-tuning does not. Knowledge articles change frequently and a retrieval approach picks up changes as soon as content is updated, with no retraining. Fine-tuning was also judged to carry an unacceptable risk of the assistant producing confident answers with no traceable source.

**Trade-off accepted.** Answer quality is bounded by article quality. An out-of-date or missing article produces a poor answer or none at all. This is the basis of RISK-007 and is why the content audit under ISSUE-008 matters to the launch.

---

## ADR-005 — Read-only archive for case history beyond 24 months

**Date:** 4 September 2026
**Status:** Approved
**Decision maker:** Priya Nair

**Decision.** Case records older than 24 months will not be migrated. They will be held in a read-only archive accessible to a small number of named users.

**Options considered.** Migrate all history; migrate 24 months with archive; migrate 24 months with no archive.

**Rationale.** Full migration would extend the migration window by an estimated three weeks and increase reconciliation scope substantially at a point when validation failures are already the principal data concern. Retention obligations under BR-07 are satisfied by the archive.

**Trade-off accepted.** Agents cannot see case history older than 24 months in the new platform and must raise a request to the archive team, expected to affect fewer than 40 contacts per month.
