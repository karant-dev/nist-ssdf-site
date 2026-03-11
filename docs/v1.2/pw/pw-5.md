---
title: 'PW.5: Create Source Code by Adhering to Secure Coding Practices'
practice_identifier: PW
task_identifier: PW.5
version: '1.2'
references:
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  SC.2, SC.3, LO.1, EE.1'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  SR3.3, CR1.4, CR3.5'
- '[IDASoar](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016):
  2'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SI-1, SI-2'
- '[ISO27034](https://www.iso.org/standard/44378.html): 7.3.5'
- '[MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 9'
- '[OWASPASVS](https://github.com/OWASP/ASVS): 1.1.7, 1.5, 1.7, 5, 7'
- '[OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 7.6'
- '[SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf):
  Establish Log Requirements and Audit Practices, Use Code Analysis Tools to Find
  Security Issues Early, Handle Data Safely, Handle Errors, Use Safe Functions Only'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-15, SI-03, SI-10, SI-10(03)'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-001; T0013, T0077,
  T0176; K0009, K0016, K0039, K0070, K0140, K0624; S0019, S0060, S0149, S0172, S0266;
  A0036, A0047'
---

# PW.5: Create Source Code by Adhering to Secure Coding Practices

Decrease the number of security vulnerabilities in the software, and reduce costs by minimizing vulnerabilities introduced during source code creation that meet or exceed organization-defined vulnerability severity criteria.

## PW.5.1 {: #pw-5-1 }

Follow all secure coding practices that are appropriate to the development languages and environment to meet the organization's requirements.

???+ example "Implementation Examples"
    * Example 1: Validate all inputs, and validate and properly encode all outputs.\nExample 2: Avoid using unsafe functions and calls.\nExample 3: Detect errors, and handle them gracefully.\nExample 4: Provide logging and tracing capabilities.\nExample 5: Use development environments with automated features that encourage or require the use of secure coding practices with just-in-time training-in-place.\nExample 6: Follow procedures for manually ensuring compliance with secure coding practices when automated methods are insufficient or unavailable.\nExample 7: Use tools (e.g., linters, formatters) to standardize the style and formatting of the source code.\nExample 8: Check for other vulnerabilities that are common to the development languages and environment.\nExample 9: Have the developer review their own human-readable code to complement (not replace) code review performed by other people or tools. See PW.7.\nExample 10: When designing interfaces that accept input, use well-structured input formats that can be easily validated and sanitized.\nExample 11: Where appropriate, use formal methods and provers to validate the correctness of code. While particular attention should be given to high-risk code, other sections of code may also benefit from these techniques while balancing cost and risk trade-offs.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): SC.2, SC.3, LO.1, EE.1
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): SR3.3, CR1.4, CR3.5
    * [IDASoar](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016): 2
    * [IEC62443](https://webstore.iec.ch/publication/33615): SI-1, SI-2
    * [ISO27034](https://www.iso.org/standard/44378.html): 7.3.5
    * [MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 9
    * [OWASPASVS](https://github.com/OWASP/ASVS): 1.1.7, 1.5, 1.7, 5, 7
    * [OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 7.6
    * [SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf): Establish Log Requirements and Audit Practices, Use Code Analysis Tools to Find Security Issues Early, Handle Data Safely, Handle Errors, Use Safe Functions Only
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): SA-15, SI-03, SI-10, SI-10(03)
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-001; T0013, T0077, T0176; K0009, K0016, K0039, K0070, K0140, K0624; S0019, S0060, S0149, S0172, S0266; A0036, A0047

## PW.5.2 {: #pw-5-2 }

!!! warning "Task Moved"
    This task has been relocated. Please refer to [PW.5.1](pw-5.md#pw-5-1) for the current content.

