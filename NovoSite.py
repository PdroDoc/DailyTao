import os

CAPITULOS_DIR = "capitulos"
OUTPUT_FILE = "index.html"

html_template = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Tao Te Ching - O Caminho do Sábio</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;700&family=Ma+Shan+Zheng&display=swap');

    body {{
      margin: 0;
      background-color: #f8f4e9;
      background-image: url('https://www.transparenttextures.com/patterns/rice-paper.png');
      color: #3a3226;
      font-family: 'Noto Serif SC', serif;
      display: flex;
      min-height: 100vh;
    }}

    .chapter-nav {{
      width: 140px;
      background-color: #3a3226;
      padding: 10px;
      border-right: 1px solid #8b5a2b;
      box-shadow: 2px 0 5px rgba(0,0,0,0.1);
      overflow-y: auto;
      text-align: center;
    }}

    .chapter-nav img {{
      width: 100px;
      border-radius: 6px;
      margin-bottom: 10px;
      box-shadow: 0 0 5px rgba(0,0,0,0.3);
    }}

    .chapter-nav h3 {{
      color: #f8f4e9;
      border-bottom: 1px solid #8b5a2b;
      padding-bottom: 10px;
      margin-bottom: 15px;
      font-size: 1.1em;
    }}

    .chapter-item {{
      margin-bottom: 8px;
    }}

    .chapter-link {{
      color: #d4c8b5;
      text-decoration: none;
      display: block;
      padding: 5px;
      border-radius: 3px;
      transition: all 0.3s ease;
    }}

    .chapter-link:hover {{
      background-color: #8b5a2b;
      color: #f8f4e9;
    }}

    .content-container {{
      flex: 1;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 20px;
    }}

    .scroll-container {{
      max-width: 700px;
      width: 100%;
      height: 80vh;
      overflow-y: auto;
      padding: 30px;
      background-color: #fff9ee;
      border: 1px solid #d9c7a7;
      box-shadow: 0 0 15px rgba(0,0,0,0.1);
      position: relative;
    }}

    .scroll-container::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 30px;
      background: linear-gradient(to bottom, rgba(0,0,0,0.1), transparent);
    }}

    .scroll-container::after {{
      content: "";
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 30px;
      background: linear-gradient(to top, rgba(0,0,0,0.1), transparent);
    }}

    .chapter-title {{
      text-align: center;
      color: #8b5a2b;
      font-size: 2.2em;
      margin-bottom: 30px;
      font-weight: 700;
      font-family: 'Ma Shan Zheng', cursive;
    }}

    .chapter-title::before, .chapter-title::after {{
      content: "❖";
      color: #d9c7a7;
      margin: 0 15px;
      font-size: 0.8em;
    }}

    .chapter-text {{
      font-size: 1.1em;
      line-height: 1.8;
      text-align: justify;
      white-space: pre-wrap;
    }}
  </style>
</head>
<body>
  <nav class="chapter-nav">
    <img src="meandmiau.jpeg" alt="Miau e eu">
    <h3>Capítulos</h3>
    <ul class="chapter-list">
      {links}
    </ul>
  </nav>

  <div class="content-container">
    <div class="scroll-container">
      <h1 class="chapter-title">Tao Te Ching</h1>
      <div id="chapter-content" class="chapter-text">Selecione um capítulo ao lado.</div>
    </div>
  </div>

  <script>
    const capitulos = {{
      {js_dict}
    }};

    function showContent(nome) {{
      document.getElementById("chapter-content").innerText = capitulos[nome];
    }}
  </script>
</body>
</html>
"""

def gerar_site():
    links = []
    js_dict_entries = []

    for filename in sorted(os.listdir(CAPITULOS_DIR)):
        if filename.endswith(".md"):
            nome = os.path.splitext(filename)[0]
            titulo = nome.replace("_", " ").capitalize()
            with open(os.path.join(CAPITULOS_DIR, filename), "r", encoding="utf-8") as f:
                conteudo = f.read().replace('\\', '\\\\').replace('\n', '\\n').replace('"', '\\"')
            links.append(f'<li class="chapter-item"><a href="#" class="chapter-link" onclick="showContent(\'{nome}\')">{titulo}</a></li>')
            js_dict_entries.append(f'"{nome}": "{conteudo}"')

    html_final = html_template.format(
        links="\n      ".join(links),
        js_dict=",\n      ".join(js_dict_entries)
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html_final)

    print("✅ Novo site gerado com sucesso: index.html")

if __name__ == "__main__":
    gerar_site()