"""
Trabalho Prático 1.9: Sistema de Recomendação Simples (Análise de Similaridade)
Tema: Sistema de recomendação de filmes usando Similaridade de Jaccard e Cosseno
"""

import math
from collections import defaultdict


# ============================================================
# 1. DADOS DE ITENS (15 filmes com tags/gêneros)
# ============================================================

itens = {
    1:  {'titulo': 'Inception',              'tags': ['acao', 'ficcao_cientifica', 'suspense', 'drama', 'misterio']},
    2:  {'titulo': 'Interstellar',           'tags': ['ficcao_cientifica', 'drama', 'aventura', 'espaco', 'emocional']},
    3:  {'titulo': 'The Dark Knight',        'tags': ['acao', 'suspense', 'drama', 'crime', 'super_heroi']},
    4:  {'titulo': 'Avengers: Endgame',      'tags': ['acao', 'aventura', 'super_heroi', 'ficcao_cientifica', 'fantasia']},
    5:  {'titulo': 'The Matrix',             'tags': ['acao', 'ficcao_cientifica', 'suspense', 'filosofia', 'tecnologia']},
    6:  {'titulo': 'Forrest Gump',           'tags': ['drama', 'romance', 'historico', 'emocional', 'familia']},
    7:  {'titulo': 'The Shawshank Redemption','tags': ['drama', 'crime', 'emocional', 'esperanca', 'prisao']},
    8:  {'titulo': 'Pulp Fiction',           'tags': ['crime', 'suspense', 'drama', 'violencia', 'nao_linear']},
    9:  {'titulo': 'The Godfather',          'tags': ['crime', 'drama', 'familia', 'historico', 'violencia']},
    10: {'titulo': 'Toy Story',              'tags': ['animacao', 'familia', 'aventura', 'comedia', 'amizade']},
    11: {'titulo': 'Spirited Away',          'tags': ['animacao', 'fantasia', 'aventura', 'familia', 'magico']},
    12: {'titulo': 'Parasite',              'tags': ['suspense', 'drama', 'crime', 'social', 'misterio']},
    13: {'titulo': 'Gladiator',             'tags': ['acao', 'drama', 'historico', 'aventura', 'guerra']},
    14: {'titulo': 'The Lion King',         'tags': ['animacao', 'familia', 'drama', 'aventura', 'emocional']},
    15: {'titulo': 'Doctor Strange',        'tags': ['acao', 'fantasia', 'super_heroi', 'aventura', 'magico']},
}


# ============================================================
# 2. CÁLCULO DE SIMILARIDADE DE JACCARD
# ============================================================

def similaridade_jaccard(set1, set2):
    """
    Calcula a similaridade de Jaccard entre dois sets de tags.
    Jaccard = |A ∩ B| / |A ∪ B|
    Retorna valor entre 0.0 (sem similaridade) e 1.0 (idênticos).
    """
    set1 = set(set1)
    set2 = set(set2)

    intersecao = set1 & set2
    uniao = set1 | set2

    if not uniao:
        return 0.0

    return len(intersecao) / len(uniao)


# ============================================================
# 3. CÁLCULO DE SIMILARIDADE DE COSSENO (BÔNUS)
# ============================================================

def _construir_vetor(tags, vocabulario):
    """Converte uma lista de tags em vetor binário baseado no vocabulário."""
    return [1 if palavra in tags else 0 for palavra in vocabulario]


def similaridade_cosseno(vetor1, vetor2):
    """
    Calcula a similaridade de Cosseno entre dois vetores binários.
    Cosseno = (A · B) / (|A| * |B|)
    Retorna valor entre 0.0 e 1.0.
    """
    produto_interno = sum(a * b for a, b in zip(vetor1, vetor2))
    magnitude1 = math.sqrt(sum(a ** 2 for a in vetor1))
    magnitude2 = math.sqrt(sum(b ** 2 for b in vetor2))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0

    return produto_interno / (magnitude1 * magnitude2)


def _obter_vocabulario(itens):
    """Coleta todas as tags únicas do catálogo."""
    vocab = set()
    for item in itens.values():
        vocab.update(item['tags'])
    return sorted(vocab)


# ============================================================
# 4. FUNÇÃO DE RECOMENDAÇÃO
# ============================================================

