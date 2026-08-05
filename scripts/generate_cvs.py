from pathlib import Path
import shutil
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    Image,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf"
PORTRAIT = ROOT / "assets" / "paul-freyhofer-portrait.jpg"

ACCENT = colors.HexColor("#A95533")
INK = colors.HexColor("#18201D")
MUTED = colors.HexColor("#636860")
PAPER = colors.HexColor("#FFFCF6")
LINE = colors.HexColor("#D9D0C2")


COPY = {
    "de": {
        "tagline": "SOFTWARE ENGINEERING | WEB | AUTOMATISIERUNG",
        "summary_title": "PROFIL",
        "summary": (
            "Software-Engineering-Student bei 42 Berlin mit Erfahrung in Webentwicklung, "
            "Automatisierung und digitalen Geschäftsprozessen. Ich verbinde technische "
            "Umsetzung mit einem praktischen Blick auf Abläufe, Nutzer und Teams."
        ),
        "experience": "BERUFSERFAHRUNG",
        "experience_items": [
            ("langjährige Mitarbeit | Digitalprojekte seit 2026 | Hamburg", "Digitale Projekte, operative Mitarbeit und Stadtteilarbeit", "Schnelsener Büchereck", [
                "Online-Vertrieb, TikTok Shop, Instagram Ads und Produktdaten-Workflows.",
                "DATEV-Automatisierung, Creator-Kooperationen und Tagesgeschäft.",
                "Mit HI! Schnelsen: Lesungen und Stadtteilveranstaltungen, Social Media, Begegnungsorte und Einsatz für eine fußgängerfreundlichere Frohmestraße."
            ]),
            ("10/2025 - heute | Rio de Janeiro / hybrid", "Produktentwickler", "Blink P&C", [
                "n8n-Chatbot für kleine Dienstleister: freie Kalenderzeiten prüfen und bestätigte Termine direkt eintragen."
            ]),
            ("03-07/2025 | Marseille", "Tourguide und Gästebetreuung", "Planet Azur", []),
            ("2023-2024 | Chile", "Rezeption und Organisation", "LÖF Hostal | PazZHOtel Eco/Art", []),
            ("10/2023 | Hamburg", "IT-Praktikum", "Peter Mattfeld & Sohn", []),
            ("06-07/2023 | Deutschland", "Fundraising", "Direct Result Marketing Deutschland", []),
        ],
        "projects": "PROJEKTE",
        "project_items": [
            ("DATEV Kassenbericht OCR", "Python, OCR, Playwright | Kontrollierte Übertragung von Kassenberichten in DATEV."),
            ("TikTok Shop x Libri", "Python, APIs, GitHub Actions | Produktimporte, Bestandsabgleich und Bestellvorbereitung."),
            ("Vergabe Radar", "Next.js, TypeScript, Supabase | Nachvollziehbares Matching öffentlicher IT-Ausschreibungen mit Anbieterprofilen."),
        ],
        "education": "AUSBILDUNG",
        "education_items": [
            ("seit 2026", "42 Berlin", "Software Engineering | projektbasiertes Peer-Learning"),
            ("2025", "42 Rio", "Software Engineering | C, Algorithmen und Unix"),
            ("2024-2025", "Aix-Marseille Université", "Mathematik und Informatik, angewandt auf Human- und Sozialwissenschaften (MIASHS) | AFEV KAPS: solidarische Wohngemeinschaft in Marseille"),
            ("2023", "Gymnasium Dörpsweg", "Abitur | 2,2"),
        ],
        "skills": "KOMPETENZEN",
        "skills_items": [
            ("Code", "C, Python, JavaScript, Git, Linux"),
            ("Web", "HTML, CSS, APIs, Plattformen"),
            ("Automation", "n8n, Playwright, OCR, GitHub Actions"),
            ("Praxis", "E-Commerce, Retail, Operations"),
        ],
        "languages": "SPRACHEN",
        "language_items": [
            ("Deutsch", "Muttersprache"),
            ("Spanisch", "zweite Muttersprache"),
            ("Englisch", "C2"),
            ("Französisch", "B2"),
            ("Portugiesisch", "ca. B1"),
        ],
        "footer": "Lebenslauf | August 2026",
    },
    "en": {
        "tagline": "SOFTWARE ENGINEERING | WEB | AUTOMATION",
        "summary_title": "PROFILE",
        "summary": (
            "Software engineering student at 42 Berlin with experience in web development, "
            "automation and digital business processes. I combine technical delivery with "
            "a practical understanding of workflows, users and teams."
        ),
        "experience": "EXPERIENCE",
        "experience_items": [
            ("long-standing role | digital projects since 2026 | Hamburg", "Digital projects, operations and community work", "Schnelsener Büchereck", [
                "Online sales, TikTok Shop, Instagram Ads and product-data workflows.",
                "DATEV automation, creator partnerships and daily operations.",
                "With HI! Schnelsen: readings and neighbourhood events, social media, meeting spaces and advocacy for a more pedestrian-friendly Frohmestraße."
            ]),
            ("10/2025 - present | Rio de Janeiro / hybrid", "Product Developer", "Blink P&C", [
                "n8n chatbot for small service businesses: check free calendar slots and add confirmed appointments directly."
            ]),
            ("03-07/2025 | Marseille", "Tour guide and guest support", "Planet Azur", []),
            ("2023-2024 | Chile", "Reception and operations", "LÖF Hostal | PazZHOtel Eco/Art", []),
            ("10/2023 | Hamburg", "IT Intern", "Peter Mattfeld & Sohn", []),
            ("06-07/2023 | Germany", "Fundraising", "Direct Result Marketing Deutschland", []),
        ],
        "projects": "PROJECTS",
        "project_items": [
            ("DATEV Cash Report OCR", "Python, OCR, Playwright | Controlled transfer of cash reports into DATEV."),
            ("TikTok Shop x Libri", "Python, APIs, GitHub Actions | Product imports, stock sync and order preparation."),
            ("Tender Radar", "Next.js, TypeScript, Supabase | Transparent matching of public IT tenders with provider profiles."),
        ],
        "education": "EDUCATION",
        "education_items": [
            ("since 2026", "42 Berlin", "Software Engineering | project-based peer learning"),
            ("2025", "42 Rio", "Software Engineering | C, algorithms and Unix"),
            ("2024-2025", "Aix-Marseille University", "Mathematics and Computer Science applied to Humanities and Social Sciences (MIASHS) | AFEV KAPS: solidarity-based shared flat in Marseille"),
            ("2023", "Gymnasium Dörpsweg", "German Abitur | 2.2"),
        ],
        "skills": "SKILLS",
        "skills_items": [
            ("Code", "C, Python, JavaScript, Git, Linux"),
            ("Web", "HTML, CSS, APIs, platforms"),
            ("Automation", "n8n, Playwright, OCR, GitHub Actions"),
            ("Business", "E-commerce, retail, operations"),
        ],
        "languages": "LANGUAGES",
        "language_items": [
            ("German", "native"),
            ("Spanish", "second native language"),
            ("English", "C2"),
            ("French", "B2"),
            ("Portuguese", "approx. B1"),
        ],
        "footer": "Curriculum Vitae | August 2026",
    },
    "fr": {
        "tagline": "GÉNIE LOGICIEL | WEB | AUTOMATISATION",
        "summary_title": "PROFIL",
        "summary": (
            "Étudiant en génie logiciel à 42 Berlin, avec une expérience en développement web, "
            "automatisation et processus numériques. J'associe réalisation technique et "
            "compréhension pratique des flux de travail, des utilisateurs et des équipes."
        ),
        "experience": "EXPÉRIENCE",
        "experience_items": [
            ("collaboration de longue date | projets numériques depuis 2026 | Hambourg", "Projets numériques, activité opérationnelle et engagement local", "Schnelsener Büchereck", [
                "Vente en ligne, TikTok Shop, campagnes Instagram et flux de données produits.",
                "Automatisation DATEV, partenariats avec des créateurs et activité quotidienne.",
                "Avec HI! Schnelsen : lectures et événements de quartier, réseaux sociaux, lieux de rencontre et engagement pour une Frohmestraße plus accueillante pour les piétons."
            ]),
            ("10/2025 - aujourd'hui | Rio de Janeiro / hybride", "Développeur produit", "Blink P&C", [
                "Chatbot n8n pour petits prestataires : vérifier les créneaux libres et inscrire directement les rendez-vous confirmés."
            ]),
            ("03-07/2025 | Marseille", "Guide touristique et accueil", "Planet Azur", []),
            ("2023-2024 | Chili", "Réception et organisation", "LÖF Hostal | PazZHOtel Eco/Art", []),
            ("10/2023 | Hambourg", "Stagiaire informatique", "Peter Mattfeld & Sohn", []),
            ("06-07/2023 | Allemagne", "Collecte de fonds", "Direct Result Marketing Deutschland", []),
        ],
        "projects": "PROJETS",
        "project_items": [
            ("OCR des rapports de caisse DATEV", "Python, OCR, Playwright | Transfert contrôlé des rapports de caisse dans DATEV."),
            ("TikTok Shop x Libri", "Python, APIs, GitHub Actions | Imports produits, stocks et préparation des commandes."),
            ("Radar des appels d'offres", "Next.js, TypeScript, Supabase | Mise en correspondance transparente entre appels d'offres informatiques et prestataires."),
        ],
        "education": "FORMATION",
        "education_items": [
            ("depuis 2026", "42 Berlin", "Génie logiciel | apprentissage par projets entre pairs"),
            ("2025", "42 Rio", "Génie logiciel | C, algorithmes et Unix"),
            ("2024-2025", "Aix-Marseille Université", "Mathématiques et informatique appliquées aux sciences humaines et sociales (MIASHS) | AFEV KAPS : colocation à projet solidaire à Marseille"),
            ("2023", "Gymnasium Dörpsweg", "Abitur allemand | 2,2"),
        ],
        "skills": "COMPÉTENCES",
        "skills_items": [
            ("Code", "C, Python, JavaScript, Git, Linux"),
            ("Web", "HTML, CSS, APIs, plateformes"),
            ("Automatisation", "n8n, Playwright, OCR, GitHub Actions"),
            ("Activité", "E-commerce, commerce, opérations"),
        ],
        "languages": "LANGUES",
        "language_items": [
            ("Allemand", "langue maternelle"),
            ("Espagnol", "deuxième langue maternelle"),
            ("Anglais", "C2"),
            ("Français", "B2"),
            ("Portugais", "env. B1"),
        ],
        "footer": "Curriculum Vitae | Août 2026",
    },
    "es": {
        "tagline": "INGENIERÍA DE SOFTWARE | WEB | AUTOMATIZACIÓN",
        "summary_title": "PERFIL",
        "summary": (
            "Estudiante de ingeniería de software en 42 Berlin con experiencia en desarrollo web, "
            "automatización y procesos digitales. Combino la implementación técnica con una "
            "visión práctica de los flujos de trabajo, los usuarios y los equipos."
        ),
        "experience": "EXPERIENCIA",
        "experience_items": [
            ("colaboración de larga trayectoria | proyectos digitales desde 2026 | Hamburgo", "Proyectos digitales, trabajo operativo y compromiso local", "Schnelsener Büchereck", [
                "Venta online, TikTok Shop, campañas de Instagram y flujos de datos de producto.",
                "Automatización con DATEV, colaboraciones con creadores y operación diaria.",
                "Con HI! Schnelsen: lecturas y eventos de barrio, redes sociales, espacios de encuentro y trabajo por una Frohmestraße más orientada a los peatones."
            ]),
            ("10/2025 - actualidad | Río de Janeiro / híbrido", "Desarrollador de producto", "Blink P&C", [
                "Chatbot n8n para pequeños negocios de servicios: comprobar huecos libres y registrar las citas confirmadas."
            ]),
            ("03-07/2025 | Marsella", "Guía turístico y atención a visitantes", "Planet Azur", []),
            ("2023-2024 | Chile", "Recepción y organización", "LÖF Hostal | PazZHOtel Eco/Art", []),
            ("10/2023 | Hamburgo", "Prácticas de TI", "Peter Mattfeld & Sohn", []),
            ("06-07/2023 | Alemania", "Captación de fondos", "Direct Result Marketing Deutschland", []),
        ],
        "projects": "PROYECTOS",
        "project_items": [
            ("OCR de informes de caja DATEV", "Python, OCR, Playwright | Transferencia controlada de informes de caja a DATEV."),
            ("TikTok Shop x Libri", "Python, APIs, GitHub Actions | Importaciones, existencias y preparación de pedidos."),
            ("Radar de licitaciones", "Next.js, TypeScript, Supabase | Vinculación transparente de licitaciones públicas de TI con proveedores."),
        ],
        "education": "FORMACIÓN",
        "education_items": [
            ("desde 2026", "42 Berlin", "Ingeniería de software | aprendizaje por proyectos entre pares"),
            ("2025", "42 Rio", "Ingeniería de software | C, algoritmos y Unix"),
            ("2024-2025", "Aix-Marseille Université", "Matemáticas e informática aplicadas a las ciencias humanas y sociales (MIASHS) | AFEV KAPS: vivienda compartida solidaria en Marsella"),
            ("2023", "Gymnasium Dörpsweg", "Abitur alemán | 2,2"),
        ],
        "skills": "COMPETENCIAS",
        "skills_items": [
            ("Código", "C, Python, JavaScript, Git, Linux"),
            ("Web", "HTML, CSS, APIs, plataformas"),
            ("Automatización", "n8n, Playwright, OCR, GitHub Actions"),
            ("Negocio", "E-commerce, retail, operaciones"),
        ],
        "languages": "IDIOMAS",
        "language_items": [
            ("Alemán", "lengua materna"),
            ("Español", "segunda lengua materna"),
            ("Inglés", "C2"),
            ("Francés", "B2"),
            ("Portugués", "aprox. B1"),
        ],
        "footer": "Curriculum Vitae | Agosto 2026",
    },
}


def styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name", parent=base["Normal"], fontName="Times-Roman", fontSize=28,
            leading=29, textColor=INK, spaceAfter=4 * mm
        ),
        "tagline": ParagraphStyle(
            "Tagline", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=7.7,
            leading=9, textColor=ACCENT, tracking=.7, spaceAfter=3 * mm
        ),
        "contact": ParagraphStyle(
            "Contact", parent=base["Normal"], fontName="Helvetica", fontSize=7.6,
            leading=10, textColor=MUTED
        ),
        "section": ParagraphStyle(
            "Section", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=8.2,
            leading=10, textColor=ACCENT, tracking=.8, spaceBefore=1.5 * mm,
            spaceAfter=1.5 * mm
        ),
        "summary": ParagraphStyle(
            "Summary", parent=base["Normal"], fontName="Helvetica", fontSize=8.4,
            leading=11.1, textColor=INK
        ),
        "date": ParagraphStyle(
            "Date", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=6.8,
            leading=8.2, textColor=ACCENT, spaceAfter=.6 * mm
        ),
        "role": ParagraphStyle(
            "Role", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=8.6,
            leading=10.2, textColor=INK, spaceAfter=.25 * mm
        ),
        "company": ParagraphStyle(
            "Company", parent=base["Normal"], fontName="Helvetica-Oblique", fontSize=7.4,
            leading=9, textColor=MUTED, spaceAfter=.6 * mm
        ),
        "bullet": ParagraphStyle(
            "Bullet", parent=base["Normal"], fontName="Helvetica", fontSize=7.3,
            leading=9.1, leftIndent=3 * mm, firstLineIndent=-2.4 * mm,
            textColor=INK, bulletIndent=0
        ),
        "small": ParagraphStyle(
            "Small", parent=base["Normal"], fontName="Helvetica", fontSize=7.25,
            leading=9.2, textColor=INK
        ),
        "small_muted": ParagraphStyle(
            "SmallMuted", parent=base["Normal"], fontName="Helvetica", fontSize=7.1,
            leading=9.1, textColor=MUTED
        ),
        "footer": ParagraphStyle(
            "Footer", parent=base["Normal"], fontName="Helvetica", fontSize=6.6,
            leading=8, textColor=MUTED, alignment=TA_LEFT
        ),
    }


