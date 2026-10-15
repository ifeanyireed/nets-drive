# 📋 Steps.md: New Era Transports Services Sequential Multi-Agent Production Workflow

This document outlines the sequential steps required to generate the complete B2B marketing, sales enablement, and corporate acquisition content suite for **New Era Transports Services**.

Agents must follow this exact sequence to ensure consistency, voice alignment, and adherence to quality standards across **all 5 Corporate Clusters and 9 Months (36 Weeks)**.

> [!IMPORTANT]
> **Social Media Channel Policy**: Social media distribution is **strictly and exclusively LinkedIn**. Stream 4 produces `linkedin-pack.md`. No content is produced for Twitter/X, Facebook, Instagram, or TikTok.

---

## Workflow Overview

```
[Phase 0: nets-drive.html Calendar & Universe Ingestion]
                      │
                      ▼
[Folder Initialization: Cluster-[XX]/Week-[YY]/]
                      │
                      ▼
[Phase 1: Video Script ────────► video-script.md]
                      │
                      ▼
[Phase 2: Blog Post ──────────► blog-post.md]
                      │
                      ▼
[Phase 3: HTML Email Blast ────► email-blast.html & email-blast.md]
                      │
                      ▼
[Phase 4: LinkedIn Pack ───────► linkedin-pack.md (ONLY social channel)]
                      │
                      ▼
[Phase 5: Cross-Asset Audit & Progress-Tracker Update]
```

---

## Phase 0: Calendar & Account Universe Ingestion

