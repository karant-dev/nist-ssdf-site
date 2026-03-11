---
title: 'PW.4: Reuse Existing, Well-Secured Software When Feasible Instead of Duplicating
  Functionality'
practice_identifier: PW
task_identifier: PW.4
version: '1.2'
references:
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  SM.2'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  SFD2.1, SFD3.2, SR2.4, SR3.1, SE3.6'
- "[CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper):\
  \ Securing Materials\u2014Verification"
- '[IDASoar](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016):
  19'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SM-9, SM-10'
- '[MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 6'
- '[NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): ID.SC-2'
- '[OWASPASVS](https://github.com/OWASP/ASVS): 1.1.6'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): SA1-A'
- '[OWASPSCVS](https://github.com/OWASP/Software-Component-Verification-Standard):
  4'
- '[SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf):
  Vendor Sourcing Integrity Controls'
- '[SCTPC](https://www.safecode.org/wp-content/uploads/2017/05/SAFECode_TPC_Whitepaper.pdf):
  MAINTAIN'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-08, SA-04, SA-05, SA-10(06),
  SC-12, SR-03, SR-04'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SR-13'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0039'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  SFD1.1, SFD2.1, SFD3.2, SR1.1'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-09, CM-11, SA-15, SA-17,
  SA-20'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-001'
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  SC.3-1, SM.2-1, SM.2-2, SM.2-3, TV.2, TV.3'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  CP3.2, SR2.4, SR3.1, SR3.2, SE2.4, SE3.6'
- "[CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper):\
  \ Securing Materials\u2014Verification, Automation"
- '[IDASoar](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016):
  21'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SI-1, SM-9, SM-10, DM-1'
- '[IR8397](https://doi.org/10.6028/NIST.IR.8397): 2.11'
- '[MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 7'
- '[NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): ID.SC-4, PR.DS-6'
- '[NISTLABEL](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity):
  2.2.2.2'
- '[OWASPASVS](https://github.com/OWASP/ASVS): 10, 14.2'
- '[OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 7.5'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): TA3-A, SR3-B'
- '[OWASPSCVS](https://github.com/OWASP/Software-Component-Verification-Standard):
  4, 5, 6'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  3.2, 3.4, 4.1'
- '[SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf):
  Tasks Requiring the Help of Security Experts 8'
- '[SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf):
  Manage Security Risk Inherent in the Use of Third-Party Components'
- '[SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf):
  Vendor Sourcing Integrity Controls, Peer Reviews and Security Testing'
- '[SCTPC](https://www.safecode.org/wp-content/uploads/2017/05/SAFECode_TPC_Whitepaper.pdf):
  MAINTAIN, ASSESS'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CA-02, CA-05, CA-06, SA-09,
  SR-03, SR-04, SR-04(03), SR-04(04)'
- '[SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.1.2, 3.3.8'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SR-03, SR-04'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-002; K0153, K0266;
  S0298'
---

# PW.4: Reuse Existing, Well-Secured Software When Feasible Instead of Duplicating Functionality

Lower the costs of software development, expedite software development, and decrease the likelihood of introducing additional security vulnerabilities into the software by reusing software modules and services that have already had their security posture checked. This is particularly important for software that implements security functionality, such as cryptographic modules and protocols.

## PW.4.1 {: #pw-4-1 }

Acquire and maintain well-secured software components (e.g., software libraries, modules, middleware, frameworks) from commercial, open-source, and other third-party developers for use by the organization's software.

