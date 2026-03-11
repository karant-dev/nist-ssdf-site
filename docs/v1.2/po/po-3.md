---
title: 'PO.3: Implement Supporting Toolchains'
practice_identifier: PO
task_identifier: PO.3
version: '1.2'
references:
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  CR1.4, ST1.4, ST2.5, SE2.7'
- "[CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper):\
  \ Securing Materials\u2014Verification; Securing Build Pipelines\u2014Verification,\
  \ Automation, Secure Authentication/Access; Securing Artefacts\u2014Verification;\
  \ Securing Deployments\u2014Verification"
- '[MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 8'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): IR2-B, ST2-B'
- '[SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf):
  Tasks Requiring the Help of Security Experts 9'
- '[SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf):
  Vendor Software Delivery Integrity Controls'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-08, SA-15, SA-17, SR-09'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): CM-08, SR-09'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0013, K0178'
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  DE.2'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  SR1.1, SR1.3, SR3.4'
- "[CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper):\
  \ Securing Build Pipelines\u2014Verification, Automation, Controlled Environments,\
  \ Secure Authentication/Access; Securing Artefacts\u2014Verification, Automation,\
  \ Controlled Environments, Encryption; Securing Deployments\u2014Verification, Automation"
- '[IEC62443](https://webstore.iec.ch/publication/33615): SM-7'
- '[IR8397](https://doi.org/10.6028/NIST.IR.8397): 2.2'
- '[OWASPASVS](https://github.com/OWASP/ASVS): 1.14.3, 1.14.4, 14.1, 14.2'
- '[OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 7.9'
- '[OWASPSCVS](https://github.com/OWASP/Software-Component-Verification-Standard):
  3, 5'
- '[SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf):
  Use Current Compiler and Toolchain Versions and Secure Compiler Options'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-06, CM-08, CM-10, CM-11,
  CM-14, SA-15, SA-17, SR-09'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): CM-06, CM-08, SR-09'
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  PD.1-5'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  SM1.4, SM3.4, SR1.3'
- "[CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper):\
  \ Securing Build Pipelines\u2014Verification, Automation, Controlled Environments;\
  \ Securing Artefacts\u2014Verification"
- '[IEC62443](https://webstore.iec.ch/publication/33615): SM-12, SI-2'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): PC3-B'
- '[OWASPSCVS](https://github.com/OWASP/Software-Component-Verification-Standard):
  3.13, 3.14'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  2.5'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): AC-02, AU-03, AU-06, AU-07,
  AU-09, AU-12, CM-06, SA-15, SI-06, SI-12'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): AU-06, CM-06'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0013; T0024'
---

# PO.3: Implement Supporting Toolchains

Use automation to reduce human effort and improve the accuracy, reproducibility, usability, and comprehensiveness of security practices throughout the SDLC, as well as provide a way to document and demonstrate the use of these practices. Toolchains and tools may be used at different levels of the organization (e.g., organization-wide, project-specific) and may address a particular part of the SDLC, like a build pipeline.

## PO.3.1 {: #po-3-1 }

Specify which tools or tool types must or should be included in each toolchain to mitigate identified risks, as well as how the toolchain components are to be integrated with each other.

???+ example "Implementation Examples"
    * Example 1: Define categories of toolchains, and specify the mandatory tools or tool types to be used for each category.\nExample 2: Identify security tools to integrate into the developer toolchain.\nExample 3: Define what information is to be passed between tools and what data formats are to be used.\nExample 4: Evaluate tools' signing capabilities to create immutable records/logs for auditability within the toolchain.\nExample 5: Use automated technology for toolchain management and orchestration.

??? info "References"
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): CR1.4, ST1.4, ST2.5, SE2.7
    * [CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper): Securing Materials—Verification; Securing Build Pipelines—Verification, Automation, Secure Authentication/Access; Securing Artefacts—Verification; Securing Deployments—Verification
    * [MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 8
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): IR2-B, ST2-B
    * [SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf): Tasks Requiring the Help of Security Experts 9
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Vendor Software Delivery Integrity Controls
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-08, SA-15, SA-17, SR-09
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): CM-08, SR-09
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0013, K0178

## PO.3.2 {: #po-3-2 }

Follow recommended security practices to deploy, operate, and maintain tools and toolchains.

???+ example "Implementation Examples"
    * Example 1: Evaluate, select, and acquire tools, and assess the security of each tool.\nExample 2: Integrate tools with other tools and existing software development processes and workflows.\nExample 3: Use code-based configuration for toolchains (e.g., pipelines as code, toolchains as code).\nExample 4: Implement the technologies and processes needed for reproducible builds.\nExample 5: Update, upgrade, or replace tools as needed to address tool vulnerabilities or add new tool capabilities.\nExample 6: Continuously monitor tools and tool logs for potential operational and security issues, including policy violations and anomalous behavior.\nExample 7: Regularly verify the integrity and check the provenance of each tool to identify potential problems.\nExample 8: See PW.6 regarding compiler, interpreter, and build tools.\nExample 9: See PO.5 regarding implementing and maintaining secure environments.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): DE.2
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): SR1.1, SR1.3, SR3.4
    * [CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper): Securing Build Pipelines—Verification, Automation, Controlled Environments, Secure Authentication/Access; Securing Artefacts—Verification, Automation, Controlled Environments, Encryption; Securing Deployments—Verification, Automation
    * [IEC62443](https://webstore.iec.ch/publication/33615): SM-7
    * [IR8397](https://doi.org/10.6028/NIST.IR.8397): 2.2
    * [OWASPASVS](https://github.com/OWASP/ASVS): 1.14.3, 1.14.4, 14.1, 14.2
    * [OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 7.9
    * [OWASPSCVS](https://github.com/OWASP/Software-Component-Verification-Standard): 3, 5
    * [SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf): Tasks Requiring the Help of Security Experts 9
    * [SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf): Use Current Compiler and Toolchain Versions and Secure Compiler Options
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Vendor Software Delivery Integrity Controls
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-06, CM-08, CM-10, CM-11, CM-14, SA-15, SA-17, SR-09
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): CM-06, CM-08, SR-09
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0013, K0178

## PO.3.3 {: #po-3-3 }

Configure tools to generate artifacts of their support of secure software development practices as defined by the organization.

???+ example "Implementation Examples"
    * Example 1: Use existing tooling (e.g., workflow tracking, issue tracking, value stream mapping) to create an audit trail of the secure development-related actions that are performed for continuous improvement purposes.\nExample 2: Determine how often the collected information should be audited, and implement the necessary processes.\nExample 3: Establish and enforce security and retention policies for artifact data.\nExample 4: Assign responsibility for creating any needed artifacts that tools cannot generate.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): PD.1-5
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): SM1.4, SM3.4, SR1.3
    * [CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper): Securing Build Pipelines—Verification, Automation, Controlled Environments; Securing Artefacts—Verification
    * [IEC62443](https://webstore.iec.ch/publication/33615): SM-12, SI-2
    * [MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 8
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): PC3-B
    * [OWASPSCVS](https://github.com/OWASP/Software-Component-Verification-Standard): 3.13, 3.14
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 2.5
    * [SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf): Tasks Requiring the Help of Security Experts 9
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Vendor Software Delivery Integrity Controls
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): AC-02, AU-03, AU-06, AU-07, AU-09, AU-12, CM-06, SA-15, SI-06, SI-12
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): AU-06, CM-06
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0013; T0024

