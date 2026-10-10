# -*- coding: utf-8 -*-
"""Regenerate Xillim Scientific HTML pages with shared chrome and brief-aligned content."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

NAV = """
<header class="header"><nav class="wrap nav" aria-label="Primary navigation">
<a href="index.html" class="logo" aria-label="Xillim Scientific home"><img src="assets/logo.png" alt="Xillim Scientific"></a>
<button class="menu" aria-controls="mainnav" aria-expanded="false">Menu ☰</button>
<div class="navlinks" id="mainnav">
<div class="navitem">
<button type="button" aria-expanded="false" aria-haspopup="true">Services <span class="chev">▾</span></button>
<div class="dropdown" role="menu">
<div class="group">Biomedical &amp; Life Sciences</div>
<a href="medical-imaging.html">Advanced Medical Imaging</a>
<a href="computational-modelling.html">Computational Modelling &amp; CFD</a>
<a href="digital-pathology.html">Digital Pathology</a>
<a href="ai-validation.html">Medical AI Validation</a>
<a href="research-analytics.html">Research &amp; Clinical Development</a>
<div class="group">Manufacturing &amp; Industrial</div>
<a href="manufacturing-intelligence.html">Pharmaceutical Manufacturing Intelligence</a>
<div class="group">Earth &amp; Environmental</div>
<a href="earth-intelligence.html">Satellite &amp; Geospatial Intelligence</a>
<a href="asset-risk.html">Physical Asset &amp; Climate Risk</a>
<a href="environmental-intelligence.html">Environmental &amp; Sustainability</a>
<a href="services.html">All services overview →</a>
</div>
</div>
<a href="about.html">Approach</a>
<a href="demonstrations.html">Case Studies</a>
<a href="request.html">Contact</a>
<a class="cta" href="request.html">Request an assessment ↗</a>
</div>
</nav></header>
""".strip()

FOOTER = """
<footer class="footer"><div class="wrap footgrid">
<div>
<a class="logo" href="index.html"><img src="assets/logo.png" alt="Xillim Scientific"></a>
<p class="tagline">Scientific rigor. Independent analysis. Reproducible intelligence.</p>
<p class="muted">Independent Computational Intelligence<br>Biomedical | Pharmaceutical | AI | Earth Observation</p>
<p class="fine">© 2026 Xillim Scientific. All rights reserved. Based in Egypt · serving clients internationally.</p>
</div>
<div>
<strong>Explore</strong>
<a href="services.html">All services</a>
<a href="about.html">Our approach</a>
<a href="demonstrations.html">Demonstrations</a>
<a href="request.html">Project inquiry</a>
<a href="privacy.html">Privacy</a>
</div>
<div>
<strong>Practices</strong>
<a href="medical-imaging.html">Biomedical imaging</a>
<a href="manufacturing-intelligence.html">Pharmaceutical</a>
<a href="ai-validation.html">AI assurance</a>
<a href="earth-intelligence.html">Earth intelligence</a>
<a href="asset-risk.html">Asset risk</a>
</div>
</div></footer>
<script src="assets/site.js" defer></script>
""".strip()


def page(title, description, body, og_title=None):
    og_title = og_title or title
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#090D1C">
<meta name="description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="assets/banner.png">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="stylesheet" href="assets/site.css">
<title>{title}</title>
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
{NAV}
<main id="main">
{body}
</main>
{FOOTER}
</body>
</html>
"""


def service_page(
    title,
    description,
    practice,
    h1,
    tagline,
    intro,
    capabilities,
    deliverables,
    disclaimer,
    clients="",
):
    caps = "\n".join(f"<li>{c}</li>" for c in capabilities)
    dels = "\n".join(f"<li>{d}</li>" for d in deliverables)
    clients_block = (
        f'<div class="callout reveal"><strong>Typical clients:</strong> {clients}</div>'
        if clients
        else ""
    )
    body = f"""
<section class="pagehero">
<div class="wrap">
<div class="eyebrow reveal">{practice}</div>
<h1 class="reveal reveal-delay-1">{h1}</h1>
<p class="lead reveal reveal-delay-2">{tagline}</p>
<p class="muted reveal reveal-delay-3">{intro}</p>
<div class="actions reveal reveal-delay-4">
<a class="button" href="request.html">Discuss an assessment ↗</a>
<a class="button secondary" href="services.html">All services</a>
</div>
</div>
</section>
<section class="section">
<div class="wrap two">
<div class="panel reveal">
<h3>What we can investigate</h3>
<ul class="bullet">{caps}</ul>
</div>
<div>
<div class="panel reveal reveal-delay-1">
<h3>Typical deliverables</h3>
<ul class="bullet">{dels}</ul>
</div>
<div class="callout reveal reveal-delay-2"><strong>Scope and limitations:</strong> {disclaimer}</div>
{clients_block}
</div>
</div>
</section>
<section class="section alt">
<div class="wrap">
<div class="bannercta reveal">
<div>
<div class="eyebrow">Independent analysis</div>
<h2>Have a project in this area?</h2>
<p class="muted">Describe your question and available non-confidential data. We will review feasibility and propose a suitable analytical scope.</p>
</div>
<a class="button" href="request.html">Request an assessment ↗</a>
</div>
</div>
</section>
"""
    return page(f"{title} | Xillim Scientific", description, body, f"{title} | Xillim Scientific")


