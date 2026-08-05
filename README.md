# Paul Freyhofer - Portfolio & CV

Personal portfolio and résumé website for Paul Freyhofer.

## Features

- German, English, French and Spanish
- Responsive one-page portfolio
- Warm editorial color system with dark and light mode
- Personal photography and responsive layouts
- Motion effects with reduced-motion fallback
- Selected GitHub projects
- Classic, downloadable CV PDFs with portrait in four languages
- Static deployment on Vercel

## Rebuild the CV PDFs

```bash
python scripts/generate_cvs.py
```

The generator writes review copies to `output/pdf/` and refreshes the four
stable download files in the project root.

## Deployment

The `main` branch is connected to Vercel and is the production source.

## Local preview

```bash
python3 -m http.server 4173
```

Open `http://localhost:4173`.
