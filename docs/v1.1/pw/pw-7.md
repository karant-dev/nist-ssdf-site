---
title: 'PW.7: Review and/or Analyze Human-Readable Code to Identify Vulnerabilities
  and Verify Compliance with Security Requirements'
practice_identifier: PW
task_identifier: PW.7
version: '1.1'
references:
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  CR1.5'
- '[EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(iv), 4e(ix)'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SM-5, SI-1, SVV-1'
- '[NISTLABEL](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity):
  2.2.2.2'
- '[SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf):
  Peer Reviews and Security Testing'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-11'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-11'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-002; K0013, K0039,
  K0070, K0153, K0165; S0174'
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  TV.2, PD.1-4'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  CR1.2, CR1.4, CR1.6, CR2.6, CR2.7, CR3.4, CR3.5'
- '[EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(iv), 4e(v), 4e(ix)'
- '[IDASOAR](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016):
  3, 4, 5, 14, 15, 48'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SI-1, SVV-1, SVV-2'
- '[IR8397](https://doi.org/10.6028/NIST.IR.8397): 2.3, 2.4'
- '[ISO27034](https://www.iso.org/standard/44378.html): 7.3.6'
- '[MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 9, 10'
- '[OWASPASVS](https://github.com/OWASP/ASVS): 1.1.7, 10'
- '[OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 7.5'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): IR1-B, IR2-A,
  IR2-B, IR3-A'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  3.2, 4.1'
- '[SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf):
  Operational Security Tasks 4, 7; Tasks Requiring the Help of Security Experts 10'
- '[SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf):
  Use Code Analysis Tools to Find Security Issues Early, Use Static Analysis Security
  Testing Tools, Perform Manual Verification of Security Features/Mitigations'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-11, SA-11(1), SA-11(4),
  SA-15(7)'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-11, SA-11(1),
  SA-11(4), SA-15(7)'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-001, SP-DEV-002; T0013,
  T0111, T0176, T0267, T0516; K0009, K0039, K0070, K0140, K0624; S0019, S0060, S0078,
  S0137, S0149, S0167, S0174, S0242, S0266; A0007, A0015, A0036, A0044, A0047'
---

# PW.7: Review and/or Analyze Human-Readable Code to Identify Vulnerabilities and Verify Compliance with Security Requirements

Help identify vulnerabilities so that they can be corrected before the software is released to prevent exploitation. Using automated methods lowers the effort and resources needed to detect vulnerabilities. Human-readable code includes source code, scripts, and any other form of code that an organization deems human-readable.

## PW.7.1 {: #pw-7-1 }

Determine whether code review (a person looks directly at the code to find issues) and/or code analysis (tools are used to find issues in code, either in a fully automated way or in conjunction with a person) should be used, as defined by the organization.

???+ example "Implementation Examples"
    * Example 1: Follow the organization’s policies or guidelines for when code review should be performed and how it should be conducted. This may include third-party code and reusable code modules written in-house.
    * Example 2: Follow the organization’s policies or guidelines for when code analysis should be performed and how it should be conducted.
    * Example 3: Choose code review and/or analysis methods based on the stage of the software.

??? info "References"
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): CR1.5
    * [EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(iv), 4e(ix)
    * [IEC62443](https://webstore.iec.ch/publication/33615): SM-5, SI-1, SVV-1
    * [NISTLABEL](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity): 2.2.2.2
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Peer Reviews and Security Testing
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-11
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-11
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-002; K0013, K0039, K0070, K0153, K0165; S0174

## PW.7.2 {: #pw-7-2 }

Perform the code review and/or code analysis based on the organization’s secure coding standards, and record and triage all discovered issues and recommended remediations in the development team’s workflow or issue tracking system.

???+ example "Implementation Examples"
    * Example 1: Perform peer review of code, and review any existing code review, analysis, or testing results as part of the peer review.
    * Example 2: Use expert reviewers to check code for backdoors and other malicious content.
    * Example 3: Use peer reviewing tools that facilitate the peer review process, and document all discussions and other feedback.
    * Example 4: Use a static analysis tool to automatically check code for vulnerabilities and compliance with the organization’s secure coding standards with a human reviewing the issues reported by the tool and remediating them as necessary.
    * Example 5: Use review checklists to verify that the code complies with the requirements.
    * Example 6: Use automated tools to identify and remediate documented and verified unsafe software practices on a continuous basis as human-readable code is checked into the code repository.
    * Example 7: Identify and document the root causes of discovered issues.
    * Example 8: Document lessons learned from code review and analysis in a wiki that developers can access and search.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): TV.2, PD.1-4
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): CR1.2, CR1.4, CR1.6, CR2.6, CR2.7, CR3.4, CR3.5
    * [EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(iv), 4e(v), 4e(ix)
    * [IDASOAR](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016): 3, 4, 5, 14, 15, 48
    * [IEC62443](https://webstore.iec.ch/publication/33615): SI-1, SVV-1, SVV-2
    * [IR8397](https://doi.org/10.6028/NIST.IR.8397): 2.3, 2.4
    * [ISO27034](https://www.iso.org/standard/44378.html): 7.3.6
    * [MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 9, 10
    * [NISTLABEL](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity): 2.2.2.2
    * [OWASPASVS](https://github.com/OWASP/ASVS): 1.1.7, 10
    * [OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 7.5
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): IR1-B, IR2-A, IR2-B, IR3-A
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 3.2, 4.1
    * [SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf): Operational Security Tasks 4, 7; Tasks Requiring the Help of Security Experts 10
    * [SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf): Use Code Analysis Tools to Find Security Issues Early, Use Static Analysis Security Testing Tools, Perform Manual Verification of Security Features/Mitigations
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Peer Reviews and Security Testing
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-11, SA-11(1), SA-11(4), SA-15(7)
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-11, SA-11(1), SA-11(4), SA-15(7)
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-001, SP-DEV-002; T0013, T0111, T0176, T0267, T0516; K0009, K0039, K0070, K0140, K0624; S0019, S0060, S0078, S0137, S0149, S0167, S0174, S0242, S0266; A0007, A0015, A0036, A0044, A0047