SERVICES = {
    "medical-imaging.html": dict(
        title="Advanced Medical Imaging",
        description="Quantitative MRI analysis, QSM reconstruction, segmentation and imaging biomarkers for research use.",
        practice="Biomedical &amp; Life Sciences",
        h1="Advanced Medical Imaging &amp; Quantitative Image Analysis",
        tagline="Quantitative imaging beyond conventional reporting.",
        intro="We provide advanced medical image processing and quantitative analysis for biomedical research, clinical research, academic institutions, medical device development and medical imaging AI research—extracting reproducible quantitative information from existing medical images.",
        capabilities=[
            "Quantitative Susceptibility Mapping (QSM) reconstruction and analysis",
            "MRI relaxometry including T1, T2 and T2* mapping",
            "Diffusion MRI and diffusion-derived metrics",
            "Brain segmentation and regional volumetry",
            "Longitudinal neuroimaging and anatomical change analysis",
            "Organ and tumor segmentation, volumetry and lesion tracking",
            "Medical image registration and 3D anatomical reconstruction",
            "Radiomics, texture analysis and quantitative imaging biomarkers",
            "Tissue characterization, QC and research-ready image datasets",
        ],
        deliverables=[
            "Quantitative maps, measurements and segmentation masks",
            "Imaging biomarker tables and statistical analyses",
            "3D anatomical models and scientific reports",
            "Reproducible computational workflows",
        ],
        disclaimer="Research use only on authorized, appropriately de-identified datasets. Not an independent clinical diagnostic service.",
        clients="Researchers, universities, hospitals, CROs, imaging laboratories and MedTech companies.",
    ),
    "computational-modelling.html": dict(
        title="Image-Based Computational Modelling &amp; CFD",
        description="Patient-specific biomedical CFD simulation, mesh generation and model credibility assessment from CT/MRI.",
        practice="Biomedical &amp; Life Sciences",
        h1="Patient-Specific Computational Modelling &amp; Fluid Dynamics",
        tagline="From medical images to credible physiological simulations.",
        intro="Biomedical computational modelling based on patient-specific imaging—converting CT/MRI anatomy into simulation-ready models for research in hemodynamics, respiratory flow and biomedical devices.",
        capabilities=[
            "CT/MRI-derived anatomical segmentation and reconstruction",
            "Patient-specific vessel, cardiac and airway geometries",
            "Watertight surface meshes and volume meshing for CFD",
            "Boundary identification, labelling and physiological boundary conditions",
            "Hemodynamic and respiratory airflow simulation",
            "Pressure, velocity and wall shear stress analysis",
            "Mesh independence, sensitivity analysis and solver verification",
            "Model validation and uncertainty quantification informed by ASME V&amp;V 40",
            "Biomedical device research and treatment-planning research support",
        ],
        deliverables=[
            "Simulation-ready geometries, surface and volume meshes",
            "CFD results, flow visualizations and quantitative reports",
            "Verification, validation and uncertainty evidence",
            "Reproducible simulation workflows",
        ],
        disclaimer="Patient-specific simulations are for research and engineering evaluation, not autonomous clinical decision-making.",
        clients="Biomedical researchers, medical device developers, hospitals, engineering research teams and universities.",
    ),
    "digital-pathology.html": dict(
        title="Digital Pathology &amp; Microscopy Analytics",
        description="Whole-slide image analysis, IHC quantification and quantitative tissue intelligence for research.",
        practice="Biomedical &amp; Life Sciences",
        h1="Digital Pathology, Microscopy &amp; Quantitative Tissue Intelligence",
        tagline="Quantify tissue, cells and their spatial organization.",
        intro="Independent biomedical image analysis across whole-slide histology, immunohistochemistry and microscopy—producing quantitative tissue intelligence for research programs.",
        capabilities=[
            "Whole-slide image analysis, tissue segmentation and classification",
            "Cell detection, counting and morphology analysis",
            "Immunohistochemistry (IHC) quantification and stain normalization",
            "Tumor microenvironment and cell-neighborhood analysis",
            "Histological structure quantification and spatial organization",
            "Fluorescence and multi-channel microscopy processing",
            "Quantitative pathology biomarkers and batch image processing",
            "Pathology image quality assessment",
        ],
        deliverables=[
            "Tissue masks, cellular measurements and annotated images",
            "Quantitative image tables and spatial analyses",
            "Statistical reports and research-ready pathology datasets",
        ],
        disclaimer="Research-use analytics on appropriately authorized, de-identified datasets.",
        clients="Pathology laboratories, universities, research institutes, hospitals, CROs and biomedical AI developers.",
    ),
    "ai-validation.html": dict(
        title="Independent Medical &amp; Biomedical AI Validation",
        description="Independent medical AI validation, benchmarking, robustness and model assurance.",
        practice="AI &amp; Research Assurance",
        h1="Independent AI Validation, Benchmarking &amp; Model Assurance",
        tagline="Models should earn trust beyond their original dataset.",
        intro="AI performance on one dataset does not guarantee performance across scanners, laboratories, populations or protocols. We independently evaluate how well biomedical AI systems generalize and where limitations become significant.",
        capabilities=[
            "Independent model performance benchmarking",
            "Classification, segmentation and detection evaluation",
            "Sensitivity, specificity, precision, recall and calibration analysis",
            "Cross-dataset, cross-site and scanner/acquisition variability",
            "Stain and microscopy protocol variation; dataset shift",
            "Subgroup performance, failure-mode and leakage assessment",
            "Statistical agreement, repeatability and reproducibility",
            "Model-version regression testing and lifecycle assurance",
            "Dataset quality and label consistency analysis",
        ],
        deliverables=[
            "Model evaluation reports and robustness analyses",
            "Statistical validation metrics and failure-mode dossiers",
            "Reproducible benchmark pipelines and technical recommendations",
        ],
        disclaimer="Technical assessment does not itself constitute regulatory certification, FDA approval or clinical validation.",
        clients="Medical AI developers, MedTech companies, research laboratories, biomedical startups, CROs and research institutions.",
    ),
    "manufacturing-intelligence.html": dict(
        title="Pharmaceutical &amp; Biopharmaceutical Intelligence",
        description="Pharmaceutical manufacturing data analytics, CPV, multivariate process intelligence without modifying validated systems.",
        practice="Manufacturing Intelligence",
        h1="Independent Pharmaceutical Manufacturing &amp; Process Intelligence",
        tagline="Discover latent relationships within process and batch data.",
        intro="Modern manufacturing systems generate substantial operational data. We independently analyze authorized exports to help identify variability, critical relationships, anomalies and opportunities for improved process understanding—without modifying validated production systems.",
        capabilities=[
            "Multivariate manufacturing process and batch-to-batch analysis",
            "CPP/CQA relationships and latent process parameter identification",
            "Continued Process Verification (CPV) and process drift detection",
            "Time-series anomaly detection and deviation recurrence support",
            "Root-cause hypothesis analysis and cross-system correlation",
            "Fermentation, cell-culture, purification and downstream analytics",
            "Environmental monitoring and aseptic manufacturing analytics",
            "SPC, process modelling, sensitivity analysis and AI/ML assurance",
            "Integration of MES, LIMS, QMS, ERP, historian and SCADA exports",
        ],
        deliverables=[
            "Process intelligence and multivariate statistical reports",
            "CPP/CQA, drift and deviation trend assessments",
            "Predictive-model evaluations and reproducible workflows",
        ],
        disclaimer="Uses authorized datasets or controlled interfaces. Does not automatically replace formal GMP investigations, validation responsibilities or regulatory quality decisions.",
        clients="Pharmaceutical manufacturers, biopharmaceutical companies, CDMOs, process development and quality organizations.",
    ),
    "research-analytics.html": dict(
        title="Research &amp; Clinical Development Analytics",
        description="Quantitative imaging endpoints, longitudinal analysis and research analytics for universities and CROs.",
        practice="AI &amp; Research Assurance",
        h1="Quantitative Research, Clinical Study &amp; Development Analytics",
        tagline="Reproducible computational evidence for research.",
        intro="Support research groups and CROs with quantitative imaging endpoints, longitudinal studies, multimodal biomedical datasets and independent algorithm evaluation under appropriate study governance.",
        capabilities=[
            "Quantitative imaging endpoint development and biomarkers",
            "Longitudinal imaging analysis and measurement validation",
            "Centralized imaging and pathology data workflows",
            "Multimodal biomedical data analysis",
            "Clinical research statistical analysis and data quality assessment",
            "Reproducible research pipelines and dataset preparation",
            "Independent biomedical algorithm evaluation",
        ],
        deliverables=[
            "Analysis-ready datasets and endpoint tables",
            "Statistical summaries and methods documentation",
            "Research workflow documentation",
        ],
        disclaimer="Subject to applicable research approval, privacy protections and study-specific requirements.",
        clients="Universities, CROs, clinical research teams, hospitals, research institutes, pharmaceutical R&amp;D and MedTech developers.",
    ),
    "earth-intelligence.html": dict(
        title="Satellite &amp; Earth Observation Intelligence",
        description="Satellite image analysis, Sentinel/Landsat processing, SAR/InSAR and geospatial change detection.",
        practice="Earth &amp; Asset Intelligence",
        h1="Satellite Image Analysis &amp; Earth Observation Intelligence",
        tagline="Make the Earth’s observable history actionable.",
        intro="By combining optical, multispectral, radar and environmental datasets, we reconstruct physical changes, detect anomalies and quantify geospatial patterns from publicly accessible and appropriately licensed Earth observation data.",
        capabilities=[
            "Sentinel-1 SAR and Sentinel-2 multispectral analysis",
            "Landsat historical imagery and optical time-series",
            "Cloud masking, atmospheric correction and geospatial alignment",
            "Image classification, segmentation and change detection",
            "SAR/InSAR deformation screening where data support it",
            "Land-use/land-cover, urban expansion and construction change",
            "NDVI, NDMI, NDRE and agricultural/water intelligence",
            "Shoreline, water-body and large-area infrastructure monitoring",
        ],
        deliverables=[
            "Change-detection maps, time series and GIS-ready datasets",
            "Geospatial analytical reports and spatial statistics",
            "Risk/anomaly maps and reproducible processing results",
        ],
        disclaimer="Remote sensing provides indirect measurements; site conditions require appropriate validation.",
        clients="Investors, agricultural businesses, infrastructure groups, environmental consultancies and research institutions.",
    ),
    "asset-risk.html": dict(
        title="Physical Asset, Geohazard &amp; Climate Risk",
        description="Independent physical asset risk screening using satellite, terrain, seismic and climate datasets.",
        practice="Earth &amp; Asset Intelligence",
        h1="Independent Physical Asset &amp; Geospatial Risk Intelligence",
        tagline="Screen physical risk before it becomes an asset decision.",
        intro="We combine satellite imagery, radar observations, terrain models, seismic hazard data and climate datasets to assess independently observable physical risks associated with land, real estate and infrastructure.",
        capabilities=[
            "Regional seismic hazard and ground-motion exposure screening",
            "Satellite-derived ground deformation, subsidence and uplift",
            "Terrain, slope and land-instability indicators",
            "Flood, coastal, extreme-heat and drought exposure screening",
            "Historical site condition and surrounding development monitoring",
            "Multi-hazard screening and portfolio exposure comparison",
            "Geospatial due-diligence evidence for investment review",
            "Loss sensitivity under explicitly stated assumptions when data allow",
        ],
        deliverables=[
            "Asset physical-risk screening dossiers",
            "Multi-hazard maps and evidence registers",
            "Uncertainty statements and investigation priorities",
        ],
        disclaimer="Satellite observations cannot establish structural safety, hidden foundations, legal ownership, regulatory compliance or market valuation. InSAR measures radar line-of-sight displacement, not automatic proof of structural damage. Formal engineering certification and property valuation are outside standard scope.",
        clients="Real estate investors, developers, financial institutions, insurers, infrastructure owners and engineering consultancies.",
    ),
    "environmental-intelligence.html": dict(
        title="Environmental &amp; Sustainability Evidence",
        description="Environmental change detection, climate exposure and sustainability evidence from Earth observation.",
        practice="Earth &amp; Asset Intelligence",
        h1="Environmental Change, Climate Exposure &amp; Sustainability Evidence",
        tagline="Measure environmental change, not just claims.",
        intro="We use Earth observation, environmental datasets and quantitative analysis to examine observable environmental change and climate-related risk—with transparent evidence quality and uncertainty reporting.",
        capabilities=[
            "Long-term land-cover, vegetation and ecosystem indicators",
            "Water-body, wetland, coastal and surface-temperature analysis",
            "Historical temperature/precipitation trends and extreme-heat analysis",
            "Drought, flood-hazard exposure and climate scenario screening",
            "Satellite-derived atmospheric pollutant indicators where resolution permits",
            "Environmental baselines and land-use impact assessment",
            "Observable sustainability claim assessment with uncertainty reporting",
        ],
        deliverables=[
            "Environmental timeline and exposure maps",
            "Evidence and data-quality reports",
            "Reproducible geospatial outputs",
        ],
        disclaimer="Satellite observations do not independently provide verified facility-level Scope 1, 2 or 3 carbon inventories or a complete ESG rating.",
        clients="Investors, environmental consultancies, sustainability teams, real estate developers, infrastructure groups and research institutions.",
    ),
}


