# Deploying digitalinformationgovernance.com

This repo carries the full static-site generator (`build/`) and the generated
output (`site/`) for digitalinformationgovernance.com, alongside the DIG®
framework spec in `docs/`. The site is plain static HTML — no framework, no
build service required.

## Rebuild

```
cd build
python generate.py        # regenerates ../site/ from content*.py + templates.py
```

- `templates.py` holds the `TODAY` constant used for "Updated" bylines — bump it
  before a rebuild so dates are honest.
- The generator runs a de-slop scan and JSON-LD validation as part of the build;
  a failed gate prints and aborts.

## Deploy (Vercel)

The production project is `digitalinformationgovernance` on Vercel. Deploy the
`site/` directory as the root:

```
cd site
vercel --prod --yes
```

Then verify a changed URL live (load it, check the content), and re-submit the
sitemap to IndexNow:

```
python build/indexnow_submit.py
```

(The IndexNow key file is part of `site/` and is public by design.)

Alternatively, connect this GitHub repo to the Vercel project with the root
directory set to `site/` and framework preset "Other" — then a push to `main`
deploys.

## Content map

- `build/content.py` … `content5.py` — core pages (v1.0 corpus)
- `build/content6.py` — `/ai-agent-governance` (v1.1 agentic extension)
- `build/content7.py` — glossary override, `/ai-regulation-tracker`,
  `/ai-agent-incident-register`, `/compare/frontier-model-access-tiers`
- `build/templates.py` — layout, JSON-LD, cite-this-page box, verification slots
- `site/data/*.json` — machine-readable exports (regulation tracker, five
  questions, maturity model)
