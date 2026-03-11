---
title: 'PW.6: Configure the Compilation, Interpreter, and Build Processes to Improve
  Executable Security'
practice_identifier: PW
task_identifier: PW.6
version: '1.2'
references:
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  DE.2-1'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  SE2.4'
- "[CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper):\
  \ Securing Build Pipelines\u2014Verification, Automation"
- '[IEC62443](https://webstore.iec.ch/publication/33615): SI-2'
- '[MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 8'
- '[SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf):
  Operational Security Task 3'
- '[SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf):
  Use Current Compiler and Toolchain Versions and Secure Compiler Options'
- '[SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf):
  Vendor Software Development Integrity Controls'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-09, SA-15'
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  DE.2-3, DE.2-4, DE.2-5'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  SE2.4, SE3.2'
- '[IR8397](https://doi.org/10.6028/NIST.IR.8397): 2.5'
- '[OWASPASVS](https://github.com/OWASP/ASVS): 14.1, 14.2.1'
- '[OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 7.2'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  3.2'
- '[SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf):
  Operational Security Task 8'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-02, CM-09, SA-15, SC-38,
  SR-09'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SR-09'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0039, K0070'
---

# PW.6: Configure the Compilation, Interpreter, and Build Processes to Improve Executable Security

Decrease the number of security vulnerabilities in the software and reduce costs by eliminating vulnerabilities before testing occurs.

## PW.6.1 {: #pw-6-1 }

Use compiler, interpreter, and build tools that offer features to improve executable security.

???+ example "Implementation Examples"
    * Example 1: Use up-to-date versions of compiler, interpreter, and build tools.\nExample 2: Follow change management processes when deploying or updating compiler, interpreter, and build tools, and audit all unexpected changes to tools.\nExample 3: Regularly validate the authenticity and integrity of compiler, interpreter, and build tools. See PO.3.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): DE.2-1
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): SE2.4
    * [CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper): Securing Build Pipelines—Verification, Automation
    * [IEC62443](https://webstore.iec.ch/publication/33615): SI-2
    * [MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 8
    * [SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf): Operational Security Task 3
    * [SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf): Use Current Compiler and Toolchain Versions and Secure Compiler Options
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Vendor Software Development Integrity Controls
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-09, SA-15

## PW.6.2 {: #pw-6-2 }

Determine which compiler, interpreter, and build tool features should be used and how each should be configured, then implement and use the approved configurations.

???+ example "Implementation Examples"
    * Example 1: Enable compiler features that produce warnings for poorly secured code during the compilation process.\nExample 2: Implement the "clean build" concept, where all compiler warnings are treated as errors and eliminated except those determined to be false positives or irrelevant.\nExample 3: Perform all builds in a dedicated, highly controlled build environment.\nExample 4: Enable compiler features that randomize or obfuscate execution characteristics, such as memory location usage, that would otherwise be predictable and thus potentially exploitable.\nExample 5: Test to ensure that the features are working as expected and are not inadvertently causing any operational issues or other problems.\nExample 6: Continuously verify that the approved configurations are being used.\nExample 7: Make the approved tool configurations available as configuration-as-code so developers can readily use them.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): DE.2-3, DE.2-4, DE.2-5
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): SE2.4, SE3.2
    * [CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper): Securing Build Pipelines—Verification, Automation
    * [IEC62443](https://webstore.iec.ch/publication/33615): SI-2
    * [IR8397](https://doi.org/10.6028/NIST.IR.8397): 2.5
    * [MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 8
    * [OWASPASVS](https://github.com/OWASP/ASVS): 14.1, 14.2.1
    * [OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 7.2
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 3.2
    * [SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf): Operational Security Task 8
    * [SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf): Use Current Compiler and Toolchain Versions and Secure Compiler Options
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Vendor Software Development Integrity Controls
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-02, CM-09, SA-15, SC-38, SR-09
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SR-09
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0039, K0070

