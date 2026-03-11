---
title: 'PS.1: Protect All Forms of Code from Unauthorized Access and Tampering'
practice_identifier: PS
task_identifier: PS.1
version: '1.2'
references:
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  IA.1, IA.2, SM.4-1, DE.1-2'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  SE2.4'
- "[CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper):\
  \ Securing the Source Code\u2014Verification, Automation, Controlled Environments,\
  \ Secure Authentication; Securing Materials\u2014Automation"
- '[IDASoar](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016):
  Fact Sheet 25'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SM-6, SM-7, SM-8'
- '[NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): PR.AC-4, PR.DS-6, PR.IP-3'
- '[OWASPASVS](https://github.com/OWASP/ASVS): 1.10, 10.3.2'
- '[OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 7.1'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): OE3-B'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  5.1, 6.1'
- '[SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf):
  Vendor Software Delivery Integrity Controls, Vendor Software Development Integrity
  Controls'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): AC-03, AC-06, CM-05, SA-10,
  SC-12, SC-28, SI-12'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): AC-03, SC-28'
---

# PS.1: Protect All Forms of Code from Unauthorized Access and Tampering

Help prevent unauthorized changes to code, both inadvertent and intentional, which could circumvent or negate the intended security characteristics of the software. For code that is not intended to be publicly accessible, this helps prevent the theft of the software and may make it more difficult or time-consuming for attackers to find vulnerabilities in the software.

## PS.1.1 {: #ps-1-1 }

Store all forms of code – including source code, executable code, and configuration as code – based on the principle of least privilege so that only authorized personnel, tools, and services have access.

???+ example "Implementation Examples"
    * Example 1: Store all source code and configuration as code in a code repository, and restrict access to it based on the nature of the code. For example, open-source code intended for public access may need its integrity and availability protected; other code may also need its confidentiality protected.\nExample 2: Use version control features of the repository to track all changes made to the code with accountability to the individual account.\nExample 3: Use commit signing for code repositories.\nExample 4: Have the code owner review and approve all changes made to the code by others.\nExample 5: Use code signing to help protect the integrity of executables.\nExample 6: Use cryptography (e.g., cryptographic hashes) to help protect file integrity.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): IA.1, IA.2, SM.4-1, DE.1-2
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): SE2.4
    * [CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper): Securing the Source Code—Verification, Automation, Controlled Environments, Secure Authentication; Securing Materials—Automation
    * [IDASoar](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016): Fact Sheet 25
    * [IEC62443](https://webstore.iec.ch/publication/33615): SM-6, SM-7, SM-8
    * [NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): PR.AC-4, PR.DS-6, PR.IP-3
    * [OWASPASVS](https://github.com/OWASP/ASVS): 1.10, 10.3.2
    * [OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 7.1
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): OE3-B
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 5.1, 6.1
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Vendor Software Delivery Integrity Controls, Vendor Software Development Integrity Controls
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): AC-03, AC-06, CM-05, SA-10, SC-12, SC-28, SI-12
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): AC-03, SC-28

