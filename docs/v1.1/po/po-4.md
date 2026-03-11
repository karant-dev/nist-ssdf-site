---
title: 'PO.4: Define and Use Criteria for Software Security Checks'
practice_identifier: PO
task_identifier: PO.4
version: '1.1'
references:
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  TV.2-1, TV.5-1'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  SM1.4, SM2.1, SM2.2, SM2.6, SM3.3, CP2.2'
- '[EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(iv), 4e(v), 4e(ix)'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SI-1, SI-2, SVV-3'
- '[ISO27034](https://www.iso.org/standard/44378.html): 7.3.5'
- '[MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 3'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): PC3-A, DR3-B,
  IR3-B, ST3-B'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  3.3'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-15, SA-15(1)'
- '[SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.2.1, 3.2.5, 3.3.1'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-15, SA-15(1)'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0153, K0165'
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  PD.1-4, PD.1-5'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  SM1.4, SM2.1, SM2.2, SM3.4'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SI-1, SVV-1, SVV-2, SVV-3,
  SVV-4'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): PC3-B'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  2.5'
- '[SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf):
  Vendor Software Delivery Integrity Controls'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-15, SA-15(1), SA-15(11)'
- '[SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.2.5, 3.3.7'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-15, SA-15(1),
  SA-15(11)'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): T0349; K0153'
---

# PO.4: Define and Use Criteria for Software Security Checks

Help ensure that the software resulting from the SDLC meets the organization’s expectations by defining and using criteria for checking the software’s security during development.

## PO.4.1 {: #po-4-1 }

Define criteria for software security checks and track throughout the SDLC.

???+ example "Implementation Examples"
    * Example 1: Ensure that the criteria adequately indicate how effectively security risk is being managed.
    * Example 2: Define key performance indicators (KPIs), key risk indicators (KRIs), vulnerability severity scores, and other measures for software security.
    * Example 3: Add software security criteria to existing checks (e.g., the Definition of Done in agile SDLC methodologies).
    * Example 4: Review the artifacts generated as part of the software development workflow system to determine if they meet the criteria.
    * Example 5: Record security check approvals, rejections, and exception requests as part of the workflow and tracking system.
    * Example 6: Analyze collected data in the context of the security successes and failures of each development project, and use the results to improve the SDLC.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): TV.2-1, TV.5-1
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): SM1.4, SM2.1, SM2.2, SM2.6, SM3.3, CP2.2
    * [EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(iv), 4e(v), 4e(ix)
    * [IEC62443](https://webstore.iec.ch/publication/33615): SI-1, SI-2, SVV-3
    * [ISO27034](https://www.iso.org/standard/44378.html): 7.3.5
    * [MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 3
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): PC3-A, DR3-B, IR3-B, ST3-B
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 3.3
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-15, SA-15(1)
    * [SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.2.1, 3.2.5, 3.3.1
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-15, SA-15(1)
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0153, K0165

## PO.4.2 {: #po-4-2 }

Implement processes, mechanisms, etc. to gather and safeguard the necessary information in support of the criteria.

???+ example "Implementation Examples"
    * Example 1: Use the toolchain to automatically gather information that informs security decision-making.
    * Example 2: Deploy additional tools if needed to support the generation and collection of information supporting the criteria.
    * Example 3: Automate decision-making processes utilizing the criteria, and periodically review these processes.
    * Example 4: Only allow authorized personnel to access the gathered information, and prevent any alteration or deletion of the information.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): PD.1-4, PD.1-5
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): SM1.4, SM2.1, SM2.2, SM3.4
    * [EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(iv), 4e(v), 4e(ix)
    * [IEC62443](https://webstore.iec.ch/publication/33615): SI-1, SVV-1, SVV-2, SVV-3, SVV-4
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): PC3-B
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 2.5
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Vendor Software Delivery Integrity Controls
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-15, SA-15(1), SA-15(11)
    * [SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.2.5, 3.3.7
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-15, SA-15(1), SA-15(11)
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): T0349; K0153

