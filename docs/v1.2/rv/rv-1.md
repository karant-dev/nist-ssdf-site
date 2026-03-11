---
title: 'RV.1: Identify and Confirm Vulnerabilities on an Ongoing Basis'
practice_identifier: RV
task_identifier: RV.1
version: '1.2'
references:
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  VM.1-3, VM.3'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  AM1.5, CMVM1.2, CMVM2.1, CMVM3.4, CMVM3.7'
- "[CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper):\
  \ Securing Materials\u2014Verification"
- '[IEC62443](https://webstore.iec.ch/publication/33615): DM-1, DM-2, DM-3'
- '[ISO29147](https://www.iso.org/standard/72311.html): 6.2.1, 6.2.2, 6.2.4, 6.3,
  6.5'
- '[ISO30111](https://www.iso.org/standard/53231.html): 7.1.3'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): IM1-A, IM2-B,
  EH1-B'
- '[OWASPSCVS](https://github.com/OWASP/Software-Component-Verification-Standard):
  4'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  3.4, 4.1, 9.1'
- '[SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf):
  Operational Security Task 5'
- '[SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf):
  Vulnerability Response and Disclosure'
- '[SCTPC](https://www.safecode.org/wp-content/uploads/2017/05/SAFECode_TPC_Whitepaper.pdf):
  MONITOR1'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): RA-05, SA-10, SI-05, SR-03,
  SR-04'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SR-04'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0009, K0038, K0040, K0070,
  K0161, K0362; S0078'
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  VM.1-2, VM.2-1'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  CMVM3.1'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SI-1, SVV-2, SVV-3, SVV-4,
  DM-1, DM-2'
- '[ISO27034](https://www.iso.org/standard/44378.html): 7.3.6'
- '[ISO29147](https://www.iso.org/standard/72311.html): 6.4'
- '[ISO30111](https://www.iso.org/standard/53231.html): 7.1.4'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  3.4, 4.1'
- '[SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf):
  Operational Security Tasks 10, 11'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-06, RA-05, SA-11, SI-07'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-002; K0009, K0039,
  K0153'
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  VM.1-1, VM.2'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  CMVM1.1, CMVM2.1, CMVM3.3, CMVM3.7'
- '[IEC62443](https://webstore.iec.ch/publication/33615): DM-1, DM-2, DM-3, DM-4,
  DM-5'
- '[ISO29147](https://www.iso.org/standard/72311.html): All'
- '[ISO30111](https://www.iso.org/standard/53231.html): All'
- '[MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 12'
- '[NISTLABEL](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity):
  2.2.2.3'
- '[OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 1.11'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): IM1-A, IM1-B,
  IM2-A, IM2-B'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  9.2, 9.3'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): AC-02, AC-03, CM-09, IR-01,
  IR-08, RA-05, RA-05(11), SA-15, SA-15(10)'
- '[SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.3.8'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0041, K0042, K0151, K0292,
  K0317; S0054; A0025'
- '[SP800216](https://doi.org/10.6028/NIST.SP.800-216): All'
---

# RV.1: Identify and Confirm Vulnerabilities on an Ongoing Basis

Help ensure that vulnerabilities are identified more quickly so that they can be remediated more quickly in accordance with risk, reducing the window of opportunity for attackers.

## RV.1.1 {: #rv-1-1 }

Gather information from software acquirers, users, and public sources on potential vulnerabilities in the software and third-party components that the software uses, and investigate all credible reports.

???+ example "Implementation Examples"
    * Example 1: Monitor vulnerability databases, security mailing lists, and other sources of vulnerability reports through manual or automated means.\nExample 2: Use threat intelligence sources to better understand how vulnerabilities in general are being exploited.\nExample 3: Automatically review provenance and software composition data for all software components to identify any new vulnerabilities they have.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): VM.1-3, VM.3
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): AM1.5, CMVM1.2, CMVM2.1, CMVM3.4, CMVM3.7
    * [CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper): Securing Materials—Verification
    * [IEC62443](https://webstore.iec.ch/publication/33615): DM-1, DM-2, DM-3
    * [ISO29147](https://www.iso.org/standard/72311.html): 6.2.1, 6.2.2, 6.2.4, 6.3, 6.5
    * [ISO30111](https://www.iso.org/standard/53231.html): 7.1.3
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): IM1-A, IM2-B, EH1-B
    * [OWASPSCVS](https://github.com/OWASP/Software-Component-Verification-Standard): 4
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 3.4, 4.1, 9.1
    * [SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf): Operational Security Task 5
    * [SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf): Vulnerability Response and Disclosure
    * [SCTPC](https://www.safecode.org/wp-content/uploads/2017/05/SAFECode_TPC_Whitepaper.pdf): MONITOR1
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): RA-05, SA-10, SI-05, SR-03, SR-04
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SR-04
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0009, K0038, K0040, K0070, K0161, K0362; S0078

## RV.1.2 {: #rv-1-2 }

Review, analyze, and/or test the software's code and its default and other common configurations to identify or confirm the presence of previously undetected vulnerabilities.

???+ example "Implementation Examples"
    * Example 1: Configure the toolchain to perform automated code analysis and testing on a regular or continuous basis for all supported releases.\nExample 2: See PW.7 and PW.8.\nExample 3: Monitor customer issues to determine whether default configurations should be updated and whether alerts should be added to the software to warn customers about insecure configurations.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): VM.1-2, VM.2-1
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): CMVM3.1
    * [IEC62443](https://webstore.iec.ch/publication/33615): SI-1, SVV-2, SVV-3, SVV-4, DM-1, DM-2
    * [ISO27034](https://www.iso.org/standard/44378.html): 7.3.6
    * [ISO29147](https://www.iso.org/standard/72311.html): 6.4
    * [ISO30111](https://www.iso.org/standard/53231.html): 7.1.4
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 3.4, 4.1
    * [SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf): Operational Security Tasks 10, 11
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-06, RA-05, SA-11, SI-07
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-002; K0009, K0039, K0153

## RV.1.3 {: #rv-1-3 }

Have a policy that addresses vulnerability disclosure and remediation, and implement the roles, responsibilities, and processes needed to support that policy.

???+ example "Implementation Examples"
    * Example 1: Establish a vulnerability disclosure program, and make it easy for security researchers to learn about the program and report possible vulnerabilities.\nExample 2: Have a Product Security Incident Response Team (PSIRT) and processes in place to handle the responses to vulnerability reports and incidents, including communications plans for all stakeholders.\nExample 3: Have a security response playbook to handle a generic reported vulnerability, a report of zero days, a vulnerability being exploited in the wild, and a major ongoing incident involving multiple parties and open-source software components.\nExample 4: Periodically conduct exercises of the product security incident response processes.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): VM.1-1, VM.2
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): CMVM1.1, CMVM2.1, CMVM3.3, CMVM3.7
    * [IEC62443](https://webstore.iec.ch/publication/33615): DM-1, DM-2, DM-3, DM-4, DM-5
    * [ISO29147](https://www.iso.org/standard/72311.html): All
    * [ISO30111](https://www.iso.org/standard/53231.html): All
    * [MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 12
    * [NISTLABEL](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity): 2.2.2.3
    * [OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 1.11
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): IM1-A, IM1-B, IM2-A, IM2-B
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 9.2, 9.3
    * [SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf): Vulnerability Response and Disclosure
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): AC-02, AC-03, CM-09, IR-01, IR-08, RA-05, RA-05(11), SA-15, SA-15(10)
    * [SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.3.8
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0041, K0042, K0151, K0292, K0317; S0054; A0025
    * [SP800216](https://doi.org/10.6028/NIST.SP.800-216): All

