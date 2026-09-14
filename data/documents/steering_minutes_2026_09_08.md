# Project Phoenix — Steering Committee Minutes

**Date:** 8 September 2026
**Time:** 14:00 to 15:30
**Chair:** Amara Okonkwo, Programme Director
**Minutes:** David Renshaw, Project Manager

## Attendees

Amara Okonkwo (Chair), David Renshaw, Sarah Whitfield, Priya Nair, Tom Brennan, Marcus Chen, Rachel Adeyemi, James Fitzgerald, Ingrid Larsen, Callum Roberts, Elena Vasquez (Northwind Technologies)

**Apologies:** Nadia Hassan

## 1. Minutes of the previous meeting

Minutes of 11 August approved without amendment.

## 2. Programme status

David Renshaw presented the position as at 4 September. Overall status Amber. Build for release 1 completed on 4 September, one week behind baseline but within tolerance. MS-04 closed.

## 3. UAT environment

Sarah Whitfield reported that Infrastructure has confirmed a five working day delay to provisioning of the UAT environment. Capacity originally allocated to Project Phoenix was reassigned to the network refresh programme without notice to the project. This has been logged as ISSUE-007 and is the realisation of RISK-004, which has been open since 21 August.

The environment was planned to be available on 12 October (MS-06). The revised date is expected to be 19 October but has not yet been confirmed by Infrastructure.

Tom Brennan noted that user acceptance testing is scheduled to complete on 30 October (MS-07). A five day loss at the start of the window leaves eight working days for UAT against a planned thirteen. He stated that this is not sufficient to complete the full UAT scope and that either the completion date moves or scope is reduced.

Amara Okonkwo asked whether the go-live date of 9 November is at risk. David Renshaw responded that it is not yet, but that it will be if the environment is not available by 19 October or if UAT identifies a significant volume of defects.

The Chair asked for the revised date to be confirmed in writing by Infrastructure by 11 September, and for a reforecast testing schedule showing what can be de-scoped. **ACTION-021** and **ACTION-022** raised.

## 4. Data migration

Priya Nair reported that ISSUE-003 remains open with 12 per cent of records failing validation. Root cause analysis under ACTION-014 is due 11 September. Early indications are that two thirds of the failures relate to date format handling, which is expected to be resolvable through a transformation rule, and one third to orphaned attachment references, which will require manual intervention.

Ingrid Larsen noted that the extended cleansing contractor engagement takes that budget line to 74,000 against a plan of 48,000. A change request is required. **ACTION-026** raised.

Amara Okonkwo asked whether the 99 per cent reconciliation success criterion remains achievable. Priya Nair confirmed that it does, provided the transformation rule resolves the date format failures as expected, and undertook to report at the October committee.

## 5. Supplier resourcing

James Fitzgerald reported that Northwind has not yet provided written confirmation of resource levels for October and November. Elena Vasquez confirmed that the named team remains committed but that formal confirmation requires sign-off from the Northwind account director.

The Chair requested written confirmation by 25 September. **ACTION-023** raised. RISK-006 remains open at Medium.

Elena Vasquez also noted that the billing platform API specification (ISSUE-005) is expected to be delivered by 16 September.

## 6. Security

Marcus Chen confirmed the penetration test is booked for w/c 19 October with a remediation window to 2 November. Security assurance sign-off (MS-08) remains scheduled for 2 November, three days before the go-live decision point. He noted that this leaves no float and that any significant finding would put the go-live date at risk. RISK-009 remains open at High.

## 7. Business change

Rachel Adeyemi reported that the training schedule has been published and that contact centre operations have agreed in principle to release agents, subject to volume forecasts. The knowledge article audit is behind plan at 340 of 1,120 reviewed. Articles not reviewed by 16 October will be excluded from launch, which will reduce the knowledge base available to the Aurora assistant at go-live.

Amara Okonkwo asked what the impact of a reduced article set would be. Rachel Adeyemi responded that the highest-volume contact reasons are prioritised in the audit, so coverage of common queries should be unaffected, but that agents will need to be briefed on the gap. **ACTION-025** raised.

## 8. Cutover

Callum Roberts confirmed the cutover rehearsal is scheduled for w/c 26 October. The rollback plan will be presented to the October committee for approval. **ACTION-024** raised. RISK-011 remains open at High.

## 9. Decisions

- **DEC-014:** Go-live date of 9 November 2026 reaffirmed. The committee will review at the October meeting in light of the UAT environment position.
- **DEC-015:** Testing scope reduction is approved in principle as the preferred response to a compressed UAT window, in preference to moving the go-live date. Specific de-scoping to be presented at the October committee.
- **DEC-016:** A change request for the data cleansing contractor overspend is approved in principle subject to submission through change control.

## 10. Any other business

None.

**Next meeting:** 13 October 2026, 14:00.
