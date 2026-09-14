# Project Phoenix — Weekly Status Report

**Week ending:** 11 September 2026
**Author:** David Renshaw, Project Manager
**Distribution:** Steering Committee, workstream leads

## Overall status: Amber

The UAT environment delay confirmed at the steering committee on 8 September has moved Testing to Amber. The go-live date of 9 November is unchanged but has lost its float.

## Workstream status

| Workstream | This week | Last week | Commentary |
|---|---|---|---|
| Programme | Green | Green | Governance operating normally |
| Technology | Amber | Green | UAT environment provisioning delayed by five days |
| Data | Amber | Amber | Root cause analysis complete; remediation approach agreed |
| Testing | Amber | Green | UAT window compressed from thirteen to eight working days |
| Security | Green | Green | Penetration test booked; no float after remediation window |
| Business Change | Amber | Amber | Knowledge article audit remains behind plan |
| Service | Green | Green | Cutover rehearsal scheduled |

## Why Testing has moved to Amber

The UAT environment was due on 12 October (MS-06). Infrastructure has confirmed a five working day delay because capacity allocated to Project Phoenix was reassigned to the network refresh programme. This is ISSUE-007 and is the realisation of RISK-004.

The revised environment date is expected to be 19 October. Written confirmation was requested from Infrastructure by 11 September under ACTION-021. That confirmation has not been received and the action is now overdue.

User acceptance testing is still scheduled to complete on 30 October (MS-07). Losing five days at the start reduces the window from thirteen working days to eight. Tom Brennan has advised that the full UAT scope cannot be completed in eight days. The steering committee agreed under DEC-015 that reducing test scope is preferred to moving go-live. A reforecast schedule showing proposed de-scoping is due on 18 September under ACTION-022.

## Progress this week

- Root cause analysis of the validation failures completed (ACTION-014). Two thirds of failures relate to date format handling and will be resolved by a transformation rule; one third relate to orphaned attachment references and require manual intervention. ISSUE-003 remains open pending the fix.
- September steering committee held on 8 September. Go-live date reaffirmed under DEC-014.
- Training materials work started for the Aurora knowledge assistant (ACTION-025).
- Change request drafted for the data cleansing contractor overspend (ACTION-026).

## Areas of concern

**UAT environment.** As above. ACTION-021 is overdue with Sarah Whitfield.

**Security has no float.** Penetration testing runs w/c 19 October with remediation to 2 November, and security sign-off (MS-08) falls three days before the go-live decision point. Any significant finding puts go-live at risk. RISK-009 remains High.

**Knowledge article audit.** 340 of 1,120 articles reviewed. Articles not reviewed by 16 October will be excluded from launch. ISSUE-008 open.

## Milestones

| Milestone | Baseline | Forecast | Status |
|---|---|---|---|
| MS-05 System testing complete | 9 October 2026 | 9 October 2026 | On track |
| MS-06 UAT environment available | 12 October 2026 | 19 October 2026 | At risk |
| MS-07 User acceptance testing complete | 30 October 2026 | 30 October 2026 | At risk |
| MS-08 Security sign-off | 2 November 2026 | 2 November 2026 | Not started |
| MS-11 Go-live | 9 November 2026 | 9 November 2026 | Not started |

## Budget

Forecast outturn is 2,283,000 against a budget of 2,400,000. Contingency drawn down to date is 63,000, against integration services, cloud infrastructure, data cleansing and test resource. The largest adverse variance is data cleansing at 26,000 over plan, subject to the change request under ACTION-026.

## Look ahead

- Written confirmation of the revised UAT environment date (ACTION-021, overdue)
- Reforecast testing schedule with proposed de-scoping due 18 September (ACTION-022)
- Billing platform API specification expected 16 September (ISSUE-005)
- Supplier resource confirmation due 25 September (ACTION-023)
