Audit Tool with TEALAS


# Audit Tool

## Purpose

The Audit Tool provides an automated framework for validating IAM, access management, and security controls across GCP environments.

The framework is designed to perform configurable compliance, governance, and security checks, identify policy violations, and generate alerts for remediation.

The solution is extensible and allows new audit controls to be added as requirements evolve.

## Current Scope

The initial implementation focuses on validating controls associated with the TEALAS Just-In-Time (JIT) access model, including:

* Read-Only Group Permission Validation
* TEALAS Access Expiration Validation
* Privileged Group Binding Validation
* Activation Group Consistency Validation

Additional audit controls may be incorporated in future releases to support broader IAM and security governance requirements.


Purpose

The Audit Tool with TEALAS provides automated validation of the GCP Just-In-Time (JIT) privileged access model. The tool continuously verifies that privileged access is configured and managed according to the approved TEALAS architecture.

Framework
Technology
Python-based framework
Source code stored in Bitbucket
Initial execution through Cloud Build
Future deployment as a Docker container with a custom Helm Chart
High-Level Workflow
Scheduler
    ↓
Audit Framework
    ↓
Cloud Identity
IAM Policies
Cloud Asset Inventory
    ↓
Email Notifications
Audit Controls
Test 1 – Read-Only Group Permission Validation
Objective

Ensure that groups designated as read-only do not have write or administrative permissions.

Validation
Identify groups following read-only naming standards (e.g., *_RO).
Analyze effective permissions granted through IAM roles.
Evaluate both predefined and custom roles.
Detect permissions that allow create, update, delete, modify, or administrative actions.
Failure Condition

A read-only group contains one or more write or administrative permissions.

Alert

Email notification sent to IAM Operations team.

Test 2 – TEALAS Access Expiration Validation
Objective

Ensure temporary access granted through TEALAS is removed after the approved access period expires.

Validation
Identify all Activation Groups.
Review active memberships.
Verify users are automatically removed after the TEALAS approval period (24 hours).
Verify expired memberships do not remain in Activation Groups.
Failure Condition

An expired user remains a member of an Activation Group.

Alert

Email notification sent to IAM Operations and TEALAS support teams.

Test 3 – Privileged Group Binding Validation
Objective

Ensure privileged IAM bindings exist only on Activation Groups.

Validation
Identify all Activation Groups.
Locate corresponding privileged Membership Groups.
Verify IAM bindings are attached only to Activation Groups.
Verify Membership Groups do not contain privileged IAM bindings.
Failure Condition

A Membership Group contains privileged IAM bindings.

Alert

Critical severity email notification.

Test 4 – Activation Group Consistency Validation
Objective

Ensure Activation Groups and corresponding privileged groups remain properly aligned.

Validation
Identify all Activation Groups.
Verify a corresponding privileged Membership Group exists.
Verify naming conventions and group relationships remain consistent.
Failure Condition

An Activation Group exists without a corresponding privileged Membership Group.

Alert

Email notification sent to IAM Operations team.

Open Questions
Alert Recipients

Need confirmation from stakeholders regarding notification distribution lists:

IAM Operations Team
TEALAS Support Team
Security Governance Team
Execution Frequency

Recommended:

Environment	Frequency
Production	Every 4 hours
UAT	Daily
Development	Daily

One additional audit I would strongly recommend based on the TEALAS design document:

Test 5 – Activation Group Membership Validation
Objective

Ensure Activation Groups are used only for temporary access.

Validation
Identify all Activation Groups.
Verify every membership contains an expiration timestamp.
Verify no permanent memberships exist.
Failure Condition

A member exists in an Activation Group without an expiration timestamp.

Alert

Critical severity email notification.

This test directly validates the core TEALAS requirement that all Activation Group memberships must be temporary. It is actually one of the strongest controls in the entire design.