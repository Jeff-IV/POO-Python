 #usando una IA para analizar un texto en este caso solo funciona con el texto en inglés
from textblob import TextBlob

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self,texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0:
                return "positivo"
        elif analisis.sentiment.polarity == 0:
                return "neutral"
        else:
                return "negativo"
            

print("""
      
     ANALIZADOR DE SENTIMIENTOS
    
       """)
analizador = AnalizadorDeSentimientos()
resultado = analizador.analizar_sentimiento("hello, i wanna play with angel but he is so good what i should do?")
print(resultado)
            
