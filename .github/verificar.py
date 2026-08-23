#!/usr/bin/env python3
"""Confere as missoes do LAB 01 e imprime um checklist.

Nao substitui a correcao do professor: le o estado do repositorio e diz o
que ja esta no lugar. Serve para o aluno conferir antes de entregar.
"""
import os
import re
import subprocess
import sys

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


def ler(caminho):
    try:
        with open(caminho, encoding='utf-8') as f:
            return f.read()
    except OSError:
        return ''


def rastreado(caminho):
    saida = subprocess.run(['git', 'ls-files', caminho],
                           capture_output=True, text=True).stdout
    return bool(saida.strip())


readme = ler('README.md')
html = ler('index.html')
css = ler('css/style.css')
gitignore = ler('.gitignore')
respostas = ler('RESPOSTAS.md')
LINHAS = respostas.splitlines()
ROTULO = ('**', '#', '---', '- `', '```')


def preenchido(padrao):
    """Ha texto do aluno logo depois do rotulo, na mesma linha ou abaixo?"""
    for i, linha in enumerate(LINHAS):
        achado = re.search(padrao, linha)
        if not achado:
            continue
        if linha[achado.end():].strip(' :*`-'):
            return True
        for proxima in LINHAS[i + 1:]:
            texto = proxima.strip()
            if not texto:
                continue
            return not texto.startswith(ROTULO)
        return False
    return False


matricula = re.search(r'\b\d{5,}\b', readme)
sensor = re.search(r'S-(\d{3})\b', html)
JA_EXISTIAM = ('101', '102', '103', '104', '210')

checagens = [
    ('M0', 'Nome e matricula no README',
     bool(matricula) and 'Escreva aqui' not in readme),
    ('M1', 'Erro de digitacao "temepratura" corrigido',
     'temepratura' not in html and 'temperatura' in html.lower()),
    ('M1', 'Sensor proprio cadastrado no index.html',
     bool(sensor) and sensor.group(1) not in JA_EXISTIAM),
    ('M1', 'Cor do cabecalho trocada para #0B6E4F',
     '#0b6e4f' in css.lower() and '#999999' not in css.lower()),
    ('M2', 'Commit culpado identificado no RESPOSTAS.md',
     preenchido(r'\*\*Hash curto do commit[^*]*\*\*')),
    ('M3', 'Arquivo .gitignore existe e cita as credenciais',
     'credenciais.env' in gitignore),
    ('M3', 'config/credenciais.env fora do rastreio do Git',
     not rastreado('config/credenciais.env')),
    ('M3', 'Resposta sobre o historico preenchida',
     preenchido(r'explicando o motivo:\*\*')),
    ('M4', 'Nenhum marcador de conflito sobrou nos arquivos',
     '<<<<<<<' not in html and '>>>>>>>' not in html),
    ('M4', 'Explicacao dos marcadores preenchida',
     preenchido(r'`<<<<<<<` :')),
]

largura = max(len(titulo) for _, titulo, _ in checagens)
falhas = 0
missao_atual = None
print()
for missao, titulo, ok in checagens:
    if missao != missao_atual:
        print('  ' + missao)
        missao_atual = missao
    print('    [%s] %s' % ('x' if ok else ' ', titulo.ljust(largura)))
    if not ok:
        falhas += 1

total = len(checagens)
print('\n  %d de %d itens concluidos.\n' % (total - falhas, total))
sys.exit(1 if falhas else 0)
