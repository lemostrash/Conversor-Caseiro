import os
from PIL import Image

def convert_jpg_to_png(input_path, output_path):
    try:
        # Abrir o arquivo JPG
        with Image.open(input_path) as img:
            # Redimensionar a imagem para a dimensão (6026x4004)
            img = img.resize((6026, 4004), Image.ANTIALIAS)
            # Converter a imagem para modo RGB de 8 bits
            img = img.convert("RGB")
            
            # Obter o nome do arquivo sem a extensão
            filename_without_extension = os.path.splitext(os.path.basename(input_path))[0]
            # Gerar o caminho de saída com a extensão .png
            output_png_path = os.path.join(output_path, f'{filename_without_extension}.png')
            # Salvar como PNG com resolução de 300 dpi
            img.save(output_png_path, 'PNG', dpi=(300, 300))
            print(f"Conversão de {input_path} para {output_png_path} concluída.")
    except Exception as e:
        print(f"Ocorreu um erro durante a conversão de {input_path}: {e}")

# Caminhos pelos caminhos reais das suas pastas
input_folder = r'C:\Users\testando\Downloads\teste'
output_folder = r'C:\Users\testando\Downloads\testee'

# Percorrer todos os arquivos JPG na pasta de entrada
for filename in os.listdir(input_folder):
    if filename.lower().endswith('.jpg'):
        input_jpg_path = os.path.join(input_folder, filename)
        convert_jpg_to_png(input_jpg_path, output_folder)
