import json
from deep_translator import GoogleTranslator

# Caminho do arquivo de entrada
input_file = 'lang.json'
output_file = 'lang_pt2.json'

# Carregar arquivo
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Traduzir valores
translated = {}
translator = GoogleTranslator(source='auto', target='pt')

for key, value in data.items():
    if isinstance(value, str) and value.strip():
        try:
             
            translated[key] = translator.translate(value)
            print(translated[key])
        except Exception as e:
            print(f"Erro ao traduzir '{value}': {e}")
            translated[key] = value
    else:
        translated[key] = value

# Salvar resultado
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(translated, f, ensure_ascii=False, indent=2)

print("Tradução concluída! Arquivo salvo como:", output_file)