### Step 0.1: Extract Cluster, Month & Week Parameters from `nets-drive.html`
* **Action**: Read `CALENDAR_DATA` inside [`nets-drive.html`](file:///Users/ifeanyifelix/Desktop/ReedBreedCC/nets-drive/nets-drive.html) for the target `clusterId` (`cluster1` to `cluster5`) and `monthId` (`Month 1` to `Month 9`).
* **Cluster Calibration Gate**:
  - **Cluster 1 $\rightarrow$ Industrial Shift Workers & Factory Lines**: FMCG, heavy manufacturing, plant downtime focus, Agbara/Sagamu/Ota corridors.
  - **Cluster 2 $\rightarrow$ High-HSE Field Crews & Energy Operations**: Upstream O&G, IOC compliance, zero-fatality standards, Port Harcourt/Warri corridors.
  - **Cluster 3 $\rightarrow$ Corporate White-Collar Commuter Networks**: Banks, fintechs, professional services, commuter burnout, Mainland-to-Island corridors.
  - **Cluster 4 $\rightarrow$ Night-Shift & Safe Store Dispersal**: Retail, QSR, 24/7 BPOs, late-night safety, closing shift dispersal routes.
  - **Cluster 5 $\rightarrow$ Executive VIP, Protocol & Projects**: C-Suite, embassies, board summits, airport protocol, luxury Prado/HiAce VIP fleet.
* **Extract the 4 Streams for the Target Week**:
  - `w.week`: Week number and theme (e.g., *Week 1: The Core Operational Bottleneck*).
  - `w.focus`: Funnel stage (e.g., *TOFU (Foundation) - The True Cost of Transit Friction*).
  - `w.blog`: Stream 1 Blog topic and strategic angle.
  - `w.email`: Stream 2 Email topic and body angle.
  - `w.video`: Stream 3 Video topic and format.
  - `w.graphic`: Stream 4 Graphic / Carousel topic (repurposed into LinkedIn Document Carousel).

### Step 0.2: Account Profile & Decision-Maker Extraction
* **Action**: Query corresponding account tables in `allCompanies` from `nets-drive.html` and the enriched markdown directories ([`cluster_1.md`](file:///Users/ifeanyifelix/Desktop/ReedBreedCC/nets-drive/cluster_1.md), [`cluster_2.md`](file:///Users/ifeanyifelix/Desktop/ReedBreedCC/nets-drive/cluster_2.md), [`cluster_3.md`](file:///Users/ifeanyifelix/Desktop/ReedBreedCC/nets-drive/cluster_3.md)).
* **Extract Lead Details**:
  - Target executive roles (Plant Director, HR Director, HSE Lead, Corporate Admin Head, EA to MD).
  - Core operational friction points (e.g., Agbara 6:00 AM shift lateness, IOC journey management failure, 3.5-hour Third Mainland Bridge fatigue, female retail staff stranded at midnight).
  - Designated NETS fleet solution from [`Skills.md`](file:///Users/ifeanyifelix/Desktop/ReedBreedCC/nets-drive/AGENT/Skills.md).

### Step 0.3: Folder Initialization
* **Action**: Create the dedicated directory for the cluster and week:
  ```
  Cluster-[XX]/Week-[YY]/
  ```
  *(Example: `Cluster-01/Week-01/`)*

---

## Phase 1: Video Script Production (`video-script.md`)

* **Agent**: Video Script Specialist (Stream 3)
* **Target File**: `Cluster-[XX]/Week-[YY]/video-script.md`

### Production Directives:
1. **Audio/Visual Two-Track Format**: Clean markdown table with columns for `Timecode | Visual / Scene Action | Audio / Spoken Dialogue & SFX`.
2. **Pacing & Runtime**: 600–650 spoken words (~4:15 runtime at ~140 WPM).
3. **Pattern-Interrupt Hook (0:00–0:15)**: Visceral corridor disruption, machine alarm, or executive panic.
4. **Three-Scene Narrative Arc**:
   - *Scene 1: The Operational Crisis (0:15–1:15)*: Frontline struggle (unreliable Danfo breaks down; workers stranded at Sagamu chokepoint; packaging line sits idle; HR director gets resignation emails).
   - *Scene 2: The Escalation & Cost Spike (1:15–2:30)*: The financial and human fallout; confrontation between plant supervisor and management; split-screen comparison between unmanaged transit and a smooth NETS fleet arrival.
   - *Talking Head: The Quantitative Math (2:30–3:15)*: Calm host breakdown explaining the cluster's mathematical downtime formula.
   - *Scene 3: The Rewind (3:15–3:55)*: Rewind sound effect; the same corridor replayed with dedicated NETS climate-controlled shuttles arriving on schedule with digital attendance.
   - *Talking Head: The Close & CTA (3:55–4:15)*: Pitch NETS Corporate Fleet Services and offer the Free Route & Cost Audit (`www.neweratransports.com/corporate-audit`).
5. **Production Notes**: Casting specs, audio SFX cues, B-roll recommendations, and a 60-second TikTok/Reels cutdown concept.

---

## Phase 2: Bookmarkable Blog Post (`blog-post.md`)

* **Agent**: Editorial Blog Specialist (Stream 1)
* **Target File**: `Cluster-[XX]/Week-[YY]/blog-post.md`

### Production Directives:
1. **Word Count & Depth**: 1,500 – 2,200 words of rigorous, bookmarkable corporate mobility strategy.
2. **Standard Metadata**:
   - H1 Title (high-intent, problem-focused).
   - Byline: `Written by @Ifeanyi Felix · Corporate Mobility Strategy Lead`.
   - Publication date, read time (8–10 min read), target audience, meta description.
3. **3D Disney Pixar Featured Image Prompt**:
   - Must use the strict prompt format:
     ```markdown
     > **VISUAL FOR BLOG FEATURED IMAGE:**
     > *3D Disney Pixar style animation. Netflix-grade cinematic lighting with screen glow on faces, UHD 8k, stylized technology. [Character description, African features, occupational attire] in [Nigerian industrial/corporate setting] facing [transit crisis/idle factory/commuter gridlock], illuminated by [the warm interior glow of a modern NETS executive shuttle].*
     ```
4. **Authentic Nigerian Transit Data**: Ground content in verified infrastructure corridors (Lagos-Ibadan Expressway, Sagamu Interchange, Agbara Estate, Lekki-Epe Expressway, Port Harcourt - Warri corridor, Third Mainland Bridge).
5. **The Quantitative Formula**: Include the cluster-specific mathematical formula from [`Skills.md`](file:///Users/ifeanyifelix/Desktop/ReedBreedCC/nets-drive/AGENT/Skills.md) with a fully worked, realistic financial example in Nigerian Naira (₦).
6. **10 Actionable Operational Tactics**: Exactly 10 numbered, tactical operational frameworks that an HR Director, Plant Manager, or HSE Lead can implement immediately.
7. **Side-by-Side Comparison Table**: "Informal Danfo Charters / Cash Allowances" vs "Dedicated NETS Managed Fleet".
8. **Decisive Corporate CTA**: Request a Free Route Review & Cost Benchmark.

---

## Phase 3: Pure-News Responsive HTML Email Newsletter (`email-blast.html` & `email-blast.md`)

* **Agent**: Email Marketing Specialist (Stream 2)
* **Target Files**: `Cluster-[XX]/Week-[YY]/email-blast.html` & `Cluster-[XX]/Week-[YY]/email-blast.md`

### Production Directives:
1. **Publication Identity**: Formatted as *The NETS Corporate Mobility Dispatch*.
2. **Subject Line Matrix**:
   - Option A: *Pain Hook*
   - Option B: *Curiosity Hook*
   - Option C: *Metric Hook*
   - *Preview Text* (under 90 characters).
3. **Pure News Reporting Mandate**:
   - The Cover Story and 3 Curated News Cards must report on **actual breaking Nigerian infrastructure, corporate transport, fuel policy, logistics, and regulatory news** (e.g. fuel subsidy impact, CNG conversion policies, corridor rehabilitation, FRSC logistics regulations, port access bottlenecks).
   - Each story includes an authentic photo, source attribution, and a highlighted *"► WHAT IT MEANS FOR CORPORATE OPERATORS"* analysis.
4. **Mobility Hack / Metric of the Week**: High-contrast callout container presenting the blog post's mathematical formula as the operational answer to transit inflation.
5. **Bulletproof CTA Button (Zero Corner Radius)**: Directs readers to read the full blog post or schedule a Corporate Route Benchmark. Must strictly feature **zero corner radius (`border-radius: 0px`)** with sharp rectangular corners, styled in primary Corporate Royal Blue (`#1A48B6`) with `#FFFFFF` bold text and generous `14px 28px` padding.
6. **Footer Offer**: Highlights NETS 1-2 Route Pilot Program, SLA guarantees, and 30-day corporate billing.
7. **HTML Architecture**: Clean responsive 600px table with inline CSS, tested for desktop and mobile clients.
8. **Light Executive UI Rule**: Zero black or dark (`#0F172A` / `#000000` / `#1E293B`) UI backgrounds. Headers, callout metric containers, and footers must use light backgrounds (`#FFFFFF`, `#F8FAFC`, `#F1F5F9`) with dark high-contrast typography.
9. **Strict Brand Colors (`logo.png`) & Zero Corner Radius Mandate**:
   - Style templates strictly with the brand palette from `logo.png`: **Primary Corporate Royal Blue (`#1A48B6` / `#0F3282`)** for CTA buttons, headings, and links; **Secondary Signature Red (`#FE0B10` / `#D4080D`)** for header masthead accent borders, category eyebrows, and alert highlights; **Crisp White (`#FFFFFF`)** and Light Neutrals (`#F8FAFC`, `#F1F5F9`) for surfaces.
   - **Zero Corner Radius (`border-radius: 0px`)**: All buttons, cards, containers, and badges must feature zero corner radius for a crisp, enterprise B2B aesthetic.
   - **Logo Placement**: Prominently feature `logo.png` reduced in size and placed **directly side-by-side with the titles** (NEVER standing alone on its own line): in the **header masthead** (`width="44" height="44"`, 2-column layout beside titles) and in the **footer legal section** (`width="22" height="22"`, inline beside company name).

---

## Phase 4: LinkedIn B2B Acquisition Pack (`linkedin-pack.md`)

* **Agent**: LinkedIn Specialist (Stream 4 — Only Social Platform)
* **Target File**: `Cluster-[XX]/Week-[YY]/linkedin-pack.md`

### Production Directives:
1. **Long-Form C-Suite Thought Leadership Post**:
   - **The Hook Before the Fold (<140 characters)**: First 1–2 lines grab attention before the `...see more` cutoff.
   - **Visual Spacing**: Short 1–2 sentence paragraphs, generous line breaks for mobile dwell time.
   - **Nigerian Corridor Realities**: Agbara, Sagamu, Third Mainland Bridge, Lekki-Epe chokepoints.
   - **Quantitative Breakdown**: Cluster mathematical formula with realistic calculations in Naira (₦).
   - **5 Actionable Takeaways**: Strategic shifts for operational leaders.
   - **Discussion Trigger**: Low-friction question to prompt executive comments.
   - **First-Comment Link Strategy**: Explicit directive placing the audit link in the first comment (`🔗 Book your free corporate route review in the first comment below`).
2. **Short-Form Alternative**:
   - Punchy 300–400 character alternative post format for fast consumption.
3. **6 to 8 Slide Document Carousel (PDF Deck Outline)**:
   - Slide 1 (Cover / Hook) $\rightarrow$ Slide 2 (The Hidden Bleed) $\rightarrow$ Slide 3 (The Math/Data) $\rightarrow$ Slide 4 (The Operational Shift) $\rightarrow$ Slide 5 (Side-by-Side Comparison) $\rightarrow$ Slide 6 (NETS Solution & Fleet) $\rightarrow$ Slide 7/8 (SLA, Trial Offer & CTA).
   - Includes slide-by-slide visual layout cues (colors `#0F172A`, `#EF8B3C`, typography, icon placement) and accompanying feed teaser caption.
4. **Interactive Industry Poll**:
   - Operational debate question relevant to that week's topic with 4 selectable choices and post context.
5. **Direct Prospecting & InMail Sequence**:
   - Connection Request Note (<300 characters, no sales pitch).
   - Day 3 Follow-Up Message (Corridor benchmark value drop).
   - Cold InMail Script for senior corporate decision-makers.

---

## Phase 5: Cross-Asset Audit & Progress-Tracker Update

* **Agent**: QA & Compliance Reviewer
* **Action**:
  1. Inspect all 5 deliverable files in `Cluster-[XX]/Week-[YY]/` against the verification criteria in [`Requirement.md`](file:///Users/ifeanyifelix/Desktop/ReedBreedCC/nets-drive/AGENT/Requirement.md).
  2. Confirm 100% compliance across Universal Gates (`BRD-01`, `SOC-01`, `FLT-01`, `COR-01`, `VOX-01`, `IMG-01`, `EML-01`, `LNK-01`) and format-specific checklists (`V-01` to `L-08`).
  3. Update [`Progress-Tracker.md`](file:///Users/ifeanyifelix/Desktop/ReedBreedCC/nets-drive/AGENT/Progress-Tracker.md) marking the cluster week as `[x] Delivered` with exact markdown links to the deliverable folder.
