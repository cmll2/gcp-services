import os
import re

NOTES_DIR = '.'  # Racine du repo
OUTPUT_FILE = 'INDEX.md'
KEYWORD_REGEX = r'\*\*Keywords\*\*: `(.*?)`'

index_entries = []

# Explorer tous les fichiers .md sauf README et INDEX
for root, _, files in os.walk(NOTES_DIR):
    for file in files:
        if file.endswith('.md') and file not in ['README.md', OUTPUT_FILE]:
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                match = re.search(KEYWORD_REGEX, content)
                keywords = match.group(1) if match else '—'
                service_name = os.path.splitext(file)[0].replace('-', ' ').title()
                rel_path = os.path.relpath(filepath, NOTES_DIR)
                index_entries.append((service_name, keywords, rel_path))

# Générer le tableau Markdown
index_md = "# 📚 Index des Services\n\n"
index_md += "| Service       | Mots-clés                          | Fichier |\n"
index_md += "|---------------|-----------------------------------|---------|\n"

for name, keywords, path in sorted(index_entries):
    index_md += f"| {name:<13} | {keywords:<35} | [{path}]({path}) |\n"

# Écrire le fichier INDEX.md
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(index_md)

print(f"✅ Fichier d'index généré : {OUTPUT_FILE}")
