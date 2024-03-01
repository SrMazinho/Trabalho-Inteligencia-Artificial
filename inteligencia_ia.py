
class StreamingService:
    def __init__(self):
        self.catalog = {
            "Filmes": ["Filme 1", "Filme 2", "Filme 3"],
            "Séries": ["Série 1", "Série 2", "Série 3"]
        }

    def show_catalog(self):
        print("Catálogo de Filmes e Séries:")
        for category, titles in self.catalog.items():
            print(f"\n{category}:")
            for title in titles:
                print(f"- {title}")

    def start_streaming(self):
        self.show_catalog()
        choice = input("\nDigite o nome do filme ou série que deseja assistir ou 'sair' para sair: ")
        while choice.lower() != "sair":
            found = False
            for titles in self.catalog.values():
                if choice in titles:
                    found = True
                    print(f"\nIniciando a reprodução de '{choice}'...")
                    break
            if not found:
                print("Desculpe, o título especificado não está disponível.")
            choice = input("\nDigite o nome do filme ou série que deseja assistir ou 'sair' para sair: ")
        print("Obrigado por usar o nosso serviço de streaming!")

# Instanciando o serviço de streaming
streaming_service = StreamingService()
# Iniciando o streaming
streaming_service.start_streaming()