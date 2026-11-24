# Agente de Dúvidas da EstudaMais

Primeira versão do Agente de Dúvidas, baseada em regras fixas em Python.

## Arquivos

- `agente.py`: classe `AgenteDuvidas` e suas respostas fixas.
- `principal.py`: programa interativo com `input()` e `print()`.
- `teste_agente.py`: testes automáticos com `assert`.
- `agente_duvidas.ipynb`: notebook para VS Code e Google Colab.

## Executar

```bash
python principal.py
python teste_agente.py
```

## Perguntas cadastradas

- O que é Python?
- O que é API?
- O que é banco de dados?
- O que é programação?

As perguntas são normalizadas com `lower()` e `strip()`. O agente compara textos exatos e não utiliza inteligência artificial nesta versão.
