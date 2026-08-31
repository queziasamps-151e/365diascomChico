#!/usr/bin/env python3
"""
Gera o arquivo fotos/lista.json com os nomes de todas as fotos
que estiverem dentro da pasta 'fotos/'.

Como usar:
1. Baixe o album inteiro do Google Fotos como .zip
   (no album, use o menu de tres pontos > Baixar tudo)
2. Extraia o .zip e copie TODAS as fotos para dentro da pasta 'fotos/'
   que fica ao lado deste script (e ao lado do index.html)
3. Rode este script:  python3 gerar-lista.py
4. Ele vai criar fotos/lista.json automaticamente
5. Suba tudo (index.html, pasta fotos/ com as imagens e o lista.json) pro GitHub

Nao precisa renomear nenhum arquivo. Funciona com os nomes
originais do Google Fotos (ex: PXL_20250830_183012.jpg, IMG_1234.HEIC, etc).
"""

import json
import os

EXTENSOES_VALIDAS = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}

def main():
    pasta_fotos = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fotos')

    if not os.path.isdir(pasta_fotos):
        print(f"ERRO: pasta 'fotos' nao encontrada em {pasta_fotos}")
        print("Crie a pasta 'fotos' ao lado deste script e coloque as imagens dentro.")
        return

    arquivos = []
    ignorados = []
    for nome in sorted(os.listdir(pasta_fotos)):
        caminho = os.path.join(pasta_fotos, nome)
        if not os.path.isfile(caminho):
            continue
        _, ext = os.path.splitext(nome)
        if ext.lower() in EXTENSOES_VALIDAS:
            arquivos.append(nome)
        elif nome != 'lista.json' and not nome.startswith('.'):
            ignorados.append(nome)

    if not arquivos:
        print("Nenhuma foto encontrada dentro da pasta 'fotos'.")
        print("Extensoes aceitas:", ', '.join(sorted(EXTENSOES_VALIDAS)))
        return

    saida = os.path.join(pasta_fotos, 'lista.json')
    with open(saida, 'w', encoding='utf-8') as f:
        json.dump(arquivos, f, ensure_ascii=False, indent=2)

    print(f"Pronto! {len(arquivos)} fotos encontradas e listadas em fotos/lista.json")
    if ignorados:
        print(f"\nAviso: {len(ignorados)} arquivo(s) ignorado(s) por extensao nao suportada:")
        for nome in ignorados[:10]:
            print(f"  - {nome}")
        if len(ignorados) > 10:
            print(f"  ... e mais {len(ignorados) - 10}")
        print("\nSe algum desses for foto (ex: .HEIC do iPhone), converta para .jpg antes.")

if __name__ == '__main__':
    main()
