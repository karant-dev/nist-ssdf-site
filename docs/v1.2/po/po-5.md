---
title: 'PO.5: Implement and Maintain Secure Environments for Software Development'
practice_identifier: PO
task_identifier: PO.5
version: '1.2'
references:
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  DE.1, IA.1, IA.2'
- "[CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper):\
  \ Securing Build Pipelines\u2014Controlled Environments"
- '[IEC62443](https://webstore.iec.ch/publication/33615): SM-7'
- '[NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): PR.AC-5, PR.DS-7'
- '[SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf):
  Tasks Requiring the Help of Security Experts 11'
- '[SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf):
  Vendor Software Delivery Integrity Controls'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): AC-04, CM-02, CM-12, PL-08,
  SA-03, SA-03(01), SA-08, SA-15, SA-17, SC-07, SC-07(01), SC-07(29)'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): AC-04, CM-02, CM-12,
  PL-08, SA-03, SC-07'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): OM-NET-001, SP-SYS-001; T0019,
  T0023, T0144, T0160, T0262, T0438, T0484, T0485, T0553; K0001, K0005, K0007, K0033,
  K0049, K0056, K0061, K0071, K0104, K0112, K0179, K0326, K0487; S0007, S0084, S0121;
  A0048'
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  DE.1-1, IA.1, IA.2'
- '[NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): PR.AC-4, PR.AC-7, PR.IP-1,
  PR.IP-3, PR.IP-12, PR.PT-1, PR.PT-3, DE.CM'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-02, CM-03, CM-04, CM-06,
  CM-14, SA-15, SA-17'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): CM-02, CM-03, CM-06'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): OM-ADM-001, SP-SYS-001; T0484,
  T0485, T0489, T0553; K0005, K0007, K0077, K0088, K0130, K0167, K0205, K0275; S0076,
  S0097, S0121, S0158; A0155'
---

# PO.5: Implement and Maintain Secure Environments for Software Development

Ensure that all components of the environments for software development are strongly protected from internal and external threats to prevent compromises of the environments or the software being developed or maintained within them. Examples of environments for software development include development, build, test, and distribution environments.

## PO.5.1 {: #po-5-1 }

Separate and protect each environment involved in software development.

???+ example "Implementation Examples"
    * Example 1: Use multi-factor, risk-based authentication and conditional access for each environment.\nExample 2: Use network segmentation and access controls to separate the environments from each other and production environments and to separate components from each other within each non-production environment in order to reduce attack surfaces and attackers' lateral movement and privilege/access escalation.\nExample 3: Enforce authentication, and tightly restrict connections entering and exiting each software development environment, including minimizing access to the internet to only what is necessary.\nExample 4: Minimize direct human access to toolchain systems, such as build services. Continuously monitor and audit all access attempts and all use of privileged access.\nExample 5: Minimize the use of production-environment software and services from non-production environments.\nExample 6: Regularly log, monitor, and audit trust relationships for authorization and access between the environments and between the components within each environment.\nExample 7: Continuously log and monitor operations and alerts across all components of the development environment to detect, respond, and recover from attempted and actual cyber incidents.\nExample 8: Configure security controls and other tools involved in separating and protecting the environments to generate artifacts for their activities.\nExample 9: Continuously monitor all software deployed in each environment for new vulnerabilities, and respond to vulnerabilities appropriately following a risk-based approach.\nExample 10: Configure and implement measures to secure the environments' hosting infrastructures following a zero trust architecture.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): DE.1, IA.1, IA.2
    * [CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper): Securing Build Pipelines—Controlled Environments
    * [IEC62443](https://webstore.iec.ch/publication/33615): SM-7
    * [NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): PR.AC-5, PR.DS-7
    * [SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf): Tasks Requiring the Help of Security Experts 11
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Vendor Software Delivery Integrity Controls
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): AC-04, CM-02, CM-12, PL-08, SA-03, SA-03(01), SA-08, SA-15, SA-17, SC-07, SC-07(01), SC-07(29)
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): AC-04, CM-02, CM-12, PL-08, SA-03, SC-07
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): OM-NET-001, SP-SYS-001; T0019, T0023, T0144, T0160, T0262, T0438, T0484, T0485, T0553; K0001, K0005, K0007, K0033, K0049, K0056, K0061, K0071, K0104, K0112, K0179, K0326, K0487; S0007, S0084, S0121; A0048

## PO.5.2 {: #po-5-2 }

Secure and harden development endpoints (e.g., for software designers, developers, testers, builders) to perform development-related tasks using a risk-based approach.

???+ example "Implementation Examples"
    * Example 1: Configure each development endpoint based on approved hardening guides and checklists (e.g., enable FIPS-compliant encryption of all sensitive data at rest and in transit).\nExample 2: Configure development endpoints and resources to provide the least functionality needed by users and services and to enforce the principle of least privilege.\nExample 3: Continuously monitor the security posture of all development endpoints, including monitoring and auditing all use of privileged access.\nExample 4: Configure security controls and other tools involved in securing and hardening development endpoints to generate artifacts for their activities.\nExample 5: Require multi-factor authentication for all access to development endpoints and resources.\nExample 6: Provide dedicated development endpoints on non-production networks for performing all development-related tasks. Provide separate endpoints on production networks for all other tasks.\nExample 7: Configure each development endpoint following a zero trust architecture.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): DE.1-1, IA.1, IA.2
    * [IEC62443](https://webstore.iec.ch/publication/33615): SM-7
    * [NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): PR.AC-4, PR.AC-7, PR.IP-1, PR.IP-3, PR.IP-12, PR.PT-1, PR.PT-3, DE.CM
    * [SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf): Tasks Requiring the Help of Security Experts 11
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Vendor Software Delivery Integrity Controls
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-02, CM-03, CM-04, CM-06, CM-14, SA-15, SA-17
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): CM-02, CM-03, CM-06
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): OM-ADM-001, SP-SYS-001; T0484, T0485, T0489, T0553; K0005, K0007, K0077, K0088, K0130, K0167, K0205, K0275; S0076, S0097, S0121, S0158; A0155

