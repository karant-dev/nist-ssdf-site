---
title: 'RV.3: Analyze Vulnerabilities to Identify Their Root Causes'
practice_identifier: RV
task_identifier: RV.3
version: '1.1'
references:
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  VM.2-1'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  CMVM3.1, CMVM3.2'
- '[EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(ix)'
- '[IEC62443](https://webstore.iec.ch/publication/33615): DM-3'
- '[ISO30111](https://www.iso.org/standard/69725.html): 7.1.4'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): IM3-A'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  4.2'
- '[SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf):
  Secure Development Lifecycle Feedback'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): T0047, K0009, K0039, K0070,
  K0343'
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  VM.2-1, PD.1-3'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  CP3.3, CMVM3.2'
- '[IEC62443](https://webstore.iec.ch/publication/33615): DM-4'
- '[ISO30111](https://www.iso.org/standard/69725.html): 7.1.7'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): IM3-B'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  2.6, 4.2'
- '[SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.3.8'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): T0111, K0009, K0039, K0070,
  K0343'
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  VM.2'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  CR3.3, CMVM3.1'
- '[EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(iv), 4e(viii),
  4e(ix)'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SI-1, DM-3, DM-4'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-11'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-11'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-001, SP-DEV-002; K0009,
  K0039, K0070'
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  PD.1-3'
- '[IEC62443](https://webstore.iec.ch/publication/33615): DM-6'
- '[MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 2'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-15'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-15'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0009, K0039, K0070'
---

# RV.3: Analyze Vulnerabilities to Identify Their Root Causes

Help reduce the frequency of vulnerabilities in the future.

## RV.3.1 {: #rv-3-1 }

Analyze identified vulnerabilities to determine their root causes.

???+ example "Implementation Examples"
    * Example 1: Record the root cause of discovered issues.
    * Example 2: Record lessons learned through root cause analysis in a wiki that developers can access and search.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): VM.2-1
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): CMVM3.1, CMVM3.2
    * [EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(ix)
    * [IEC62443](https://webstore.iec.ch/publication/33615): DM-3
    * [ISO30111](https://www.iso.org/standard/69725.html): 7.1.4
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): IM3-A
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 4.2
    * [SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf): Secure Development Lifecycle Feedback
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): T0047, K0009, K0039, K0070, K0343

## RV.3.2 {: #rv-3-2 }

Analyze the root causes over time to identify patterns, such as a particular secure coding practice not being followed consistently.

???+ example "Implementation Examples"
    * Example 1: Record lessons learned through root cause analysis in a wiki that developers can access and search.
    * Example 2: Add mechanisms to the toolchain to automatically detect future instances of the root cause.
    * Example 3: Update manual processes to detect future instances of the root cause.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): VM.2-1, PD.1-3
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): CP3.3, CMVM3.2
    * [EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(ix)
    * [IEC62443](https://webstore.iec.ch/publication/33615): DM-4
    * [ISO30111](https://www.iso.org/standard/69725.html): 7.1.7
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): IM3-B
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 2.6, 4.2
    * [SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf): Secure Development Lifecycle Feedback
    * [SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.3.8
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): T0111, K0009, K0039, K0070, K0343

## RV.3.3 {: #rv-3-3 }

Review the software for similar vulnerabilities to eradicate a class of vulnerabilities, and proactively fix them rather than waiting for external reports.

???+ example "Implementation Examples"
    * Example 1: See PW.7 and PW.8.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): VM.2
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): CR3.3, CMVM3.1
    * [EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(iv), 4e(viii), 4e(ix)
    * [IEC62443](https://webstore.iec.ch/publication/33615): SI-1, DM-3, DM-4
    * [ISO30111](https://www.iso.org/standard/69725.html): 7.1.4
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 4.2
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-11
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-11
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-001, SP-DEV-002; K0009, K0039, K0070

## RV.3.4 {: #rv-3-4 }

Review the SDLC process, and update it if appropriate to prevent (or reduce the likelihood of) the root cause recurring in updates to the software or in new software that is created.

???+ example "Implementation Examples"
    * Example 1: Record lessons learned through root cause analysis in a wiki that developers can access and search.
    * Example 2: Plan and implement changes to the appropriate SDLC practices.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): PD.1-3
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): CP3.3, CMVM3.2
    * [EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(ix)
    * [IEC62443](https://webstore.iec.ch/publication/33615): DM-6
    * [ISO30111](https://www.iso.org/standard/69725.html): 7.1.7
    * [MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 2
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 2.6, 4.2
    * [SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf): Secure Development Lifecycle Feedback
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-15
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-15
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0009, K0039, K0070

