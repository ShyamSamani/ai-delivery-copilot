# Project Phoenix — Requirements

**Version:** 1.4
**Baselined:** 19 June 2026
**Owner:** Nadia Hassan, Lead Business Analyst

Requirements were baselined one week later than the milestone date of 12 June following late input from the back office team on case categorisation.

## Business requirements

| ID | Requirement | Priority | Workstream |
|---|---|---|---|
| BR-01 | Agents must be able to create, update and resolve cases across telephone, email, web form and chat channels from a single interface | Must | Technology |
| BR-02 | Agents must see a single customer view showing case history, billing status, meter details and contact preferences | Must | Technology |
| BR-03 | The system must suggest relevant knowledge articles to agents during a live contact | Must | Business Change |
| BR-04 | Customers must be able to check case status online without contacting the centre | Should | Technology |
| BR-05 | Team managers must be able to report on volumes, handling times and resolution rates without manual extraction | Must | Technology |
| BR-06 | The system must support the ten highest-volume contact reasons through guided self-service | Should | Technology |
| BR-07 | Case records must be retained for seven years in line with the retention policy | Must | Security |
| BR-08 | Vulnerable customer flags must be visible to agents at the point of contact | Must | Business Change |

## Technical requirements

| ID | Requirement | Priority | Workstream |
|---|---|---|---|
| TR-01 | The platform must integrate with the billing platform via REST API for real-time account status | Must | Technology |
| TR-02 | The platform must authenticate users through the corporate identity provider using single sign-on | Must | Technology |
| TR-03 | The platform must support 320 concurrent users with page response under two seconds at the 95th percentile | Must | Technology |
| TR-04 | All customer data must be stored within the United Kingdom | Must | Security |
| TR-05 | The platform must maintain an immutable audit log of all case access and amendment | Must | Security |
| TR-06 | Data at rest must be encrypted using AES-256 and data in transit using TLS 1.3 or later | Must | Security |
| TR-07 | The platform must support a recovery time objective of four hours and a recovery point objective of fifteen minutes | Must | Technology |
| TR-08 | Open cases and 24 months of closed case history must be migrated from CaseTrack 7 with full reconciliation | Must | Data |
| TR-09 | The Aurora Knowledge Assistant must cite the source article for every suggestion it makes | Must | Business Change |
| TR-10 | The platform must handle a peak of 2,800 case creations per hour during a supply incident | Should | Technology |

## Notes on TR-04

TR-04 was the subject of architecture decision ADR-003. Northwind's default deployment region is Ireland, which does not satisfy the requirement. The decision to deploy in the UK South region was taken on 21 August 2026 and closed RISK-012.

## Notes on TR-08

The reconciliation approach requires that every migrated record matches its source on case reference, customer identifier, creation date, status and attachment count. The 12 per cent failure rate recorded in ISSUE-003 is measured against this definition.
