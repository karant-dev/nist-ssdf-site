---
title: 'PO.1: Define Security Requirements for Software Development'
practice_identifier: PO
task_identifier: PO.1
version: '1.2'
references:
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  SM.3, DE.1, IA.1, IA.2'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  CP1.1, CP1.3, SR1.1, SR2.2, SE1.2, SE2.6'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SM-7, SM-9'
- '[NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): ID.GV-3'
- '[OWASPASVS](https://github.com/OWASP/ASVS): 1.1.1'
- '[OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 1.10'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): PC1-A, PC1-B,
  PC2-A'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  2.1, 2.2'
- '[SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf):
  Planning the Implementation and Deployment of Secure Development Practices'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): AT-03, CM-01, PL-08, PM-01,
  SA-01, SA-02, SA-08, SA-10, SA-15, SA-17, SR-01, SR-03, SR-05'
- '[SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.1.2, 3.2.1, 3.2.2, 3.3.1,
  3.4.2, 3.4.3'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): AT-03, CM-01, PL-07,
  PL-08, SR-05'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): T0414; K0003, K0039, K0044,
  K0157, K0168, K0177, K0211, K0260, K0261, K0262, K0524; S0010, S0357, S0368; A0033,
  A0123, A0151'
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  SC.1-1, SC.2, PD.1-1, PD.1-2, PD.1-3, PD.2-2, SI, PA, CS, AA, LO, EE'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  SM1.1, SM1.4, SM2.2, CP1.1, CP1.2, CP1.3, CP2.1, CP2.3, AM1.2, SFD1.1, SFD2.1, SFD3.2,
  SR1.1, SR1.3, SR2.2, SR3.3, SR3.4'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SR-3, SR-4, SR-5, SD-4'
- '[ISO27034](https://www.iso.org/standard/44378.html): 7.3.2'
- '[MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 2, 5'
- '[OWASPMAVS]: 1.12'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): PC1-A, PC1-B,
  PC2-A, PC3-A, SR1-A, SR1-B, SR2-B, SA1-B, IR1-A'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  2.1, 2.2, 2.3, 3.3'
- '[SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf):
  Establish Coding Standards and Conventions'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CA-03, CM-08, PM-01, PM-08,
  PM-18, PM-30, RA-03, SA-02, SA-04, SR-02'
- '[SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.1.2, 3.2.1, 3.3.1'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): CM-02, CM-07, PM-30,
  RA-03, RA-09, SC-07'
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  SM.1, SM.2, SM.2-1, SM.2-4'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  CP2.4, CP3.2, SR2.5, SR3.2'
- '[IDASOAR](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016):
  19, 21'
- '[IEC62443](https://webstore.iec.ch/publication/33615): SM-9, SM-10'
- '[MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 7'
- '[NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): ID.SC-3'
- '[OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): SR3-A'
- '[SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf):
  Tasks Requiring the Help of Security Experts 8'
- '[SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf):
  Manage Security Risk Inherent in the Use of Third-Party Components'
- '[SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf):
  Vendor Sourcing Integrity Controls'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CA-03, SA-04, SA-21'
- '[SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.1.1, 3.1.2'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): T0203, T0415; K0039; S0374;
  A0056, A0161'
---

# PO.1: Define Security Requirements for Software Development

Ensure that security requirements for software development are known at all times so that they can be taken into account throughout the SDLC and the duplication of effort can be minimized because the requirements information can be collected once and shared. This includes requirements from internal sources (e.g., the organization's policies, business objectives, and risk management strategy) and external sources (e.g., applicable laws and regulations).

## PO.1.1 {: #po-1-1 }

Identify and document all security requirements for the organization's software development infrastructures and processes, and maintain the requirements over time.

???+ example "Implementation Examples"
    * Example 1: Define policies for securing software development infrastructures and their components, including development endpoints, throughout the SDLC and maintaining that security.\nExample 2: Define policies for securing software development processes throughout the SDLC and maintaining that security, including for open-source and other third-party software components utilized by software being developed.\nExample 3: Review and update security requirements at least annually, or sooner if there are new requirements from internal or external sources, or if a major security incident targeting software development infrastructure has occurred.\nExample 4: Educate affected individuals on impending changes to requirements.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): SM.3, DE.1, IA.1, IA.2
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): CP1.1, CP1.3, SR1.1, SR2.2, SE1.2, SE2.6
    * [IEC62443](https://webstore.iec.ch/publication/33615): SM-7, SM-9
    * [NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): ID.GV-3
    * [OWASPASVS](https://github.com/OWASP/ASVS): 1.1.1
    * [OWASPMASVS](https://github.com/OWASP/owasp-masvs/releases): 1.10
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): PC1-A, PC1-B, PC2-A
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 2.1, 2.2
    * [SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf): Planning the Implementation and Deployment of Secure Development Practices
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): AT-03, CM-01, PL-08, PM-01, SA-01, SA-02, SA-08, SA-10, SA-15, SA-17, SR-01, SR-03, SR-05
    * [SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.1.2, 3.2.1, 3.2.2, 3.3.1, 3.4.2, 3.4.3
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): AT-03, CM-01, PL-07, PL-08, SR-05
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): T0414; K0003, K0039, K0044, K0157, K0168, K0177, K0211, K0260, K0261, K0262, K0524; S0010, S0357, S0368; A0033, A0123, A0151

