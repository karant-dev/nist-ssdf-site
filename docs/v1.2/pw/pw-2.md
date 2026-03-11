---
title: 'PW.2: Review the Software Design to Verify Compliance with Security Requirements
  and Risk Information'
practice_identifier: PW
task_identifier: PW.2
version: '1.2'
references:
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  TV.3'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  AA1.1, AA1.2, AA1.3, AA2.1, AA3.1'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SM-2, SR-2, SR-5, SD-3,
  SD-4, SI-2'
- '[ISO27034](https://www.iso.org/standard/44378.html): 7.3.3'
- '[OWASPASVS](https://github.com/OWASP/ASVS): 1.1.5'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): DR1-A, DR1-B'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  3.2'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CA-01, CA-03'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): T0328; K0038, K0039, K0070,
  K0080, K0119, K0152, K0153, K0161, K0165, K0172, K0297; S0006, S0009, S0022, S0036,
  S0141, S0171'
---

# PW.2: Review the Software Design to Verify Compliance with Security Requirements and Risk Information

Help ensure that the software will meet the security requirements and satisfactorily address the identified risk information.

## PW.2.1 {: #pw-2-1 }

Have 1) a qualified person (or people) who were not involved with the design and/or 2) automated processes instantiated in the toolchain review the software design to confirm and enforce that it meets all of the security requirements and satisfactorily addresses the identified risk information.

???+ example "Implementation Examples"
    * Example 1: Review the software design to confirm that it addresses applicable security requirements.\nExample 2: Review the risk models created during software design to determine if they appear to adequately identify the risks.\nExample 3: Review the software design to confirm that it satisfactorily addresses the risks identified by the risk models.\nExample 4: Have the software's designer correct failures to meet the requirements.\nExample 5: Change the design and/or the risk response strategy if the security requirements cannot be met.\nExample 6: Record the findings of design reviews to serve as artifacts (e.g., in the software specification, in the issue tracking system, in the threat model).

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): TV.3
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): AA1.1, AA1.2, AA1.3, AA2.1, AA3.1
    * [IEC62443](https://webstore.iec.ch/publication/33615): SM-2, SR-2, SR-5, SD-3, SD-4, SI-2
    * [ISO27034](https://www.iso.org/standard/44378.html): 7.3.3
    * [OWASPASVS](https://github.com/OWASP/ASVS): 1.1.5
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): DR1-A, DR1-B
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 3.2
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CA-01, CA-03
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): T0328; K0038, K0039, K0070, K0080, K0119, K0152, K0153, K0161, K0165, K0172, K0297; S0006, S0009, S0022, S0036, S0141, S0171

