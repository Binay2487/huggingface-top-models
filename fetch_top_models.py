import requests
import json

def fetch_top_models():
    url = "https://huggingface.co/api/models"
    response = requests.get(url)
    models = response.json()
    
    # Sort models by downloads
    top_models = sorted(models, key=lambda x: x.get('downloads', 0), reverse=True)[:10]
    
    report = []
    for model in top_models:
        report.append({
            'name': model['modelId'],
            'downloads': model.get('downloads', 0)
        })
    
    return report

def save_report(report, filename="top_models_report.json"):
    with open(filename, 'w') as f:
        json.dump(report, f, indent=2)

if __name__ == "__main__":
    report = fetch_top_models()
    save_report(report)
    print("Report generated and saved to top_models_report.json")
