# Project Phoenix — Project Charter

**Client:** Cavendish Energy Ltd
**Programme:** Customer Service Transformation
**Document version:** 2.1
**Approved:** 24 April 2026
**Approver:** Amara Okonkwo, Programme Director
**Author:** David Renshaw, Project Manager

## 1. Background

Cavendish Energy handles approximately 41,000 customer contacts per month across telephone, email and web channels. These are managed in CaseTrack 7, an on-premise case management platform first deployed in 2011 and last substantially upgraded in 2017.

CaseTrack 7 is no longer supported by its vendor beyond January 2027. It cannot support the omnichannel contact model the business has committed to, agent handling times are above industry benchmark, and reporting requires manual extraction into spreadsheets.

## 2. Objectives

1. Replace CaseTrack 7 with Northwind Service Cloud, a supported cloud case management platform, before the licence expiry of 31 January 2027.
2. Deploy the Aurora Knowledge Assistant to give agents AI-supported access to knowledge articles during live contacts.
3. Reduce average case handling time by 15 per cent within six months of go-live.
4. Provide a single customer view combining case history, billing status and contact preferences.
5. Enable self-service resolution for the ten highest-volume contact reasons.

## 3. Scope

### In scope
- Implementation and configuration of Northwind Service Cloud for the contact centre and back office teams
- Migration of open cases and 24 months of closed case history from CaseTrack 7
- Integration with the billing platform, the identity provider and the customer data platform
- Deployment of the Aurora Knowledge Assistant with migrated and reviewed knowledge content
- Training for 280 contact centre agents and 40 back office users
- Decommissioning of CaseTrack 7

### Out of scope
- Replacement of the billing platform
- Changes to the customer-facing website beyond the case status widget
- Field operations scheduling
- Migration of case history older than 24 months, which will be retained in a read-only archive

## 4. Timeline

| Phase | Start | End |
|---|---|---|
| Initiation | 6 April 2026 | 30 April 2026 |
| Definition | 1 May 2026 | 12 June 2026 |
| Design | 15 June 2026 | 10 July 2026 |
| Build | 13 July 2026 | 28 August 2026 |
| Test | 1 September 2026 | 30 October 2026 |
| Deploy | 2 November 2026 | 9 November 2026 |
| Close and decommission | 10 November 2026 | 16 January 2027 |

Go-live is planned for 9 November 2026, following a go-live decision point on 5 November 2026.

## 5. Budget

The approved budget is 2,400,000 including a contingency of 180,000. Any single commitment above 25,000 not already in the baseline requires change control approval from the steering committee.

## 6. Governance

- **Steering Committee** — monthly, chaired by Amara Okonkwo. Attended by workstream leads, Finance and the supplier account director.
- **Delivery Board** — weekly, chaired by David Renshaw. Attended by workstream leads.
- **Workstream stand-ups** — daily, within each workstream.

Escalation runs from workstream lead to Project Manager to Programme Director to the Customer Operations Director.

## 7. Workstreams and leads

| Workstream | Lead |
|---|---|
| Programme | David Renshaw |
| Technology | Sarah Whitfield and Elena Vasquez |
| Data | Priya Nair |
| Testing | Tom Brennan |
| Security | Marcus Chen |
| Business Change | Rachel Adeyemi |
| Service | Callum Roberts |

## 8. Key assumptions

1. Northwind Technologies will maintain the resource levels set out in the statement of work through to go-live.
2. Contact centre operations will release agents for training during October and November.
3. Infrastructure will provide non-production environments in line with the agreed environment plan.
4. Legacy case data quality is broadly consistent with the sample assessed during Definition.

## 9. Success criteria

- Go-live achieved by 9 November 2026 with no severity 1 defects outstanding
- 99 per cent of in-scope case records migrated and reconciled
- 90 per cent of agents trained before go-live
- Average handling time reduced by 15 per cent within six months
- CaseTrack 7 decommissioned by 16 January 2027