def section_heading(text, s):
    return [
        Paragraph(escape(text), s["section"]),
        HRFlowable(width="100%", thickness=.55, color=LINE, spaceBefore=0, spaceAfter=2.2 * mm),
    ]


def experience_item(date, role, company, bullets, s):
    flow = [
        Paragraph(escape(date), s["date"]),
        Paragraph(escape(role), s["role"]),
        Paragraph(escape(company), s["company"]),
    ]
    for bullet in bullets:
        flow.append(Paragraph(f"- {escape(bullet)}", s["bullet"]))
    flow.append(Spacer(1, 2.1 * mm))
    return flow


def education_item(date, institution, detail, s):
    return [
        Paragraph(escape(date), s["date"]),
        Paragraph(escape(institution), s["role"]),
        Paragraph(escape(detail), s["small_muted"]),
        Spacer(1, 2.3 * mm),
    ]


def build_pdf(lang, copy):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    path = OUTPUT / f"paul-freyhofer-cv-{lang}.pdf"
    s = styles()
    doc = SimpleDocTemplate(
        str(path), pagesize=A4, rightMargin=13 * mm, leftMargin=13 * mm,
        topMargin=11 * mm, bottomMargin=10 * mm,
        title=f"Paul Freyhofer - CV ({lang.upper()})",
        author="Paul Freyhofer",
        subject="Curriculum Vitae",
    )

    portrait = Image(str(PORTRAIT), width=34 * mm, height=42.5 * mm)
    portrait.hAlign = "RIGHT"
    links = (
        '<link href="mailto:paul@freyhofer.de" color="#636860">paul@freyhofer.de</link>'
        '  |  Berlin / Hamburg<br/>'
        '<link href="https://github.com/FREYHOFER" color="#636860">github.com/FREYHOFER</link>'
        '  |  <link href="https://www.linkedin.com/in/paul-freyhofer-a4055519a" color="#636860">linkedin.com/in/paul-freyhofer</link><br/>'
        '<link href="https://paulfreyhofer.vercel.app" color="#636860">paulfreyhofer.vercel.app</link>'
    )
    header_text = [
        Paragraph("Paul Freyhofer", s["name"]),
        Paragraph(escape(copy["tagline"]), s["tagline"]),
        Paragraph(links, s["contact"]),
    ]
    header = Table([[header_text, portrait]], colWidths=[doc.width - 40 * mm, 40 * mm], hAlign="LEFT")
    header.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))

    left = []
    left.extend(section_heading(copy["experience"], s))
    for item in copy["experience_items"]:
        left.extend(experience_item(*item, s))
    left.extend(section_heading(copy["projects"], s))
    for title, detail in copy["project_items"]:
        left.extend([
            Paragraph(escape(title), s["role"]),
            Paragraph(escape(detail), s["small_muted"]),
            Spacer(1, 2.1 * mm),
        ])

    right = []
    right.extend(section_heading(copy["education"], s))
    for item in copy["education_items"]:
        right.extend(education_item(*item, s))
    right.extend(section_heading(copy["skills"], s))
    for label, detail in copy["skills_items"]:
        right.extend([
            Paragraph(f"<b>{escape(label)}</b>", s["small"]),
            Paragraph(escape(detail), s["small_muted"]),
            Spacer(1, 1.8 * mm),
        ])
    right.extend(section_heading(copy["languages"], s))
    for label, detail in copy["language_items"]:
        right.append(Paragraph(f"<b>{escape(label)}</b>  |  {escape(detail)}", s["small"]))
        right.append(Spacer(1, .9 * mm))

    body = Table([[left, right]], colWidths=[doc.width * .63, doc.width * .37], hAlign="LEFT")
    body.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("RIGHTPADDING", (0, 0), (0, 0), 7 * mm),
        ("LEFTPADDING", (1, 0), (1, 0), 7 * mm),
        ("RIGHTPADDING", (1, 0), (1, 0), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("LINEBEFORE", (1, 0), (1, 0), .55, LINE),
    ]))

    story = [
        header,
        Spacer(1, 4 * mm),
        *section_heading(copy["summary_title"], s),
        Paragraph(escape(copy["summary"]), s["summary"]),
        Spacer(1, 3.4 * mm),
        body,
        Spacer(1, 2 * mm),
        HRFlowable(width="100%", thickness=.55, color=LINE, spaceBefore=0, spaceAfter=1.5 * mm),
        Paragraph(escape(copy["footer"]), s["footer"]),
    ]

    def paint_page(canvas, _doc):
        canvas.saveState()
        canvas.setFillColor(PAPER)
        canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
        canvas.restoreState()

    doc.build(story, onFirstPage=paint_page, onLaterPages=paint_page)
    shutil.copy2(path, ROOT / path.name)
    return path


if __name__ == "__main__":
    for language, language_copy in COPY.items():
        print(build_pdf(language, language_copy))
