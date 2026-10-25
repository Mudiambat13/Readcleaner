import argparse
from scraper import extract_article
from rich import print


def main():
  parser = argparse.ArgumentParser(
      description="Convertit un article web en un fichier Markdown épuré."
  )
  parser.add_argument("url", help="L'URL de la page web à nettoyer")
  parser.add_argument(
      "-o", "--output", default="article.md", help="Nom du fichier de sortie (.md)"
  )
  args = parser.parse_args()

  print(f"[bold blue]Analyse et extraction de :[/bold blue] {args.url}")

  try:
    data = extract_article(args.url)

    # Création du Front-matter YAML (très apprécié par Obsidian / Notion)
    front_matter = f"""---
title: "{data['title']}"
author: "{data['author']}"
date: "{data['date']}"
source: "{args.url}"
---

"""
    full_markdown = front_matter + data["content"]

    # Sauvegarde dans le fichier
    with open(args.output, "w", encoding="utf-8") as f:
      f.write(full_markdown)

    print(
        f"[bold green]Succès ![/bold green] Article converti et sauvegardé dans"
        f" [cyan]{args.output}[/cyan]"
    )

  except Exception as e:
    print(f"[bold red]Erreur :[/bold red] {e}")


if __name__ == "__main__":
  main()