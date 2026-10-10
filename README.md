# Xillim Scientific static website

## Included
- HTML pages (home, services overview, 9 service pages, about/FAQ, demonstrations, request, privacy)
- Shared responsive CSS with scroll/hero animations and grouped Services navigation
- Shared JavaScript (mobile menu, dropdown, reveal-on-scroll, mailto inquiry form)
- Brand logo, banner and icon PNG assets

## Publish
Upload the complete contents of this directory to a static hosting service such as Netlify, Cloudflare Pages, GitHub Pages, or any standard web host. `index.html` must be at the site root. You do not need to upload `_build_pages.py` (optional regenerator).

## IMPORTANT before launch
The project-request form uses a `mailto:` email handoff. The destination is set in `request.html` on `form id="inquiry"` via `data-email` (not displayed in page copy). Replace it with a business email when available, or switch to Netlify Forms / Formspree for server-side delivery. A mailto form cannot guarantee delivery and requires a visitor email client.

The banner/logo images are included locally. The Google Fonts import requires internet connectivity; system-font fallbacks are provided. Expand the privacy placeholder before collecting personal data at scale. Research/clinical and asset-risk scope limitations are shown on relevant pages.

## Wix
Wix cannot natively import these files as editable Wix website pages. Use standalone hosting for the HTML site, or rebuild the pages with Wix Editor using the supplied content/assets.
