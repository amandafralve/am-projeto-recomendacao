# 🤖 AM-PROJETO-RECOMENDACAO
Este repositório contém os estudos e implementações para o projeto de Aprendizado de Máquina focado em sistemas de recomendação e fundamentos de redes neurais.

### Estrutura de Pastas
A organização do projeto segue uma divisão por módulos de aprendizado:

```python
AM-PROJETO-RECOMENDACAO/
├── 01-introducao/      # Primeiros passos e testes de ambiente.
├── 02-perceptron/      # Implementação estruturada da rede Perceptron.
│   ├── data/           # Bases de dados.
│   ├── notebooks/      # Análises e experimentos (Jupyter).
│   └── src/            # Código-fonte da aplicação (API e Modelos).
└── atv1-t1-perceptron-manual/        # Atividade prática de Perceptron.
```

## AT1 - Criar um Perceptron manual
>
>Escolha uma base do Kaggle, crie um projeto com um Perceptron de no mínimo duas entradas + bias, com o código manual sem numpy ou qualquer outra library
>- Crie tudo em um notebook onde mostre alguns detalhes sobre o dataset, alguns gráficos e principalmente os dados que foram escolhidos como entradas para o Perceptron.
>- Função do perceptron e exemplos do funcionando dentro do mesmo notebook.

<br>
<details>
    <summary><b>About Dataset (Resident Evil)</b></summary>
    <br>
    Resident Evil narrative dataset with games, characters, scenes and interactions extracted from fan-made game transcripts and enriched with AI.


    - **games.csv** – `id, title, year, type, chronology_order`
        
        Mainline titles and selected spin‑offs (Revelations, Shadow of Rose, Code Veronica), with release year and custom story chronology.
        
    - **characters.csv** – `id, name, role`
        
        Playable and key NPCs across the saga, with coarse roles (`hero`, `villain`, `support`); RE4 cast is scraped, the rest AI‑assisted and curated.
        
    - **gameAppearance.csv** – `gameId, characterId, role`
        
        Per‑game presence and narrative role of each character (e.g., Jill as hero in RE1/RE3, Wesker as villain in multiple titles).
        
    - **scenes.csv** – `game_id, scene_id, title, source`
        
        Story segments (cutscenes, set‑piece events) parsed from fan‑made transcripts, one row per narrative scene.
        
    - **interactions.csv** – `game_id, scene_id, character_id`
        
        Character‑level presence per scene, derived by mapping speaker names in the scripts to canonical characters; useful for counts, co‑occurrence networks and social network analysis.

</details>