INDEX = """
<section class="hero hero-animate">
<span class="orb a" aria-hidden="true"></span>
<span class="orb b" aria-hidden="true"></span>
<div class="wrap">
<div class="eyebrow">Independent Computational Intelligence · Biomedical, Pharmaceutical, AI &amp; Earth</div>
<h1>Data Contains More Intelligence<br><span class="grad">Than Most Organizations Extract.</span></h1>
<p class="lead">A medical image contains more than its clinical report. Manufacturing historians record process behaviour routine monitoring may never explain. Satellite observations reveal years of change. AI models produce predictions whose reliability must be independently established.</p>
<p class="lead" style="margin-top:14px;font-size:17px">We transform these complex datasets into quantitative, reproducible scientific evidence and actionable intelligence.</p>
<div class="actions">
<a class="button" href="services.html">Explore Our Services ↗</a>
<a class="button secondary" href="request.html">Request a Project Assessment</a>
</div>
<div class="strip" style="margin-top:43px">
<span>Biomedical imaging</span><span>AI validation</span><span>Pharma intelligence</span><span>Earth observation</span>
</div>
</div>
</section>

<section class="section">
<div class="wrap">
<div class="sectionhead reveal">
<div class="eyebrow">Our core expertise</div>
<h2>Four practices. One evidence-driven philosophy.</h2>
<p class="muted">Turning complex data into reliable scientific evidence and actionable intelligence—without selling scanners, proprietary models or imagery subscriptions.</p>
</div>
<div class="grid cards4">
<a class="card reveal" href="medical-imaging.html"><div class="num">01</div><h3>Biomedical Imaging &amp; Modelling</h3><p>Quantitative medical imaging, patient-specific modelling, CFD and biological imaging analytics.</p><span class="more">Explore ↗</span></a>
<a class="card reveal reveal-delay-1" href="ai-validation.html"><div class="num">02</div><h3>Independent AI Validation &amp; Research</h3><p>AI benchmarking, robustness, reproducibility, imaging biomarkers and research analytics.</p><span class="more">Explore ↗</span></a>
<a class="card reveal reveal-delay-2" href="manufacturing-intelligence.html"><div class="num">03</div><h3>Pharmaceutical Intelligence</h3><p>Multivariate process analysis, CPV, bioprocess analytics and operational intelligence.</p><span class="more">Explore ↗</span></a>
<a class="card reveal reveal-delay-3" href="earth-intelligence.html"><div class="num">04</div><h3>Earth Observation &amp; Asset Intelligence</h3><p>Satellite analytics, SAR/InSAR, environmental change, climate exposure and geohazard screening.</p><span class="more">Explore ↗</span></a>
</div>
</div>
</section>

<section class="section alt">
<div class="wrap split">
<div class="reveal">
<div class="eyebrow">Our analytical approach</div>
<h2>From acquisition to actionable intelligence.</h2>
<p class="lead">Every engagement prioritizes reproducibility, traceability, appropriate modelling assumptions, quantified uncertainty and defensible scientific conclusions.</p>
<p class="muted">Vendor-neutral. Scientifically defensible. We work with authorized existing data and public observations without replacing your systems.</p>
<div class="actions"><a class="button" href="about.html">How we work →</a></div>
</div>
<div class="visual reveal reveal-delay-2">
<span class="eyebrow">Workflow</span>
<div>Data → Quality → Analysis → Validation → Evidence → <span class="grad">Intelligence</span></div>
<small>Documented provenance · Transparent uncertainty · Decision-ready reports</small>
</div>
</div>
</section>

<section class="section">
<div class="wrap">
<div class="sectionhead reveal">
<div class="eyebrow">How projects work</div>
<h2>From complexity to clarity</h2>
</div>
<div class="steps">
<div class="step reveal">01<br>Data acquisition</div>
<div class="step reveal reveal-delay-1">02<br>Quality assessment</div>
<div class="step reveal reveal-delay-2">03<br>Computational analysis</div>
<div class="step reveal reveal-delay-3">04<br>Scientific validation</div>
<div class="step reveal reveal-delay-4">05<br>Reproducible evidence</div>
<div class="step reveal">06<br>Actionable intelligence</div>
</div>
</div>
</section>

<section class="section alt">
<div class="wrap">
<div class="sectionhead reveal">
<div class="eyebrow">Industries we serve</div>
<h2>Technical decision-makers across science and industry.</h2>
<p class="muted">Engagements for research collaborations, pilot studies, independent assessments and ongoing consulting.</p>
</div>
<div class="industries reveal">
<span>Universities &amp; research institutes</span>
<span>Hospitals &amp; biomedical research</span>
<span>CROs</span>
<span>Pharma &amp; biopharma manufacturers</span>
<span>MedTech &amp; medical AI developers</span>
<span>Agricultural businesses &amp; investors</span>
<span>Real estate &amp; asset owners</span>
<span>Financial institutions &amp; insurers</span>
<span>Infrastructure &amp; renewable energy</span>
<span>Environmental consultancies</span>
</div>
</div>
</section>

<section class="section">
<div class="wrap">
<div class="bannercta reveal">
<div>
<div class="eyebrow">Discuss your project</div>
<h2>Have a complex dataset or model needing independent evaluation?</h2>
<p class="muted">We welcome research collaborations and consulting engagements in Egypt, the Middle East &amp; GCC, Europe and international remote projects.</p>
</div>
<a class="button" href="request.html">Discuss Your Project ↗</a>
</div>
</div>
</section>
"""