## PO.1.2 {: #po-1-2 }

Identify and document all security requirements for organization-developed software to meet, and maintain the requirements over time.

???+ example "Implementation Examples"
    * Example 1: Define policies that specify risk-based software architecture and design requirements, such as making code modular to facilitate code reuse and updates, isolating security components from other components during execution, avoiding undocumented commands and settings, using consensus standards where available, and providing features that will aid software acquirers with the secure deployment, operation, and maintenance of the software, including secure default configurations.\nExample 2: Define policies that specify the security requirements for the organization's software, and verify compliance at key points in the SDLC (e.g., classes of software flaws verified by gates, responses to vulnerabilities discovered in released software).\nExample 3: Analyze the risk of applicable technology stacks (e.g., languages, environments, deployment models), and recommend or require the use of stacks that will reduce risk compared to others.\nExample 4: Define policies that specify what needs to be archived for each software release (e.g., code, package files, third-party libraries, documentation, data inventory) and how long it needs to be retained based on the SDLC model, software end-of-life, and other factors.\nExample 5: Ensure that policies cover the entire software life cycle, including notifying users of the impending end of software support and the date of software end-of-life.\nExample 6: Review all security requirements at least annually, sooner if there are new requirements from internal or external sources, if a major vulnerability is discovered in released software, or if a major security incident targeting organization-developed software has occurred.\nExample 7: Establish and follow processes for handling requirement exception requests, including periodic reviews of all approved exceptions.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): SC.1-1, SC.2, PD.1-1, PD.1-2, PD.1-3, PD.2-2, SI, PA, CS, AA, LO, EE
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): SM1.1, SM1.4, SM2.2, CP1.1, CP1.2, CP1.3, CP2.1, CP2.3, AM1.2, SFD1.1, SFD2.1, SFD3.2, SR1.1, SR1.3, SR2.2, SR3.3, SR3.4
    * [IEC62443](https://webstore.iec.ch/publication/33615): SR-3, SR-4, SR-5, SD-4
    * [ISO27034](https://www.iso.org/standard/44378.html): 7.3.2
    * [MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 2, 5
    * [NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): ID.GV-3
    * [OWASPMAVS]: 1.12
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): PC1-A, PC1-B, PC2-A, PC3-A, SR1-A, SR1-B, SR2-B, SA1-B, IR1-A
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 2.1, 2.2, 2.3, 3.3
    * [SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf): Establish Coding Standards and Conventions
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CA-03, CM-08, PM-01, PM-08, PM-18, PM-30, RA-03, SA-02, SA-04, SR-02
    * [SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.1.2, 3.2.1, 3.3.1
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): CM-02, CM-07, PM-30, RA-03, RA-09, SC-07
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): T0414; K0003, K0039, K0044, K0157, K0168, K0177, K0211, K0260, K0261, K0262, K0524; S0010, S0357, S0368; A0033, A0123, A0151

## PO.1.3 {: #po-1-3 }

Communicate requirements to all third parties who will provide commercial software components to the organization for reuse by the organization's own software. [Formerly PW.3.1]

???+ example "Implementation Examples"
    * Example 1: Define a core set of security requirements for software components, and include it in acquisition documents, software contracts, and other agreements with third parties.\nExample 2: Define security-related criteria for selecting software, such as a third party's vulnerability disclosure program, product security incident response capabilities, or adherence to their organization-defined practices.\nExample 3: Require third parties to attest that their software complies with the organization's security requirements.\nExample 4: Require third parties to provide provenance data and integrity verification mechanisms for all components of their software.\nExample 5: Establish and follow processes to address risk when there are security requirements that third-party software components to be acquired do not meet, including periodic reviews of all approved exceptions to requirements.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): SM.1, SM.2, SM.2-1, SM.2-4
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): CP2.4, CP3.2, SR2.5, SR3.2
    * [IDASOAR](https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016): 19, 21
    * [IEC62443](https://webstore.iec.ch/publication/33615): SM-9, SM-10
    * [MSSDL](https://www.microsoft.com/en-us/securityengineering/sdl/): 7
    * [NISTCSF](https://doi.org/10.6028/NIST.CSWP.04162018): ID.SC-3
    * [OWASPSAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project): SR3-A
    * [SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf): Tasks Requiring the Help of Security Experts 8
    * [SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf): Manage Security Risk Inherent in the Use of Third-Party Components
    * [SCSIC](http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf): Vendor Sourcing Integrity Controls
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CA-03, SA-04, SA-21
    * [SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.1.1, 3.1.2
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): T0203, T0415; K0039; S0374; A0056, A0161

