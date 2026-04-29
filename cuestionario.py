class pregunta:
    def __init__(self, preguntas, respuestas):
        self.preguntas = preguntas
        self.respuestas = respuestas


questionario_preguntas = ["Como estas?\n(a) Bien\n(b) Mal\n(c) velociraptor\n\n",
                          "Que edad tienes?\n(a) 18\n(b) 200\n(c) no\n\n",
                          "Cual es tu color favorito?\n(a) Azul\n(b) verde azulado ligeramente manchado con rojo oscuro\n(c) jueves\n\n"
                          ]

preguntas = [
    pregunta(questionario_preguntas[0], "a"),
    pregunta(questionario_preguntas[1], "c"),
    pregunta(questionario_preguntas[2], "b")
]

def questionario(preguntas):
    puntuacion = 0
    for pregunta in preguntas:
        respuesta = input(pregunta.preguntas)
        if respuesta == pregunta.respuestas:
            puntuacion += 1
        print("sacaste " +str(puntuacion) + "/" + str(len(preguntas)) + " respuestas correctas")

questionario(preguntas)