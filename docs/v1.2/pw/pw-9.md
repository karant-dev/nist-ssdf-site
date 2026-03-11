---
title: 'PW.9: Configure Software to Have Secure Settings by Default'
practice_identifier: PW
task_identifier: PW.9
version: '1.2'
references:
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  CF.1'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  SE2.2'
- '[IDASoar](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016):
  23'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SD-4, SVV-1, SG-1'
- '[ISO27034](https://www.iso.org/standard/44378.html): 7.3.5'
- '[SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf):
  Tasks Requiring the Help of Security Experts 12'
- '[SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf):
  Vendor Software Delivery Integrity Controls, Vendor Software Development Integrity
  Controls'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-02, CM-06, CM-09'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-002; K0009, K0039,
  K0073, K0153, K0165, K0275, K0531; S0167'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SG-3'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): OE1-A'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  8.1, 8.2'
- '[SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf):
  Verify Secure Configurations and Use of Platform Mitigation'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): AC-02, AC-03, CM-02, CM-06,
  SA-05, SA-08, SA-08(23)'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): CM-02, CM-06'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-001; K0009, K0039,
  K0073, K0153, K0165, K0275, K0531'
---

# PW.9: Configure Software to Have Secure Settings by Default

Help improve the security of the software at the time of installation to reduce the likelihood of the software being deployed with weak security settings, putting it at greater risk of compromise.

## PW.9.1 {: #pw-9-1 }

Define a secure baseline by determining how to configure each setting that has an effect on security or a security-related setting so that the default settings are secure and do not weaken the security functions provided by the platform, network infrastructure, or services.

???+ example "Implementation Examples"
    * Example 1: Conduct testing to ensure that the settings, including the default settings, are working as expected and are not inadvertently causing any security weaknesses, operational issues, or other problems.\nExample 2: Prohibit the use of default passwords or hard-coded secrets and protection mechanisms.\nExample 3: Make available a robust range of settings with secure default values that enable software administrators to control logging capabilities (e.g., changes to configuration, security events, safety events) and how long log entries are retained.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): CF.1
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): SE2.2
    * [IDASoar](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016): 23
    * [IEC62443](https://webstore.iec.ch/publication/33615): SD-4, SVV-1, SG-1
    * [ISO27034](https://www.iso.org/standard/44378.html): 7.3.5
    * [SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf): Tasks Requiring the Help of Security Experts 12
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Vendor Software Delivery Integrity Controls, Vendor Software Development Integrity Controls
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-02, CM-06, CM-09
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-002; K0009, K0039, K0073, K0153, K0165, K0275, K0531; S0167

## PW.9.2 {: #pw-9-2 }

Implement the default settings (or groups of default settings, if applicable), and document each setting for software administrators.

???+ example "Implementation Examples"
    * Example 1: Verify that the approved configuration is in place for the software.\nExample 2: Document each setting's purpose, options, default value, security relevance, potential operational impact, and relationships with other settings.\nExample 3: Use authoritative programmatic technical mechanisms to record how each setting can be implemented and assessed by software administrators.\nExample 4: Store the default configuration in a usable format and follow change control practices for modifying it (e.g., configuration as code).

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): CF.1
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): SE2.2
    * [IDASoar](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016): 23
    * [IEC62443](https://webstore.iec.ch/publication/33615): SG-3
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): OE1-A
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 8.1, 8.2
    * [SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf): Tasks Requiring the Help of Security Experts 12
    * [SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf): Verify Secure Configurations and Use of Platform Mitigation
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Vendor Software Delivery Integrity Controls, Vendor Software Development Integrity Controls
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): AC-02, AC-03, CM-02, CM-06, SA-05, SA-08, SA-08(23)
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): CM-02, CM-06
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-001; K0009, K0039, K0073, K0153, K0165, K0275, K0531