SERVICES_OVERVIEW = """
<section class="pagehero">
<div class="wrap">
<div class="eyebrow reveal">Specialized practices</div>
<h1 class="reveal reveal-delay-1">Scientific services across complex systems.</h1>
<p class="lead reveal reveal-delay-2">Independent computational intelligence across biomedicine, pharmaceutical manufacturing, AI assurance and Earth observation—delivered as scoped analytical engagements.</p>
</div>
</section>
<section class="section">
<div class="wrap">
<div class="sectionhead reveal"><div class="eyebrow">Biomedical &amp; Life Sciences</div><h2>Imaging, simulation and quantitative pathology.</h2></div>
<div class="grid">
<a class="card reveal" href="medical-imaging.html"><div class="num">Biomedical</div><h3>Advanced Medical Imaging</h3><p>Quantitative imaging beyond conventional reporting.</p><span class="more">Explore service ↗</span></a>
<a class="card reveal reveal-delay-1" href="computational-modelling.html"><div class="num">Biomedical</div><h3>Computational Modelling &amp; CFD</h3><p>From medical images to credible physiological simulations.</p><span class="more">Explore service ↗</span></a>
<a class="card reveal reveal-delay-2" href="digital-pathology.html"><div class="num">Biomedical</div><h3>Digital Pathology &amp; Microscopy</h3><p>Quantify tissue, cells and spatial organization.</p><span class="more">Explore service ↗</span></a>
</div>
<div class="grid" style="margin-top:20px">
<a class="card reveal" href="ai-validation.html"><div class="num">AI &amp; Research</div><h3>Independent Medical AI Validation</h3><p>Models should earn trust beyond their original dataset.</p><span class="more">Explore service ↗</span></a>
<a class="card reveal reveal-delay-1" href="research-analytics.html"><div class="num">AI &amp; Research</div><h3>Research &amp; Clinical Development</h3><p>Reproducible computational evidence for research.</p><span class="more">Explore service ↗</span></a>
<a class="card reveal reveal-delay-2" href="manufacturing-intelligence.html"><div class="num">Manufacturing</div><h3>Pharmaceutical Intelligence</h3><p>Latent relationships within process and batch data.</p><span class="more">Explore service ↗</span></a>
</div>
</div>
</section>
<section class="section alt">
<div class="wrap">
<div class="sectionhead reveal"><div class="eyebrow">Earth &amp; Environmental Intelligence</div><h2>Spatial change, physical risk and sustainability evidence.</h2></div>
<div class="grid">
<a class="card reveal" href="earth-intelligence.html"><div class="num">Earth</div><h3>Satellite &amp; Earth Observation</h3><p>Make the Earth’s observable history actionable.</p><span class="more">Explore service ↗</span></a>
<a class="card reveal reveal-delay-1" href="asset-risk.html"><div class="num">Earth</div><h3>Physical Asset &amp; Climate Risk</h3><p>Screen physical risk before it becomes an asset decision.</p><span class="more">Explore service ↗</span></a>
<a class="card reveal reveal-delay-2" href="environmental-intelligence.html"><div class="num">Earth</div><h3>Environmental &amp; Sustainability</h3><p>Measure environmental change, not just claims.</p><span class="more">Explore service ↗</span></a>
</div>
</div>
</section>
"""

