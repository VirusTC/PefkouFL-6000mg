# CLINICAL COORDINATOR SYSTEM DEPLOYMENT GUIDE
**Operational Scope:** Institutional Review Board (IRB) Expanded Access Site Management  
**Target API:** Standardized 15:1 *Pinus pinaster* Resin Matrix Core

This standard operating guide details the mandatory technical actions clinical coordinators must execute at each workflow node during a patient's PefkouFL-6000mg lifecycle.

## NODE 1: SCREENING & GATEKEEPER AUDIT (DAY 0)
1.  **Vascular Stagnation Baseline:** Verify that the candidate's CEAP classification is logged at $\geq C_3$ (Chronic Venous Insufficiency presenting with objective microangiopathy or ankle edema).
2.  **Oxidative Degradation Panel:** Draw a baseline blood panel to establish the patient's baseline **Erythrocyte Membrane Malondialdehyde (MDA)** concentration via the thiobarbituric acid reactive substances (TBARS) assay. 
3.  **Cross-Check Contraindications:** Reject the patient immediately if there is any scheduled surgical intervention within the next 14 days, or if they have an active history of bleeding disorders.

## NODE 2: INVESTIGATIONAL LOT ACCOUNTING & AUDITING
1.  **Environmental Validation:** Audit the clinical pharmacy storage logs weekly to verify that the ambient climate is continuously regulated beneath **35% Relative Humidity (RH)** and a temperature matrix of **20°C to 25°C**.
2.  **Traceability Registration:** When dispensing the J-code botanical unit, log the unique batch number (e.g., `PP-2026-0715-A`) into the `EXPANDED_ACCESS_PATIENT_METRICS.tsv` database alongside the exact date stamp.

## NODE 3: MID-CYCLE FLOW AUDITING (DAY 14)
1.  **Vascular Waveform Screening:** Perform non-invasive bilateral capillary fluid flow waveform analysis to verify that the up-regulation of endothelial Nitric Oxide Synthase (eNOS) is progressing inside safe physiological parameters.
2.  **Oxidative Recovery Metrics:** Re-test erythrocyte membrane MDA levels. Successful therapy displays a downward mathematical shift in MDA concentration, confirming that the Hydrogen Atom Transfer (HAT) pathway is effectively shielding red blood cell lipid bilayers from ongoing chain-reactions.
