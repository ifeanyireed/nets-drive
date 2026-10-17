# 🚦 Requirement.md: New Era Transports Services Quality Gates & Pre-Flight Checklists

This document defines the strict, non-negotiable verification criteria that every B2B marketing, sales enablement, and corporate acquisition asset must pass before advancing to production delivery for **New Era Transports Services**.

It applies to **all 5 Corporate Clusters and 9 Months (36 Weeks)** across the NETS Corporate Acquisition Engine.

---

## 1. Universal Workflow & Architecture Gates

* [ ] **Folder Structure Compliance**: All assets for a given cluster and week must reside in:
  ```
  Cluster-[XX]/Week-[YY]/
  ```
  *(e.g., `Cluster-01/Week-01/`, `Cluster-02/Week-04/`, `Cluster-05/Week-12/`)*
* [ ] **Deliverable Files Present**: Each weekly folder must contain exactly:
  1. `video-script.md` (Stream 3: Dual-Track Skit + Executive Breakdown Video Script)
  2. `blog-post.md` (Stream 1: In-depth Bookmarkable Corporate Mobility Listicle)
  3. `email-blast.html` (Stream 2: Responsive HTML Newsletter *The NETS Corporate Mobility Dispatch*)
  4. `email-blast.md` (Stream 2: Markdown Companion Edition)
  5. `linkedin-pack.md` (Stream 4: LinkedIn B2B Acquisition Pack — ONLY social platform)
* [ ] **Brand Alignment Gate (BRD-01)**:
  - Brand identity MUST be **New Era Transports Services** (www.neweratransports.com). Strictly prohibited to use "Nets Drive" or "NETS Drive" (`https://www.neweratransports.com`).
  - Tone must reflect enterprise operational authority, logistics competence, and financial empathy.
* [ ] **Social Media Exclusivity Gate (SOC-01)**:
  - Social media content is **strictly and exclusively LinkedIn**.
  - Zero generation of content for X/Twitter, Facebook, Instagram, or TikTok.
* [ ] **LinkedIn First-Comment Link Gate (LNK-01)**:
  - **Zero outbound links in the body of any LinkedIn post**.
  - All landing page links or route audit forms must be specified in the **First Comment** block.
* [ ] **LinkedIn Character Limit Enforcement Gate (CHR-01)**:
  - **Hook before fold**: Strictly under 140 characters before the `...see more` truncation.
  - **Thought leadership body**: 1,200 to 2,000 characters.
  - **Connection request note**: Strictly under 300 characters including spaces.