ABOUT = """
<section class="pagehero">
<div class="wrap">
<div class="eyebrow reveal">Our mission</div>
<h1 class="reveal reveal-delay-1">Data contains more intelligence than most organizations extract.</h1>
<p class="lead reveal reveal-delay-2">Our work is built on a simple principle: organizations frequently generate more useful data than they are able to interpret. We provide the independent scientific and computational expertise required to convert that data into reliable evidence.</p>
</div>
</section>
<section class="section">
<div class="wrap split">
<div class="prose reveal">
<div class="eyebrow">Why Xillim</div>
<h2>Independent by design.</h2>
<p>We connect biomedical engineering, quantitative data analysis, medical imaging, computational modelling, AI/ML, pharmaceutical process systems, multivariate analytics and remote sensing—without commercial incentives to promote particular scanners, models or platforms.</p>
<p>We do not sell scanners, medical devices, proprietary AI models or satellite imagery subscriptions. We work with existing data and systems to deliver scientifically defensible analyses.</p>
</div>
<div class="visual reveal reveal-delay-2">
<span class="eyebrow">Xillim principle</span>
<div>Science before claims.<br>Evidence before <span class="grad">decisions.</span></div>
<small>Independent · Quantitative · Reproducible · Transparent</small>
</div>
</div>
</section>
<section class="section alt">
<div class="wrap">
<div class="sectionhead reveal"><div class="eyebrow">Our principles</div><h2>How we work</h2></div>
<div class="grid cards2">
<div class="panel reveal"><h3>Scientific rigor</h3><p>Established computational, statistical and engineering methods appropriate to each problem.</p></div>
<div class="panel reveal reveal-delay-1"><h3>Reproducibility</h3><p>Documented assumptions, datasets, processing parameters, software versions and methods.</p></div>
<div class="panel reveal reveal-delay-2"><h3>Independent assessment</h3><p>No commercial incentive to promote particular scanners, AI models, imagery vendors or platforms.</p></div>
<div class="panel reveal"><h3>Transparent uncertainty</h3><p>Clear communication of the limits of observations and models.</p></div>
<div class="panel reveal reveal-delay-1"><h3>Practical intelligence</h3><p>Analyses that answer specific scientific, engineering, operational or investment questions.</p></div>
<div class="panel reveal reveal-delay-2"><h3>Responsible data handling</h3><p>Authorized data, appropriate confidentiality and domain-specific quality requirements.</p></div>
</div>
</div>
</section>
<section class="section">
<div class="wrap">
<div class="sectionhead reveal"><div class="eyebrow">Geographic coverage</div><h2>Egypt-based. Internationally accessible.</h2>
<p class="muted">Research and consulting engagements across Egypt, the Middle East &amp; GCC, Europe and international remote collaborations. We do not imply physical local offices in every region.</p>
</div>
</div>
</section>
<section class="section alt">
<div class="wrap">
<div class="sectionhead reveal"><div class="eyebrow">FAQ</div><h2>Common questions</h2></div>
<div class="faq">
<details class="reveal"><summary>Do you work with existing datasets?</summary><p>Yes. We typically work with authorized exports, public Earth observation data and appropriately controlled interfaces—without requiring installation of a new platform.</p></details>
<details class="reveal"><summary>Do you require software installation in our organization?</summary><p>Usually no. Many engagements use secure data transfer of authorized exports. Where interfaces are needed, they are scoped carefully and do not replace validated systems.</p></details>
<details class="reveal"><summary>Can you independently validate an existing AI model?</summary><p>Yes. We provide technical benchmarking, robustness and generalization assessment. This is not regulatory certification unless separately authorized studies are in place.</p></details>
<details class="reveal"><summary>Can you support pharmaceutical manufacturing without modifying validated systems?</summary><p>Yes. Analysis uses authorized datasets or controlled interfaces; formal GMP decisions remain with the responsible organization.</p></details>
<details class="reveal"><summary>Can you analyze publicly available satellite data?</summary><p>Yes—for example Sentinel and Landsat—plus other appropriately licensed sources when available.</p></details>
<details class="reveal"><summary>What is needed for an asset-risk assessment?</summary><p>Typically site location or asset polygons, the hazard questions of interest, and any available contextual site information. Structural certification and legal due diligence remain outside satellite-intelligence scope.</p></details>
<details class="reveal"><summary>How is confidentiality handled?</summary><p>Share only non-confidential summaries at inquiry stage. Formal confidentiality arrangements can be agreed before sensitive data transfer.</p></details>
<details class="reveal"><summary>How do pilot projects work?</summary><p>We define a focused question, assess data fitness, deliver a scoped analysis with explicit methods and limitations, then decide whether to extend the engagement.</p></details>
</div>
</div>
</section>
<section class="section">
<div class="wrap"><div class="bannercta reveal"><div><div class="eyebrow">Next step</div><h2>Discuss a collaboration</h2><p class="muted">Tell us about your scientific question or dataset.</p></div><a class="button" href="request.html">Request an assessment ↗</a></div></div>
</section>
"""

