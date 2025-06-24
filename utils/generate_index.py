import os
import re

NOTES_DIR = '.'  # Racine du repo
OUTPUT_FILE = 'INDEX.md'
KEYWORD_LINE_REGEX = r'\*\*Keywords\*\*:(.*)'
KEYWORD_REGEX = r'`([^`]+)`'

index_entries = []

for root, _, files in os.walk(NOTES_DIR):
    for file in files:
        if file.endswith('.md') and file not in ['README.md', OUTPUT_FILE]:
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                # Chercher la ligne des keywords
                keyword_line_match = re.search(KEYWORD_LINE_REGEX, content)
                if keyword_line_match:
                    keyword_line = keyword_line_match.group(1)
                    keywords = re.findall(KEYWORD_REGEX, keyword_line)
                    keywords_str = ', '.join([k.strip() for k in keywords]) if keywords else '—'
                else:
                    keywords_str = '—'
                service_name = os.path.splitext(file)[0].replace('-', ' ').title()
                rel_path = os.path.relpath(filepath, NOTES_DIR)
                index_entries.append((service_name, keywords_str, rel_path))

# Générer le tableau Markdown
index_md = "# 📚 Index des Services\n\n"
index_md += "| Service       | Mots-clés                          | Fichier |\n"
index_md += "|---------------|-----------------------------------|---------|\n"

for name, keywords, path in sorted(index_entries):
    index_md += f"| {name:<13} | {keywords:<35} | [{path}]({path}) |\n"

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(index_md)

print(f"✅ Fichier d'index généré : {OUTPUT_FILE}")