import trafilatura
from markdownify import markdownify as md


def extract_article(url: str) -> dict:
  """Télécharge une page web, extrait son contenu principal et ses métadonnées,

  puis convertit le tout en Markdown.
  """
  # 1. Télécharger la page web de manière robuste
  downloaded = trafilatura.fetch_url(url)
  if not downloaded:
    raise ValueError(
        "Impossible de télécharger la page ou URL invalide / protégée."
    )

  # 2. Extraire les métadonnées (titre, auteur, date, description)
  metadata = trafilatura.extract_metadata(downloaded)

  # 3. Extraire le contenu propre au format HTML pour garder les balises structurées
  clean_html = trafilatura.extract(
      downloaded, include_formatting=True, include_links=True, output_format="html"
  )

  if not clean_html:
    raise ValueError(
        "Impossible d'extraire le contenu textuel principal de cette page."
    )

  # 4. Convertir le HTML propre en Markdown
  markdown_content = md(clean_html, heading_style="ATX")

  return {
      "title": metadata.title if metadata and metadata.title else "Sans titre",
      "author": metadata.author if metadata and metadata.author else "Inconnu",
      "date": metadata.date if metadata and metadata.date else "Date inconnue",
      "content": markdown_content,
  }