REQUEST = """
<section class="pagehero">
<div class="wrap">
<div class="eyebrow reveal">Project inquiries</div>
<h1 class="reveal reveal-delay-1">Discuss Your Data, Research or Intelligence Project</h1>
<p class="lead reveal reveal-delay-2">Tell us about your scientific question, dataset, computational modelling requirement or intelligence assessment. We review potential collaborations, research projects, pilot engagements and independent consulting assignments.</p>
</div>
</section>
<section class="section">
<div class="wrap two">
<div class="panel reveal">
<h3>Request an assessment</h3>
<p class="small muted">The form prepares an email in your mail application. Do not include sensitive, identifiable patient data or confidential manufacturing records.</p>
<form class="form" id="inquiry" data-email="mu.elsayeh@gmail.com">
<div class="formrow">
<div><label for="person">Full name *</label><input id="person" name="Name" autocomplete="name" required></div>
<div><label for="email">Professional email *</label><input id="email" type="email" name="Email" autocomplete="email" required></div>
</div>
<div class="formrow">
<div><label for="organization">Organization or institution</label><input id="organization" name="Organization"></div>
<div><label for="country">Country</label><input id="country" name="Country"></div>
</div>
<div class="formrow">
<div><label for="industry">Industry</label>
<select id="industry" name="Industry">
<option value="">Select if applicable</option>
<option>University / research</option><option>Hospital / biomedical</option><option>CRO</option>
<option>Pharmaceutical / biopharma</option><option>MedTech / medical AI</option>
<option>Agriculture / investment</option><option>Real estate / infrastructure</option>
<option>Finance / insurance</option><option>Environmental consultancy</option><option>Other</option>
</select></div>
<div><label for="service">Requested service *</label>
<select id="service" name="Service" required>
<option value="">Choose a service</option>
<option>Advanced Medical Imaging</option>
<option>Computational Modelling &amp; CFD</option>
<option>Digital Pathology</option>
<option>Independent Medical AI Validation</option>
<option>Pharmaceutical Manufacturing Intelligence</option>
<option>Research &amp; Clinical Development Analytics</option>
<option>Satellite &amp; Geospatial Intelligence</option>
<option>Physical Asset &amp; Climate Risk</option>
<option>Environmental &amp; Sustainability Intelligence</option>
<option>Other / Custom Computational Analysis</option>
</select></div>
</div>
<div><label for="scope">Project description &amp; objectives *</label>
<textarea id="scope" name="Project description" required placeholder="Describe the research question, analytical problem or project goal. Do not submit confidential details."></textarea></div>
<div class="formrow">
<div><label for="data">Data available (optional)</label><input id="data" name="Data available" placeholder="e.g. de-identified MRI, process CSV, site coordinates"></div>
<div><label for="datasize">Approximate dataset size or area</label><input id="datasize" name="Dataset size or area" placeholder="e.g. 40 cases, 2 years of batches, 50 ha"></div>
</div>
<div class="formrow">
<div><label for="deliverables">Expected deliverables</label><input id="deliverables" name="Expected deliverables" placeholder="e.g. report, maps, biomarker table"></div>
<div><label for="time">Preferred timeline</label>
<select id="time" name="Timeline">
<option>Flexible / to discuss</option><option>Within 2 weeks</option><option>Within 1 month</option>
<option>1–3 months</option><option>Longer collaboration</option>
</select></div>
</div>
<div class="formrow">
<div><label for="budget">Optional budget range</label>
<select id="budget" name="Budget range">
<option value="">Prefer not to say</option>
<option>Exploratory / pilot</option><option>Focused assessment</option>
<option>Multi-phase collaboration</option><option>To discuss</option>
</select></div>
<div><label for="comm">Preferred communication</label>
<select id="comm" name="Preferred communication">
<option>Email</option><option>Video call</option><option>Either</option>
</select></div>
</div>
<label class="check"><input type="checkbox" id="consent" name="consent" required>
<span class="small">I understand this opens an email request for inquiry processing and will not include sensitive or identifiable data. See our <a href="privacy.html" style="color:var(--mint)">privacy notice</a>.</span></label>
<button class="button" type="submit">Prepare email request ↗</button>
<div class="formstatus" aria-live="polite"></div>
</form>
</div>
<div>
<div class="panel reveal reveal-delay-1">
<h3>Before you inquire</h3>
<p>For healthcare datasets, provide only authorized, de-identified summaries at this stage. For industrial projects, do not share confidential exports until suitable arrangements are in place.</p>
</div>
<div class="panel reveal reveal-delay-2" style="margin-top:20px">
<h3>Typical engagement formats</h3>
<ul class="bullet">
<li>Focused analytical assessment</li>
<li>Proof-of-concept or pilot project</li>
<li>Independent technical validation</li>
<li>Research collaboration</li>
<li>Recurring intelligence engagement</li>
</ul>
</div>
<div class="callout reveal" style="margin-top:20px">Business contact details will be published when a dedicated company email is available. Inquiries currently route privately via the prepared email request.</div>
</div>
</div>
</section>
"""