* [ ] **Cluster Fleet Positioning Gate (FLT-01)**:
  - Content must pitch the designated fleet assets and service tiers specified in [`Skills.md`](file:///Users/ifeanyifelix/Desktop/ReedBreedCC/nets-drive/AGENT/Skills.md) (Toyota Coaster, HiAce, Prado TXL, IVMS telematics, standby backup).
* [ ] **Corridor Fidelity Gate (COR-01)**:
  - Scenarios must reference authentic Nigerian transport corridors (Agbara, Sagamu, Sango-Ota, Third Mainland Bridge, Lekki-Epe Expressway, Port Harcourt - Warri corridor, MMIA airport corridor).
* [ ] **Anti-Fluff Enforcement (VOX-01)**:
  - Zero occurrences of banned buzzwords (*revolutionize, seamless, game-changer, delve into, in today's fast-paced digital world, supercharge, unlock the power of, tapestry, beacon*).
* [ ] **Blog Featured Image Style Gate (IMG-01)**:
  - Blog featured image MUST follow the exact prompt style: `VISUAL FOR BLOG FEATURED IMAGE: 3D Disney Pixar style animation. Netflix-grade cinematic lighting with screen glow on faces, UHD 8k, stylized technology.` featuring cluster-appropriate African characters and Nigerian operational environments.
* [ ] **Real News & Editorial Imagery Gate (IMG-02)**:
  - Email cover story and news round-ups must contain real images from the internet covering authentic Nigerian transit and logistics developments with descriptive captions and sources.
* [ ] **HTML Email Format Gate (EML-01)**:
  - Email newsletter MUST be written in clean, production-ready, mobile-responsive HTML with inline CSS (max 600px width card).
* [ ] **Native Markdown Tables Gate (TAB-01)**:
  - All balance sheets, flow cycles, bottleneck maps, comparison matrices, and structured operational breakdowns MUST be rendered as **native GitHub Flavored Markdown (GFM) tables** (`| col1 | col2 |`).
  - **Strictly forbidden**: Raw ASCII art box drawings (`┌───┐`, `│`, `└`, `├`, etc.) and wrapping tabular financial data or balance sheets inside fenced code blocks (` ``` `). Fenced code blocks trigger dark `#0F172A` container backgrounds in preview renderers and break mobile responsiveness.
* [ ] **Clean Markdown Math & Zero Raw LaTeX Gate (MTH-01)**:
  - All operational and financial formulas MUST be rendered in **clean, readable Unicode Markdown math syntax**: e.g., `$$Total Downtime Loss = (Lateness Duration (Mins) ÷ 60) × (Direct Labor Burn + Captive Power Standby + Lost SKU Margin Yield)$$`.
  - **Strictly forbidden**: Raw LaTeX markup tokens such as `\text{...}`, `\textbf{...}`, `\frac{...}{...}`, `\left(`, `\right)`, `\times`, and subscript variables like `$C_{\text{labor}}$` in formulas, body text, or headings. Standard markdown renderers lack a full LaTeX/KaTeX engine and display raw backslashes and curly braces as unformatted code or broken text.

---

## 2. Format-Specific Quality Gates

### 2.1 🎬 Video Script Gate (`video-script.md`)

| Check ID | Verification Item | Standard Required | Pass / Fail |
| :--- | :--- | :--- | :--- |
| **V-01** | **Runtime & Word Count** | 600–650 spoken words (~4:00–4:30 runtime at 140 WPM). | [ ] |
| **V-02** | **Hybrid Format** | Clear separation between Talking Head (TH) host and corporate/industrial drama scenes in a 3-column markdown table (`Timecode | Visual Action | Audio / Dialogue`). | [ ] |
| **V-03** | **Hook Strength** | Pattern interrupt in the first 10 seconds tailored to the cluster's specific transit friction point (e.g. 5:45 AM assembly line alarm, highway breakdown, stranded retail staff). | [ ] |
| **V-04** | **Narrative Arc** | Scene 1 (Operational Crisis / Gridlock) $\rightarrow$ Scene 2 (Financial Escalation / Confrontation) $\rightarrow$ Scene 3 (Rewind with NETS Fleet). | [ ] |
| **V-05** | **Visual Contrast** | Visual contrast between the chaotic, breakdown-prone informal transit system and synchronized, GPS-tracked NETS corporate shuttles. | [ ] |
| **V-06** | **Quantitative Breakdown** | Host explains the operational downtime or productivity loss using the cluster's mathematical formula. | [ ] |
| **V-07** | **Product & Route Audit Close** | Direct CTA pitching NETS Corporate Fleet Services and offering a Free Route & Fleet Benchmark. | [ ] |
| **V-08** | **Production Notes** | Includes casting guidance, sound design cues (SFX), and a 60-second cutdown concept for TikTok/Reels. | [ ] |

---

### 2.2 📚 Bookmarkable Blog Post Gate (`blog-post.md`)

| Check ID | Verification Item | Standard Required | Pass / Fail |
| :--- | :--- | :--- | :--- |
| **B-01** | **Metadata & Structure** | H1 Title, author byline (`@Ifeanyi Felix · Corporate Mobility Strategy Lead`), publication date, read time (8–10 mins), category, and meta description. | [ ] |
| **B-02** | **Research Grounding** | Cites authoritative transport reports, verifiable Nigerian corridor data, and fuel/downtime benchmark statistics. | [ ] |
| **B-03** | **Quantitative Model & Clean Math** | Features the cluster-specific mathematical formula using clean Unicode Markdown math (zero raw LaTeX: no `\text`, `\frac`, etc.) with a detailed, realistic worked financial example in Nigerian Naira (₦). | [ ] |
| **B-04** | **10 Actionable Tactics** | Delivers exactly 10 high-utility, bookmarkable operational mobility tactics with clear implementation steps for management. | [ ] |
| **B-05** | **Corridor Anchoring** | Grounds operational routes in authentic Nigerian industrial parks, expressways, and business districts. | [ ] |
| **B-06** | **Native Comparison Table & Balance Sheet** | Includes side-by-side comparison tables and balance sheets rendered exclusively as native Markdown tables (zero ASCII art boxes, zero fenced code blocks). | [ ] |
| **B-07** | **Clear Corporate CTA** | Directs enterprise decision-makers to book a Free Route & Fleet Benchmark Audit. | [ ] |
| **B-08** | **Word Count** | Substantive long-form depth between 1,500 and 2,200 words. | [ ] |

---

### 2.3 📰 Responsive Email Newsletter Gate (`email-blast.html` & `email-blast.md`)

| Check ID | Verification Item | Standard Required | Pass / Fail |
| :--- | :--- | :--- | :--- |
| **E-01** | **Publication Identity** | Formatted as *The NETS Corporate Mobility Dispatch* with issue number, date, and editorial byline. | [ ] |
| **E-02** | **Subject Line Matrix** | 3 strategic subject line options (Pain Hook, Curiosity Hook, Metric Hook) + Preview Text under 90 chars. | [ ] |
| **E-03** | **Lead News Cover Story** | Pure journalistic reporting on an authentic Nigerian transport, fuel, infrastructure, or regulatory development, featuring a real photo and *"► WHAT IT MEANS FOR OPERATORS"* analysis. | [ ] |
| **E-04** | **Industry News Round-up** | 3 distinct, authentic industry news cards with real photos, source citations, and operator implications. | [ ] |
| **E-05** | **Mobility Hack / Metric Container** | High-contrast callout container presenting the blog's quantitative downtime/fatigue formula as the tactical response to transit inflation; in `email-blast.md`, formatted as a native Markdown table or clean blockquote (zero ASCII box code blocks). | [ ] |
| **E-06** | **Zero Corner Radius CTA Button** | Prominent corporate CTA button directing readers to read the full blog post or schedule a route review. **Must strictly feature zero corner radius (`border-radius: 0px`)** with sharp architectural corners (no rounded or pill buttons), styled in primary brand blue (`#1A48B6`) with bold white text (`#FFFFFF`) and generous padding (`14px 28px`). | [ ] |
| **E-07** | **Footer Offer** | Highlights the NETS 1-2 Route Pilot Program, SLA guarantees, and 30-day corporate billing. | [ ] |
| **E-08** | **Deliverability Hygiene** | Inline CSS, 600px responsive table layout, zero spam trigger words, and compliant corporate footer. | [ ] |
| **E-09** | **Light Executive UI Standard** | Strictly NO black or dark (`#0F172A` / `#000000` / `#1E293B`) background UI styling. All email headers, metric containers, cards, and footers must use clean light executive backgrounds (`#FFFFFF`, `#F8FAFC`, `#F1F5F9`) with high-contrast typography and brand accent borders. | [ ] |
| **E-10** | **Strict Brand Colors (`logo.png`) & Zero Corner Radius** | HTML email templates must maintain **strict compliance** exclusively with the brand colors extracted from `logo.png`: **Primary Corporate Royal Blue (`#1A48B6` / `#0F3282`)** for CTA buttons, headings, and links; **Secondary Signature Red (`#FE0B10` / `#D4080D`)** for header accent borders, category eyebrows, and alert highlights; **Crisp White (`#FFFFFF`)** and Light Neutrals (`#F8FAFC`, `#F1F5F9`) for surfaces. **Zero corner radius (`border-radius: 0px`)** is strictly required on all buttons, cards, containers, and images. The official brand logo (`logo.png`) must be reduced in size and placed **directly side-by-side with the titles** (NEVER standing alone on its own line): in the **header masthead** as a 44px square (`width="44" height="44"`) aligned side-by-side with the titles in a 2-column table row, and in the **footer legal section** as a 22px icon (`width="22" height="22"`) inline beside "New Era Transports Services". | [ ] |

---

### 2.4 💼 LinkedIn B2B Acquisition Pack Gate (`linkedin-pack.md`)

| Check ID | Verification Item | Standard Required | Pass / Fail |
| :--- | :--- | :--- | :--- |
| **L-01** | **Exclusivity Standard** | Contains **only** LinkedIn assets (Long-form post, short post, carousel outline, poll, InMail/connection note). Zero content for other social networks. | [ ] |
| **L-02** | **Hook Before the Fold** | First 1–2 lines under 140 characters that create high tension, pattern interrupt, or financial contrast before `...see more`. | [ ] |
| **L-03** | **First-Comment Link Rule** | Main post body contains **no outbound links**. Link to `www.neweratransports.com/corporate-audit` placed strictly in pinned first comment. | [ ] |
| **L-04** | **Dwell-Time Formatting** | 1–2 sentence paragraphs, generous line breaks, 5 bulleted strategic shifts, and low-friction closing discussion question. | [ ] |
| **L-05** | **Document Carousel Outline** | Exactly 6 to 8 slides formatted for PDF upload with explicit layout wireframes, contrast colors (`#0F172A`, `#EF8B3C`), and comparison slide. | [ ] |
| **L-06** | **Carousel Feed Caption** | 3–4 sentence teaser caption with bulleted takeaways accompanying the PDF upload. | [ ] |
| **L-07** | **Connection Note Length** | Strictly under 300 characters including spaces; non-sales peer benchmark angle. | [ ] |
| **L-08** | **Interactive Industry Poll** | High-relevance operational debate question with 4 clear choices to drive comments from target executives. | [ ] |

---

## 3. Pass/Fail Decision Matrix & Revision Protocol

1. **Gate Evaluation**: The Quality Assurance reviewer audits each asset against the checklist.
2. **Passing Standard**: An asset must achieve a 100% pass rate across Universal and Format-Specific gates.
3. **Revision Loop**:
   * If any check fails (e.g. hook over 140 chars or link in post body), the reviewer logs the specific deficiency.
   * The authoring agent revises the asset immediately.
   * Only upon passing all checks may the step be marked `[x] Delivered` in `Progress-Tracker.md`.
