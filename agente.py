class AgenteDuvidas:

    def __init__(self, nome):
        self.nome = nome

    def responder(self, pergunta):
        pergunta = pergunta.lower().strip()

        if pergunta == "o que é python?":
            return "Python é uma linguagem de programação."

        elif pergunta == "o que é api?":
            return "API é uma forma de comunicação entre sistemas."

        elif pergunta == "o que é banco de dados?":
            return "Banco de dados é um sistema que armazena informações organizadas."

        elif pergunta == "o que é inteligência artificial?":
            return "Inteligência Artificial é a área da computação que busca criar sistemas capazes de realizar tarefas que exigem raciocínio ou aprendizado."

        return "Desculpe, ainda não sei responder essa pergunta."
