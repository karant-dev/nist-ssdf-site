---
title: 'PS.3: Archive and Protect Each Software Release'
practice_identifier: PS
task_identifier: PS.3
version: '1.1'
references:
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  PD.1-5, DE.1-2, IA.2'
- "[CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper):\
  \ Securing Artefacts\u2014Automation, Controlled Environments, Encryption; Securing\
  \ Deployments\u2014Verification"
- '[EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(iii), 4e(vi),
  4e(ix), 4e(x)'
- '[IDASOAR](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016):
  25'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SM-6, SM-7'
- '[NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): PR.IP-4'
- '[OWASPSCVS](https://github.com/OWASP/Software-Component-Verification-Standard):
  1, 3.18, 3.19, 6.3'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  5.2, 6.1, 6.2'
- '[SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf):
  Vendor Software Delivery Integrity Controls'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-10, SA-15, SA-15(11), SR-4'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-8, SA-10, SA-15(11),
  SR-4'
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  SM.2'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  SE3.6'
- "[CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper):\
  \ Securing Materials\u2014Verification, Automation"
- '[EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(vi), 4e(vii),
  4e(ix), 4e(x)'
- '[NTIASBOM](https://www.ntia.doc.gov/report/2021/minimum-elements-software-bill-materials-sbom):
  All'
- '[OWASPSCVS](https://github.com/OWASP/Software-Component-Verification-Standard):
  1.4, 2'
- '[SCTPC](https://www.safecode.org/wp-content/uploads/2017/05/SAFECode_TPC_Whitepaper.pdf):
  MAINTAIN3'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-8, SR-3, SR-4'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-8, SR-3, SR-4'
---

# PS.3: Archive and Protect Each Software Release

Preserve software releases in order to help identify, analyze, and eliminate vulnerabilities discovered in the software after release.

## PS.3.1 {: #ps-3-1 }

Securely archive the necessary files and supporting data (e.g., integrity verification information, provenance data) to be retained for each software release.

???+ example "Implementation Examples"
    * Example 1: Store the release files, associated images, etc. in repositories following the organization’s established policy. Allow read-only access to them by necessary personnel and no access by anyone else.
    * Example 2: Store and protect release integrity verification information and provenance data, such as by keeping it in a separate location from the release files or by signing the data.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): PD.1-5, DE.1-2, IA.2
    * [CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper): Securing Artefacts—Automation, Controlled Environments, Encryption; Securing Deployments—Verification
    * [EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(iii), 4e(vi), 4e(ix), 4e(x)
    * [IDASOAR](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016): 25
    * [IEC62443](https://webstore.iec.ch/publication/33615): SM-6, SM-7
    * [NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): PR.IP-4
    * [OWASPSCVS](https://github.com/OWASP/Software-Component-Verification-Standard): 1, 3.18, 3.19, 6.3
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 5.2, 6.1, 6.2
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Vendor Software Delivery Integrity Controls
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-10, SA-15, SA-15(11), SR-4
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-8, SA-10, SA-15(11), SR-4

## PS.3.2 {: #ps-3-2 }

Collect, safeguard, maintain, and share provenance data for all components of each software release (e.g., in a software bill of materials [SBOM]).

???+ example "Implementation Examples"
    * Example 1: Make the provenance data available to software acquirers in accordance with the organization’s policies, preferably using standards-based formats.
    * Example 2: Make the provenance data available to the organization’s operations and response teams to aid them in mitigating software vulnerabilities.
    * Example 3: Protect the integrity of provenance data, and provide a way for recipients to verify provenance data integrity.
    * Example 4: Update the provenance data every time any of the software’s components are updated.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): SM.2
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): SE3.6
    * [CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper): Securing Materials—Verification, Automation
    * [EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(vi), 4e(vii), 4e(ix), 4e(x)
    * [NTIASBOM](https://www.ntia.doc.gov/report/2021/minimum-elements-software-bill-materials-sbom): All
    * [OWASPSCVS](https://github.com/OWASP/Software-Component-Verification-Standard): 1.4, 2
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Vendor Software Delivery Integrity Controls
    * [SCTPC](https://www.safecode.org/wp-content/uploads/2017/05/SAFECode_TPC_Whitepaper.pdf): MAINTAIN3
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-8, SR-3, SR-4
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-8, SR-3, SR-4

