import os
from pathlib import Path

try:
    import minify_html
    MINIFY = True
except ImportError:
    MINIFY = False
    print("Подсказка: установите 'pip install minify-html' для минификации HTML")

def minify_html_files():
    """Находит и минифицирует все HTML файлы в папке 'site/'"""
    site_dir = Path("site")
    if not site_dir.exists():
        print("Папка 'site/' не найдена. Сначала выполните 'mkdocs build'.")
        return

    for html_file in site_dir.rglob("*.html"):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            if MINIFY:
                content = minify_html.minify(content, minify_js=True, minify_css=True)
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  Обработан: {html_file.relative_to(site_dir)}")
        except Exception as e:
            print(f"  Ошибка с {html_file}: {e}")

if __name__ == "__main__":
    print("Запуск минификации HTML...")
    minify_html_files()
    print("Готово.")