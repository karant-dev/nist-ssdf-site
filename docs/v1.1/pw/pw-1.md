---
title: 'PW.1: Design Software to Meet Security Requirements and Mitigate Security
  Risks'
practice_identifier: PW
task_identifier: PW.1
version: '1.1'
references:
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  SC.1'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  AM1.2, AM1.3, AM1.5, AM2.1, AM2.2, AM2.5, AM2.6, AM2.7, SFD2.2, AA1.1, AA1.2, AA1.3,
  AA2.1'
- '[EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(ix)'
- '[IDASOAR](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016):
  1'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SM-4, SR-1, SR-2, SD-1'
- '[IR8397](https://doi.org/10.6028/NIST.IR.8397): 2.1'
- '[ISO27034](https://www.iso.org/standard/44378.html): 7.3.3'
- '[MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 4'
- '[NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): ID.RA'
- '[OWASPASVS](https://github.com/OWASP/ASVS): 1.1.2, 1.2, 1.4, 1.6, 1.8, 1.9, 1.11,
  2, 3, 4, 6, 8, 9, 11, 12, 13'
- '[OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 1.6, 1.8, 2, 3, 4,
  5, 6'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): TA1-A, TA1-B,
  TA3-B, DR1-A'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  3.2, 3.3'
- '[SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf):
  Tasks Requiring the Help of Security Experts 3'
- '[SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf):
  Threat Modeling'
- '[SCTTM](https://www.safecode.org/wp-content/uploads/2017/05/SAFECode_TM_Whitepaper.pdf):
  Entire guide'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-8, SA-11(2), SA-11(6),
  SA-15(5)'
- '[SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.3.4, 3.4.5'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-8, SA-11(2), SA-11(6),
  SA-15(5)'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): T0038, T0062; K0005, K0009,
  K0038, K0039, K0070, K0080, K0119, K0147, K0149, K0151, K0152, K0160, K0161, K0162,
  K0165, K0297, K0310, K0344, K0362, K0487, K0624; S0006, S0009, S0022, S0078, S0171,
  S0229, S0248; A0092, A0093, A0107'
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  SC.1-1, PD.1-1'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  SFD3.1, SFD3.3, AA2.2, AA3.2'
- '[EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(v), 4e(ix)'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SD-1'
- '[NISTLABEL](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity):
  2.2.2.2'
- '[OWASPASVS](https://github.com/OWASP/ASVS): 1.1.3, 1.1.4'
- '[OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 1.3, 1.6'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): DR1-B'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-8, SA-10, SA-17'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-8, SA-17'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): T0256; K0005, K0038, K0039,
  K0147, K0149, K0160, K0161, K0162, K0165, K0344, K0362, K0487; S0006, S0009, S0078,
  S0171, S0229, S0248; A0092, A0107'
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  SI.2-1, SI.2-2, LO.1'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  SFD1.1, SFD2.1, SFD3.2, SR1.1, SR3.4'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SD-1, SD-4'
- '[MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 5'
- '[OWASPASVS](https://github.com/OWASP/ASVS): 1.1.6'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): SA2-A'
- '[SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf):
  Standardize Identity and Access Management; Establish Log Requirements and Audit
  Practices'
---

# PW.1: Design Software to Meet Security Requirements and Mitigate Security Risks

Identify and evaluate the security requirements for the software; determine what security risks the software is likely to face during operation and how the software’s design and architecture should mitigate those risks; and justify any cases where risk-based analysis indicates that security requirements should be relaxed or waived. Addressing security requirements and risks during software design (secure by design) is key for improving software security and also helps improve development efficiency.

## PW.1.1 {: #pw-1-1 }

Use forms of risk modeling – such as threat modeling, attack modeling, or attack surface mapping – to help assess the security risk for the software.

