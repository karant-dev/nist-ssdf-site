---
title: 'PS.2: Provide a Mechanism for Verifying Software Release Integrity'
practice_identifier: PS
task_identifier: PS.2
version: '1.1'
references:
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  SM.4, SM.5, SM.6'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  SE2.4'
- "[CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper):\
  \ Securing Deployments\u2014Verification"
- '[EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(iii), 4e(ix),
  4e(x)'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SM-6, SM-8, SUM-4'
- '[NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): PR.DS-6'
- '[NISTLABEL](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity):
  2.2.2.4'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): OE3-B'
- '[OWASPSCVS](https://github.com/OWASP/Software-Component-Verification-Standard):
  4'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  6.1, 6.2'
- '[SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf):
  Vendor Software Delivery Integrity Controls'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-8'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-8'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0178'
---

# PS.2: Provide a Mechanism for Verifying Software Release Integrity

Help software acquirers ensure that the software they acquire is legitimate and has not been tampered with.

## PS.2.1 {: #ps-2-1 }

Make software integrity verification information available to software acquirers.

???+ example "Implementation Examples"
    * Example 1: Post cryptographic hashes for release files on a well-secured website.
    * Example 2: Use an established certificate authority for code signing so that consumers’ operating systems or other tools and services can confirm the validity of signatures before use.
    * Example 3: Periodically review the code signing processes, including certificate renewal, rotation, revocation, and protection.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): SM.4, SM.5, SM.6
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): SE2.4
    * [CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper): Securing Deployments—Verification
    * [EO14028](https://www.govinfo.gov/app/details/DCPD-202100401): 4e(iii), 4e(ix), 4e(x)
    * [IEC62443](https://webstore.iec.ch/publication/33615): SM-6, SM-8, SUM-4
    * [NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): PR.DS-6
    * [NISTLABEL](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity): 2.2.2.4
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): OE3-B
    * [OWASPSCVS](https://github.com/OWASP/Software-Component-Verification-Standard): 4
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 6.1, 6.2
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Vendor Software Delivery Integrity Controls
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-8
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SA-8
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0178