DEMONSTRATIONS = """
<section class="pagehero">
<div class="wrap">
<div class="eyebrow reveal">Examples of what we can do</div>
<h1 class="reveal reveal-delay-1">Demonstration concepts &amp; analytical workflows.</h1>
<p class="lead reveal reveal-delay-2">These examples describe proposed workflows rather than completed client projects. Actual sample analyses will be added when available. All visuals would be illustrative until real work is published.</p>
</div>
</section>
<section class="section">
<div class="wrap grid">
<div class="card reveal"><div class="num">Illustrative research workflow</div><h3>Quantitative MRI &amp; Biomarkers</h3><p>MRI acquisition → QSM/volumetry → quantitative measures and QC.</p></div>
<div class="card reveal reveal-delay-1"><div class="num">Illustrative validation design</div><h3>Medical AI Generalization</h3><p>External datasets → subgroup and acquisition shifts → independent performance evidence.</p></div>
<div class="card reveal reveal-delay-2"><div class="num">Illustrative analytics study</div><h3>Manufacturing Batch Variability</h3><p>Historian exports → multivariate trends → deviations and investigation hypotheses.</p></div>
<div class="card reveal"><div class="num">Illustrative Earth observation</div><h3>Satellite Land Change</h3><p>Multi-date satellite scenes → validated land-cover change → dated evidence maps.</p></div>
<div class="card reveal reveal-delay-1"><div class="num">Illustrative geospatial project</div><h3>Physical Asset Hazard Screening</h3><p>Asset polygon → ground, flood and seismic hazards → evidence-led risk screening.</p></div>
<div class="card reveal reveal-delay-2"><div class="num">Illustrative simulation workflow</div><h3>Patient-Specific CFD</h3><p>CT/MRI segmentation → quality mesh → flow simulation and V&amp;V checks.</p></div>
</div>
</section>
<section class="section alt"><div class="wrap"><div class="bannercta reveal"><div><h2>Propose a demonstration scope</h2><p class="muted">Tell us which workflow you want explored first.</p></div><a class="button" href="request.html">Request an assessment ↗</a></div></div></section>
"""

