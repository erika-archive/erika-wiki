# Preservation details

This unofficial archive preserves selected public ErikaWiki documentation and its current original uploaded resources. Acquisition began on 2026-11-06; conversion and publication were completed on 2026-11-07 (Asia/Shanghai).

## Coverage

| Material | Preserved |
|---|---:|
| Articles | 204 |
| Uploaded-file description pages | 690 |
| Categories | 6 |
| Help and project reference pages | 4 |
| Discussion pages | 4 |
| Total page records | 908 |
| Original editing-history revisions | 4420 |
| Current original uploaded resources | 690 |
| Additional linked images, PDFs and example archives | 33 |

The 27 unrelated gift-card/generator spam pages were excluded at the archive owner's request. Their titles and original page IDs are preserved in [the exclusion inventory](metadata/excluded-spam-pages.json); their spam content is not imported. Personal account/profile namespaces and MediaWiki interface-message namespaces are outside the documentation scope. The [complete selected-page inventory](metadata/page-inventory.json) identifies every included page.

## Reading and source material

- `docs/`, `reference/`, `discussions/` and `categories/` contain converted Markdown.
- `files/` contains original resource descriptions, image previews and upload credits.
- `assets/uploads/` contains all 690 current original uploads, including unused images.
- `assets/linked/` contains available additional resources referenced by the documentation.
- `source/history/` preserves complete editing-history exports for the selected pages.
- `source/wikitext/` preserves each page's current original MediaWiki source.
- `source/html/` preserves unmodified rendered article HTML or a transparent rendering of plain file descriptions and redirects.
- `metadata/` contains inventories, authors, revision IDs, source links, resource checksums and validation results.

Each converted page links to its original source and history export. Historical article revisions are retained in the XML exports; the reading copy is the latest exported revision. Current original uploaded files are included; previous binary upload versions and external websites are outside this snapshot.

Two legacy project-page titles contain doubled namespace separators and were silently skipped by MediaWiki's normal export. Their histories were recovered by numeric page ID through the read-only revision API and included in the corresponding XML batch. These cases are identified by `api_history_fallback_titles` in [the export index](metadata/history-export-index.json).

## Conversion

Rendered content was converted to Markdown, including headings, lists, links, tables and code blocks. Complex tables retain HTML where required to preserve row/column spans. Original MediaWiki heading anchors are retained alongside Markdown headings. Internal links point to local Markdown files, and image references use local resources. The complete original source remains available for checking conversion decisions.

Links through original redirect pages are resolved to the archived destination. One obsolete ScicosLab installation-section anchor is retained as a compatibility alias for links that used its old heading. Original source exports are unchanged by these navigation fixes.

The archive appends provenance sections identifying the original title, revision ID, source timestamp, contributors and source files. Original copyright, license, acknowledgement, dedication and disclaimer material is preserved with the original source and converted content. See [NOTICE.md](NOTICE.md) and [GNU FDL 1.2](LICENSE-GFDL-1.2.txt).

## Resource integrity and known source failures

All 690 original uploads were checked against the Wiki's recorded size and SHA-1. Downloaded resources also have SHA-256 checksums. Preserved source/resources are protected from automatic Git newline conversion by `.gitattributes`.

One non-image historical installer link already returns HTTP 404 at the original server:

`http://download.tuxfamily.org/erika/webdownload/eeb_gpl/EE_160_Win.zip`

It is referenced from the Freescale S12 article. Its original URL is retained and the failure is documented in [the linked-resource manifest](metadata/linked-resource-manifest.json). No substitute file was invented. All current original Wiki uploads and all embedded document images are present.

Validation checks selected-page coverage, source/history checksums, all original-upload checksums, local page/image links, heading anchors, and original preformatted code blocks. Machine-readable results are stored in `metadata/verification.json`.

Final validation passed: 908 page records; 690 original uploads; 33 additional resources; 7633 local page/image/section-link checks; 1402 image references; 718 original code blocks. There are no broken local links, missing section anchors, remote embedded images, or conversion-validation errors.