def recomendar_itens(item_id, itens, num_recomendacoes=5, metodo='jaccard'):
    """
    Recomenda os itens mais semelhantes a um item dado.

    Parâmetros:
        item_id (int)          : ID do item de referência
        itens (dict)           : Dicionário com todos os itens
        num_recomendacoes (int): Quantidade de recomendações (padrão: 5)
        metodo (str)           : 'jaccard' ou 'cosseno'

    Retorna:
        Lista de tuplas (id, titulo, similaridade) ordenada por similaridade.
    """
    if item_id not in itens:
        print(f"[ERRO] Item com ID {item_id} não encontrado.")
        return []

    item_ref = itens[item_id]
    tags_ref = item_ref['tags']
    similaridades = []

    # Vocabulário global (necessário apenas para cosseno)
    vocabulario = _obter_vocabulario(itens) if metodo == 'cosseno' else None
    if metodo == 'cosseno':
        vetor_ref = _construir_vetor(tags_ref, vocabulario)

    for id_item, dados in itens.items():
        if id_item == item_id:
            continue  # Exclui o próprio item

        tags_item = dados['tags']

        if metodo == 'jaccard':
            score = similaridade_jaccard(tags_ref, tags_item)
        elif metodo == 'cosseno':
            vetor_item = _construir_vetor(tags_item, vocabulario)
            score = similaridade_cosseno(vetor_ref, vetor_item)
        else:
            raise ValueError(f"Método '{metodo}' inválido. Use 'jaccard' ou 'cosseno'.")

        similaridades.append((id_item, dados['titulo'], round(score, 4)))

    # Ordena por similaridade decrescente e retorna os top N
    similaridades.sort(key=lambda x: x[2], reverse=True)
    return similaridades[:num_recomendacoes]


# ============================================================
# 5. EXIBIÇÃO DE RESULTADOS
# ============================================================

def exibir_recomendacoes(item_id, itens, num_recomendacoes=5, metodo='jaccard'):
    """Exibe as recomendações de forma formatada."""
    if item_id not in itens:
        print(f"[ERRO] Item ID {item_id} não existe.")
        return

    titulo_ref = itens[item_id]['titulo']
    tags_ref   = itens[item_id]['tags']

    print("=" * 55)
    print(f"  Filme de referência : {titulo_ref} (ID: {item_id})")
    print(f"  Tags                : {', '.join(tags_ref)}")
    print(f"  Método              : {metodo.capitalize()}")
    print(f"  Top {num_recomendacoes} recomendações:")
    print("=" * 55)

    recomendacoes = recomendar_itens(item_id, itens, num_recomendacoes, metodo)

    if not recomendacoes:
        print("  Nenhuma recomendação encontrada.")
        return

    for rank, (id_item, titulo, score) in enumerate(recomendacoes, start=1):
        barra = '█' * int(score * 20)
        print(f"  {rank}. {titulo:<30} Similaridade: {score:.4f}  {barra}")

    print("=" * 55)
    print()


# ============================================================
# 6. PROGRAMA PRINCIPAL
# ============================================================

if __name__ == "__main__":

    print("\n" + "=" * 55)
    print("   SISTEMA DE RECOMENDAÇÃO DE FILMES")
    print("   Trabalho Prático 1.9 — Análise de Similaridade")
    print("=" * 55)

    print("\n📋 Catálogo de filmes disponíveis:")
    for id_filme, dados in itens.items():
        print(f"  [{id_filme:2}] {dados['titulo']:<30} | Tags: {', '.join(dados['tags'])}")

    print()

    # --- Testes com Jaccard ---
    exibir_recomendacoes(item_id=1, itens=itens, num_recomendacoes=5, metodo='jaccard')
    exibir_recomendacoes(item_id=10, itens=itens, num_recomendacoes=5, metodo='jaccard')

    # --- Testes com Cosseno ---
    exibir_recomendacoes(item_id=1, itens=itens, num_recomendacoes=5, metodo='cosseno')
    exibir_recomendacoes(item_id=10, itens=itens, num_recomendacoes=5, metodo='cosseno')

    # --- Comparação direta entre dois filmes ---
    print("=" * 55)
    print("  Comparação direta: Inception vs The Matrix")
    tags_a = set(itens[1]['tags'])
    tags_b = set(itens[5]['tags'])
    jaccard = similaridade_jaccard(tags_a, tags_b)
    vocab   = _obter_vocabulario(itens)
    vec_a   = _construir_vetor(itens[1]['tags'], vocab)
    vec_b   = _construir_vetor(itens[5]['tags'], vocab)
    cosseno = similaridade_cosseno(vec_a, vec_b)
    print(f"  Jaccard : {jaccard:.4f}")
    print(f"  Cosseno : {cosseno:.4f}")
    print("=" * 55)
