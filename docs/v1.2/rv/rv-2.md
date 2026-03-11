---
title: 'RV.2: Assess, Prioritize, and Remediate Vulnerabilities'
practice_identifier: RV
task_identifier: RV.2
version: '1.2'
references:
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  VM.2'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  CMVM1.2, CMVM2.2'
- '[IEC62443](https://webstore.iec.ch/publication/33615): DM-2, DM-3'
- '[ISO30111](https://www.iso.org/standard/53231.html): 7.1.4'
- '[NISTLABEL](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity):
  2.2.2.2'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  3.4, 4.2'
- '[SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf):
  Operational Security Task 1, Tasks Requiring the Help of Security Experts 10'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-03, CM-04, RA-05, RA-05(04),
  SA-10, SA-15(07)'
- '[SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.3.8'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): CM-03'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0009, K0039, K0070, K0161,
  K0165; S0078'
- '[BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf):
  VM.1-1, VM-2'
- '[BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf):
  CMVM2.1'
- '[IEC62443](https://webstore.iec.ch/publication/33615): DM-4'
- '[ISO30111](https://www.iso.org/standard/53231.html): 7.1.4, 7.1.5'
- '[PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results):
  4.1, 4.2, 10.1'
- '[SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf):
  Operational Security Task 2'
- '[SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf):
  Fix the Vulnerability, Identify Mitigating Factors or Workarounds'
- '[SCTPC](https://www.safecode.org/wp-content/uploads/2017/05/SAFECode_TPC_Whitepaper.pdf):
  MITIGATE'
- '[SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-03, CM-04, CM-05, CM-06,
  SA-05, SA-10, SA-11, SA-15, SA-15(07)'
- '[SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): CM-03, CM-06'
- '[SP800181](https://doi.org/10.6028/NIST.SP.800-181): T0163, T0229, T0264; K0009,
  K0070'
---

# RV.2: Assess, Prioritize, and Remediate Vulnerabilities

Help ensure that vulnerabilities are remediated in accordance with risk to reduce the window of opportunity for attackers.

## RV.2.1 {: #rv-2-1 }

Analyze each vulnerability to gather sufficient information about risk and plan its remediation or other risk response.

???+ example "Implementation Examples"
    * Example 1: Use existing issue tracking software to record each vulnerability.\nExample 2: Perform risk calculations for each vulnerability based on estimates of its exploitability, the potential impact if exploited, and any other relevant characteristics.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): VM.2
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): CMVM1.2, CMVM2.2
    * [IEC62443](https://webstore.iec.ch/publication/33615): DM-2, DM-3
    * [ISO30111](https://www.iso.org/standard/53231.html): 7.1.4
    * [NISTLABEL](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity): 2.2.2.2
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 3.4, 4.2
    * [SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf): Operational Security Task 1, Tasks Requiring the Help of Security Experts 10
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-03, CM-04, RA-05, RA-05(04), SA-10, SA-15(07)
    * [SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.3.8
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): CM-03
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): K0009, K0039, K0070, K0161, K0165; S0078

## RV.2.2 {: #rv-2-2 }

Plan and implement risk responses for vulnerabilities.

???+ example "Implementation Examples"
    * Example 1: Make a risk-based decision as to whether each vulnerability will be remediated or if the risk will be addressed through other means (e.g., risk acceptance, risk transference), and prioritize any actions to be taken.\nExample 2: If a remediation for a vulnerability is not yet available, determine how the vulnerability can be temporarily mitigated until the permanent solution is available, and add that temporary mitigation to the plan.\nExample 3: Develop and release security advisories that provide the necessary information to software acquirers, including descriptions of what the vulnerabilities are, how to find instances of the vulnerable software, and how to address them (e.g., where to get patches and what the patches change in the software, what configuration settings may need to be changed, how temporary workarounds could be implemented).\nExample 4: Deliver remediations to acquirers via an automated and trusted delivery mechanism. A single remediation could address multiple vulnerabilities.\nExample 5: Update and periodically review records of design decisions, risk responses, and approved exceptions as needed. See PW.1.2.

??? info "References"
    * [BSAFSS](https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf): VM.1-1, VM-2
    * [BSIMM](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf): CMVM2.1
    * [IEC62443](https://webstore.iec.ch/publication/33615): DM-4
    * [ISO30111](https://www.iso.org/standard/53231.html): 7.1.4, 7.1.5
    * [NISTLABEL](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity): 2.2.2.2
    * [PCISSLC](https://www.pcisecuritystandards.org/document_library?category=sware_sec#results): 4.1, 4.2, 10.1
    * [SCAGILE](http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf): Operational Security Task 2
    * [SCFPSSD](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf): Fix the Vulnerability, Identify Mitigating Factors or Workarounds
    * [SCTPC](https://www.safecode.org/wp-content/uploads/2017/05/SAFECode_TPC_Whitepaper.pdf): MITIGATE
    * [SP80053](https://doi.org/10.6028/NIST.SP.800-53r5): CM-03, CM-04, CM-05, CM-06, SA-05, SA-10, SA-11, SA-15, SA-15(07)
    * [SP800160](https://doi.org/10.6028/NIST.SP.800-160v1): 3.3.8
    * [SP800161](https://doi.org/10.6028/NIST.SP.800-161r1-draft2): CM-03, CM-06
    * [SP800181](https://doi.org/10.6028/NIST.SP.800-181): T0163, T0229, T0264; K0009, K0070

