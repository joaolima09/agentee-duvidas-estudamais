from agente import AgenteDuvidas

agente = AgenteDuvidas("Tutor IA")

assert agente.nome == "Tutor IA"
assert agente.responder("O que é Python?") == "Python é uma linguagem de programação."
assert agente.responder("O QUE É API?") == "API é uma forma de comunicação entre sistemas."
assert agente.responder("  o que é api?  ") == "API é uma forma de comunicação entre sistemas."
assert agente.responder("O que é banco de dados?") == "Banco de dados é um sistema que armazena informações organizadas."
assert agente.responder("O que é Inteligência Artificial?") == "Inteligência Artificial é a área da computação que busca criar sistemas capazes de realizar tarefas que exigem raciocínio ou aprendizado."
assert agente.responder("O que é banco de dados") == "Desculpe, ainda não sei responder essa pergunta."

print("✅ Todos os testes passaram!")