PRIVACY = """
<section class="pagehero">
<div class="wrap">
<div class="eyebrow reveal">Legal</div>
<h1 class="reveal reveal-delay-1">Privacy notice</h1>
<p class="lead reveal reveal-delay-2">Placeholder privacy notice for launch. Replace with a full policy before collecting personal data at scale.</p>
</div>
</section>
<section class="section">
<div class="wrap prose reveal" style="max-width:800px">
<p>When you use the project inquiry form, you may provide contact and project information. That information is used only to evaluate and respond to your inquiry.</p>
<p>Do not submit patient-identifiable health information, confidential manufacturing records or other sensitive personal data through the public form.</p>
<p>Email prepared by the form is sent via your own email application. Until a business email and formal processing system are in place, treat inquiries as private correspondence.</p>
<p>For privacy questions, contact us through the <a href="request.html" style="color:var(--mint)">inquiry form</a>.</p>
</div>
</section>
"""


def main():
    pages = {
        "index.html": page(
            "Independent Computational Intelligence | Xillim Scientific",
            "Xillim Scientific provides independent biomedical imaging, AI validation, pharmaceutical analytics, simulation and Earth observation intelligence.",
            INDEX,
        ),
        "services.html": page(
            "Services | Xillim Scientific",
            "Independent scientific and computational intelligence services across biomedicine, pharma, AI and Earth observation.",
            SERVICES_OVERVIEW,
        ),
        "about.html": page(
            "About Xillim | Xillim Scientific",
            "The mission, principles and FAQ of Xillim Scientific: independent computational intelligence.",
            ABOUT,
        ),
        "request.html": page(
            "Request an Assessment | Xillim Scientific",
            "Contact Xillim Scientific to request independent biomedical, pharmaceutical, AI or Earth intelligence analysis.",
            REQUEST,
        ),
        "demonstrations.html": page(
            "Demonstrations | Xillim Scientific",
            "Proposed computational intelligence demonstration concepts across Xillim Scientific services.",
            DEMONSTRATIONS,
        ),
        "privacy.html": page(
            "Privacy | Xillim Scientific",
            "Privacy notice placeholder for Xillim Scientific project inquiries.",
            PRIVACY,
        ),
    }
    for name, html in pages.items():
        (ROOT / name).write_text(html, encoding="utf-8")
        print("wrote", name)

    for filename, conf in SERVICES.items():
        (ROOT / filename).write_text(service_page(**conf), encoding="utf-8")
        print("wrote", filename)

    # cleanup pretty dump if present
    for tmp in ["_index_pretty.txt"]:
        p = ROOT / tmp
        if p.exists():
            p.unlink()
            print("removed", tmp)


if __name__ == "__main__":
    main()
