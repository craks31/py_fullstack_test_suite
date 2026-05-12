import yaml
import json

def generate_karate_tests(yaml_file_path: str) -> str:
    # Read
    with open(yaml_file_path, 'r') as f:
        yaml_content = f.read()

    # Parse deterministically
    spec = yaml.safe_load(yaml_content)
    base_url = spec.get('servers', [{}])[0].get('url', 'http://localhost:8080')
    title = spec.get('info', {}).get('title', 'API Tests')

    endpoints = []
    for path, methods in spec.get('paths', {}).items():
        for method, details in methods.items():
            endpoints.append({
                "path": path,
                "method": method.upper(),
                "summary": details.get('summary', ''),
                "parameters": details.get('parameters', []),
                "request_body": details.get('requestBody', {}),
                "responses": details.get('responses', {})
            })

    result = {
    "instruction": "Generate a Karate BDD feature file strictly following all rules below",
    "rules": {
        "feature_name": title,
        "background_url": base_url,
        "request_body_format": "Always wrap in triple quotes",
        "scenarios": "One per status code per endpoint",
        "scenario_name": "Use summary if exists else METHOD path",
        "parameters": "Only explicitly defined ones",
        "status_codes": "Only explicitly defined ones, else 200 only",
        "response_assertions": "Status code only, never body fields",
        "indentation": "2 spaces throughout",
        "output": "Raw feature file only, no markdown"
    },
    "endpoints": endpoints
    }
    return json.dumps(result, indent=2)