import requests
from tools.pdf_exporter import export_pdf


class ToolAgent:
    def web_search(self, query):
        url = "https://duckduckgo.com/html/"
        params = {"q": query}
        headers = {"User-Agent": "Mozilla/5.0"}
        
        response = requests.get(url, params=params, headers=headers, timeout=10)
        return response.text[:2000]   # trimmed for context safety
    
    def pdf_export(self, text, filename="research_report.pdf"):
        export_pdf(text, filename)
        return f"PDF successfully generated as {filename}"

