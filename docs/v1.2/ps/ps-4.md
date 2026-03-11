---
title: 'PS.4: Ensure Software Updates Are Robust and Reliable'
practice_identifier: PS
task_identifier: PS.4
version: '1.2'
references:
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-03, CM-04, SA-11'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-11'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-02, CM-06, CM-09, SA-10'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): CM-02, CM-06'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-02, CM-09, SA-08, SA-10'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): CM-02'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CA-06, CA-07, CM-09, SA-10'
---

# PS.4: Ensure Software Updates Are Robust and Reliable

Implement robust and reliable software update strategies, preferably allowing customers to control any updates to the software package and application configurations. Help software acquirers maintain operations and minimize disruptions by ensuring that software updates are tested and responsibly delivered.

## PS.4.1 {: #ps-4-1 }

Thoroughly test all releases following all guidance in PW.

???+ example "Implementation Examples"
    * Example 1: Test using configurations and environments that replicate actual or expected customer installations.\nExample 2: Consider using an "early access" program to allow customers to test updates before general release.

??? info "References"
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-03, CM-04, SA-11
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-11

## PS.4.2 {: #ps-4-2 }

Use tiered update and release strategies, such as canaries, staged roll-out, and test deployments.

???+ example "Implementation Examples"
    * Example 1: Enable customers to configure and identify those systems that they consider critical and those that are considered safe to receive early updates for testing purposes.\nExample 2: Support multiple strategies for rolling out updates to customers, including staged or segmented rollouts with built-in wait times for customer feedback.\nExample 3: Consider the use of mechanisms that enable tailored updates or that support or provide information for troubleshooting problems while still maintaining user privacy.

??? info "References"
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-02, CM-06, CM-09, SA-10
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): CM-02, CM-06

## PS.4.3 {: #ps-4-3 }

Include robust rollback mechanisms for updates.

???+ example "Implementation Examples"
    * Example 1: Failed software updates automatically revert software to the last known good configuration, leaving systems in a runnable state.\nExample 2: Enable end-user organizations to roll back updates on systems as needed.\nExample 3: Implement protection mechanisms that prevent unauthorized roll-back to vulnerable software versions.

??? info "References"
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-02, CM-09, SA-08, SA-10
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): CM-02

## PS.4.4 {: #ps-4-4 }

Maintain robust and reliable update engines and associated infrastructure for the delivery of updates.

???+ example "Implementation Examples"
    * Example 1: Make the update engine fault-tolerant so that it can recover and retry downloading an update in the event of infrastructure overload.\nExample 2: Have the delivery infrastructure for updates degrade gracefully, or refuse new download attempts until current requests have been completed.

??? info "References"
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CA-06, CA-07, CM-09, SA-10