???+ example "Implementation Examples"
    * Example 1: Train the development team (security champions, in particular) or collaborate with a risk modeling expert to create models and analyze how to use a risk-based approach to communicate the risks and determine how to address them, including implementing mitigations.
    * Example 2: Perform more rigorous assessments for high-risk areas, such as protecting sensitive data and safeguarding identification, authentication, and access control, including credential management.
    * Example 3: Review vulnerability reports and statistics for previous software to inform the security risk assessment.
    * Example 4: Use data classification methods to identify and characterize each type of data that the software will interact with.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): SC.1
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): AM1.2, AM1.3, AM1.5, AM2.1, AM2.2, AM2.5, AM2.6, AM2.7, SFD2.2, AA1.1, AA1.2, AA1.3, AA2.1
    * [EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(ix)
    * [IDASOAR](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016): 1
    * [IEC62443](https://webstore.iec.ch/publication/33615): SM-4, SR-1, SR-2, SD-1
    * [IR8397](https://doi.org/10.6028/NIST.IR.8397): 2.1
    * [ISO27034](https://www.iso.org/standard/44378.html): 7.3.3
    * [MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 4
    * [NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): ID.RA
    * [OWASPASVS](https://github.com/OWASP/ASVS): 1.1.2, 1.2, 1.4, 1.6, 1.8, 1.9, 1.11, 2, 3, 4, 6, 8, 9, 11, 12, 13
    * [OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 1.6, 1.8, 2, 3, 4, 5, 6
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): TA1-A, TA1-B, TA3-B, DR1-A
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 3.2, 3.3
    * [SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf): Tasks Requiring the Help of Security Experts 3
    * [SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf): Threat Modeling
    * [SCTTM](https://www.safecode.org/wp-content/uploads/2017/05/SAFECode_TM_Whitepaper.pdf): Entire guide
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-8, SA-11(2), SA-11(6), SA-15(5)
    * [SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.3.4, 3.4.5
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-8, SA-11(2), SA-11(6), SA-15(5)
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): T0038, T0062; K0005, K0009, K0038, K0039, K0070, K0080, K0119, K0147, K0149, K0151, K0152, K0160, K0161, K0162, K0165, K0297, K0310, K0344, K0362, K0487, K0624; S0006, S0009, S0022, S0078, S0171, S0229, S0248; A0092, A0093, A0107

## PW.1.2 {: #pw-1-2 }

Track and maintain the software’s security requirements, risks, and design decisions.

???+ example "Implementation Examples"
    * Example 1: Record the response to each risk, including how mitigations are to be achieved and what the rationales are for any approved exceptions to the security requirements. Add any mitigations to the software’s security requirements.
    * Example 2: Maintain records of design decisions, risk responses, and approved exceptions that can be used for auditing and maintenance purposes throughout the rest of the software life cycle.
    * Example 3: Periodically re-evaluate all approved exceptions to the security requirements, and implement changes as needed.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): SC.1-1, PD.1-1
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): SFD3.1, SFD3.3, AA2.2, AA3.2
    * [EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(v), 4e(ix)
    * [IEC62443](https://webstore.iec.ch/publication/33615): SD-1
    * [ISO27034](https://www.iso.org/standard/44378.html): 7.3.3
    * [MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 4
    * [NISTLABEL](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity): 2.2.2.2
    * [OWASPASVS](https://github.com/OWASP/ASVS): 1.1.3, 1.1.4
    * [OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 1.3, 1.6
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): DR1-B
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 3.2, 3.3
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-8, SA-10, SA-17
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-8, SA-17
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): T0256; K0005, K0038, K0039, K0147, K0149, K0160, K0161, K0162, K0165, K0344, K0362, K0487; S0006, S0009, S0078, S0171, S0229, S0248; A0092, A0107

## PW.1.3 {: #pw-1-3 }

Where appropriate, build in support for using standardized security features and services (e.g., enabling software to integrate with existing log management, identity management, access control, and vulnerability management systems) instead of creating proprietary implementations of security features and services. [Formerly PW.4.3]

???+ example "Implementation Examples"
    * Example 1: Maintain one or more software repositories of modules for supporting standardized security features and services.
    * Example 2: Determine secure configurations for modules for supporting standardized security features and services, and make these configurations available (e.g., as configuration-as-code) so developers can readily use them.
    * Example 3: Define criteria for which security features and services must be supported by software to be developed.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): SI.2-1, SI.2-2, LO.1
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): SFD1.1, SFD2.1, SFD3.2, SR1.1, SR3.4
    * [EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(ix)
    * [IEC62443](https://webstore.iec.ch/publication/33615): SD-1, SD-4
    * [MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 5
    * [OWASPASVS](https://github.com/OWASP/ASVS): 1.1.6
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): SA2-A
    * [SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf): Standardize Identity and Access Management; Establish Log Requirements and Audit Practices