???+ example "Implementation Examples"
    * Example 1: Review and evaluate third-party software components in the context of their expected use. If a component is to be used in a substantially different way in the future, perform the review and evaluation again with that new context in mind.\nExample 2: Determine secure configurations for software components, and make these available (e.g., as configuration-as-code) so developers can readily use the configurations.\nExample 3: Obtain provenance information (e.g., SBOM, source composition analysis, binary software composition analysis) for each software component, and analyze that information to better assess the risk that the component may introduce.\nExample 4: Establish one or more software repositories to host sanctioned and vetted open-source components.\nExample 5: Maintain a list of organization-approved commercial software components and component versions along with their provenance data.\nExample 6: Designate which components must be included in software to be developed.\nExample 7: Implement processes to update deployed software components to newer versions, and retain older versions of software components until all transitions from those versions have been completed successfully.\nExample 8: If the integrity or provenance of acquired binaries cannot be confirmed, build binaries from source code after verifying the source code's integrity and provenance.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): SM.2
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): SFD2.1, SFD3.2, SR2.4, SR3.1, SE3.6
    * [CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper): Securing Materials—Verification
    * [IDASoar](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016): 19
    * [IEC62443](https://webstore.iec.ch/publication/33615): SM-9, SM-10
    * [MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 6
    * [NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): ID.SC-2
    * [OWASPASVS](https://github.com/OWASP/ASVS): 1.1.6
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): SA1-A
    * [OWASPSCVS](https://github.com/OWASP/Software-Component-Verification-Standard): 4
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Vendor Sourcing Integrity Controls
    * [SCTPC](https://www.safecode.org/wp-content/uploads/2017/05/SAFECode_TPC_Whitepaper.pdf): MAINTAIN
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-08, SA-04, SA-05, SA-10(06), SC-12, SR-03, SR-04
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SR-13
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0039

## PW.4.2 {: #pw-4-2 }

Create and maintain well-secured software components in-house following SDLC processes to meet common internal software development needs that cannot be better met by third-party software components.

???+ example "Implementation Examples"
    * Example 1: Follow organization-established security practices for secure software development when creating and maintaining the components.\nExample 2: Determine secure configurations for software components, and make these available (e.g., as configuration-as-code) so developers can readily use the configurations.\nExample 3: Maintain one or more software repositories for these components.\nExample 4: Designate which components must be included in software to be developed.\nExample 5: Implement processes to update deployed software components to newer versions, and maintain older versions of software components until all transitions from those versions have been completed successfully.

??? info "References"
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): SFD1.1, SFD2.1, SFD3.2, SR1.1
    * [IDASoar](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016): 19
    * [OWASPASVS](https://github.com/OWASP/ASVS): 1.1.6
    * [SCTPC](https://www.safecode.org/wp-content/uploads/2017/05/SAFECode_TPC_Whitepaper.pdf): MAINTAIN
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-09, CM-11, SA-15, SA-17, SA-20
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-001

## PW.4.3 {: #pw-4-3 }

!!! warning "Task Moved"
    This task has been relocated. Please refer to [PW.1.3](pw-1.md#pw-1-3) for the current content.

## PW.4.4 {: #pw-4-4 }

Verify that acquired commercial, open-source, and all other third-party software components comply with the requirements, as defined by the organization, throughout their life cycles.

???+ example "Implementation Examples"
    * Example 1: Regularly check whether there are publicly known vulnerabilities in the software modules and services that vendors have not yet remediated.\nExample 2: Build into the toolchain automatic detection of known vulnerabilities in software components.\nExample 3: Use existing results from commercial services for vetting the software modules and services.\nExample 4: Ensure that each software component is still actively maintained and has not reached end of life. This should include assurance that new vulnerabilities found in the software are being remediated and should extend to software that has been acquired as part of a merger or acquisition.\nExample 5: Determine a plan of action for each software component that is no longer being maintained or will not be available in the near future.\nExample 6: Confirm the integrity of software components through digital signatures or other mechanisms.\nExample 7: Review, analyze, and/or test code. See PW.7 and PW.8.\nExample 8: Regularly review all third-party libraries for ownership changes, and evaluate any impacts from a change in ownership.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): SC.3-1, SM.2-1, SM.2-2, SM.2-3, TV.2, TV.3
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): CP3.2, SR2.4, SR3.1, SR3.2, SE2.4, SE3.6
    * [CNCFSSCP](https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper): Securing Materials—Verification, Automation
    * [IDASoar](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016): 21
    * [IEC62443](https://webstore.iec.ch/publication/33615): SI-1, SM-9, SM-10, DM-1
    * [IR8397](https://doi.org/10.6028/NIST.IR.8397): 2.11
    * [MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 7
    * [NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): ID.SC-4, PR.DS-6
    * [NISTLABEL](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity): 2.2.2.2
    * [OWASPASVS](https://github.com/OWASP/ASVS): 10, 14.2
    * [OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 7.5
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): TA3-A, SR3-B
    * [OWASPSCVS](https://github.com/OWASP/Software-Component-Verification-Standard): 4, 5, 6
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 3.2, 3.4, 4.1
    * [SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf): Tasks Requiring the Help of Security Experts 8
    * [SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf): Manage Security Risk Inherent in the Use of Third-Party Components
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Vendor Sourcing Integrity Controls, Peer Reviews and Security Testing
    * [SCTPC](https://www.safecode.org/wp-content/uploads/2017/05/SAFECode_TPC_Whitepaper.pdf): MAINTAIN, ASSESS
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CA-02, CA-05, CA-06, SA-09, SR-03, SR-04, SR-04(03), SR-04(04)
    * [SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.1.2, 3.3.8
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): SR-03, SR-04
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): SP-DEV-002; K0153, K0266; S0298

## PW.4.5 {: #pw-4-5 }

!!! warning "Task Moved"
    This task has been relocated. Please refer to [PW.4.1](pw-4.md#pw-4-1) for the current content.

