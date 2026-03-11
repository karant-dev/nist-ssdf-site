---
title: 'PW.8: Test Executable Code to Identify Vulnerabilities and Verify Compliance
  with Security Requirements'
practice_identifier: PW
task_identifier: PW.8
version: '1.1'
references:
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  TV.3'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  PT2.3'
- '[EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(ix)'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SVV-1, SVV-2, SVV-3, SVV-4,
  SVV-5'
- '[NISTLABEL](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity):
  2.2.2.2'
- '[SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf):
  Peer Reviews and Security Testing'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-11'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-11'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-001, SP-DEV-002; T0456;
  K0013, K0039, K0070, K0153, K0165, K0342, K0367, K0536, K0624; S0001, S0015, S0026,
  S0061, S0083, S0112, S0135'
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  TV.3, TV.5, PD.1-4'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  ST1.1, ST1.3, ST1.4, ST2.4, ST2.5, ST2.6, ST3.3, ST3.4, ST3.5, ST3.6, PT1.1, PT1.2,
  PT1.3, PT3.1'
- '[EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(iv), 4e(v), 4e(ix)'
- '[IDASOAR](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016):
  7, 8, 10, 11, 38, 39, 43, 44, 48, 55, 56, 57'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SM-5, SM-13, SI-1, SVV-1,
  SVV-2, SVV-3, SVV-4, SVV-5'
- '[IR8397](https://doi.org/10.6028/NIST.IR.8397): 2.6, 2.7, 2.8, 2.9, 2.10, 2.11'
- '[ISO27034](https://www.iso.org/standard/44378.html): 7.3.6'
- '[MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 10, 11'
- '[OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 7.5'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): ST1-A, ST1-B,
  ST2-A, ST2-B, ST3-A'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  4.1'
- '[SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf):
  Operational Security Tasks 10, 11; Tasks Requiring the Help of Security Experts
  4, 5, 6, 7'
- '[SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf):
  Perform Dynamic Analysis Security Testing, Fuzz Parsers, Network Vulnerability Scanning,
  Perform Automated Functional Testing of Security Features/Mitigations, Perform Penetration
  Testing'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-11, SA-11(5), SA-11(8),
  SA-15(7)'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-11, SA-11(5),
  SA-11(8), SA-15(7)'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-001, SP-DEV-002; T0013,
  T0028, T0169, T0176, T0253, T0266, T0456, T0516; K0009, K0039, K0070, K0272, K0339,
  K0342, K0362, K0536, K0624; S0001, S0015, S0046, S0051, S0078, S0081, S0083, S0135,
  S0137, S0167, S0242; A0015'
---

# PW.8: Test Executable Code to Identify Vulnerabilities and Verify Compliance with Security Requirements

Help identify vulnerabilities so that they can be corrected before the software is released in order to prevent exploitation. Using automated methods lowers the effort and resources needed to detect vulnerabilities and improves traceability and repeatability. Executable code includes binaries, directly executed bytecode and source code, and any other form of code that an organization deems executable.

## PW.8.1 {: #pw-8-1 }

Determine whether executable code testing should be performed to find vulnerabilities not identified by previous reviews, analysis, or testing and, if so, which types of testing should be used.

???+ example "Implementation Examples"
    * Example 1: Follow the organization’s policies or guidelines for when code testing should be performed and how it should be conducted (e.g., within a sandboxed environment). This may include third-party executable code and reusable executable code modules written in-house.
    * Example 2: Choose testing methods based on the stage of the software.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): TV.3
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): PT2.3
    * [EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(ix)
    * [IEC62443](https://webstore.iec.ch/publication/33615): SVV-1, SVV-2, SVV-3, SVV-4, SVV-5
    * [NISTLABEL](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity): 2.2.2.2
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Peer Reviews and Security Testing
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-11
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-11
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-001, SP-DEV-002; T0456; K0013, K0039, K0070, K0153, K0165, K0342, K0367, K0536, K0624; S0001, S0015, S0026, S0061, S0083, S0112, S0135

## PW.8.2 {: #pw-8-2 }

Scope the testing, design the tests, perform the testing, and document the results, including recording and triaging all discovered issues and recommended remediations in the development team’s workflow or issue tracking system.

???+ example "Implementation Examples"
    * Example 1: Perform robust functional testing of security features.
    * Example 2: Integrate dynamic vulnerability testing into the project’s automated test suite.
    * Example 3: Incorporate tests for previously reported vulnerabilities into the project’s test suite to ensure that errors are not reintroduced.
    * Example 4: Take into consideration the infrastructures and technology stacks that the software will be used with in production when developing test plans.
    * Example 5: Use fuzz testing tools to find issues with input handling.
    * Example 6: If resources are available, use penetration testing to simulate how an attacker might attempt to compromise the software in high-risk scenarios.
    * Example 7: Identify and record the root causes of discovered issues.
    * Example 8: Document lessons learned from code testing in a wiki that developers can access and search.
    * Example 9: Use source code, design records, and other resources when developing test plans.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): TV.3, TV.5, PD.1-4
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): ST1.1, ST1.3, ST1.4, ST2.4, ST2.5, ST2.6, ST3.3, ST3.4, ST3.5, ST3.6, PT1.1, PT1.2, PT1.3, PT3.1
    * [EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(iv), 4e(v), 4e(ix)
    * [IDASOAR](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016): 7, 8, 10, 11, 38, 39, 43, 44, 48, 55, 56, 57
    * [IEC62443](https://webstore.iec.ch/publication/33615): SM-5, SM-13, SI-1, SVV-1, SVV-2, SVV-3, SVV-4, SVV-5
    * [IR8397](https://doi.org/10.6028/NIST.IR.8397): 2.6, 2.7, 2.8, 2.9, 2.10, 2.11
    * [ISO27034](https://www.iso.org/standard/44378.html): 7.3.6
    * [MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 10, 11
    * [NISTLABEL](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity): 2.2.2.2
    * [OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 7.5
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): ST1-A, ST1-B, ST2-A, ST2-B, ST3-A
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 4.1
    * [SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf): Operational Security Tasks 10, 11; Tasks Requiring the Help of Security Experts 4, 5, 6, 7
    * [SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf): Perform Dynamic Analysis Security Testing, Fuzz Parsers, Network Vulnerability Scanning, Perform Automated Functional Testing of Security Features/Mitigations, Perform Penetration Testing
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Peer Reviews and Security Testing
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-11, SA-11(5), SA-11(8), SA-15(7)
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-11, SA-11(5), SA-11(8), SA-15(7)
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-001, SP-DEV-002; T0013, T0028, T0169, T0176, T0253, T0266, T0456, T0516; K0009, K0039, K0070, K0272, K0339, K0342, K0362, K0536, K0624; S0001, S0015, S0046, S0051, S0078, S0081, S0083, S0135, S0137, S0167, S0242; A0015

