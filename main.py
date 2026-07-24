from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

# Criação da aplicação FastAPI
app = FastAPI()

# Configuração do middleware CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Definição do caminho absoluto da pasta de imagens
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Lista de figurinhas com os campos id, nome, categoria e imagem_url
figurinhas = [
    {"id": 1, "nome": "Alan Turing", "categoria": "IA", "imagem_url": "/figurinhas/33/imagem"},
    {"id": 2, "nome": "Jhon", "categoria": "IA", "imagem_url": "/figurinhas/34/imagem"},
    # Comentário: Figurinhas ainda não disponíveis
    {"id": 3, "nome": "Ada Lovelace", "categoria": "Pioneira", "imagem_url": "/figurinhas/32/imagem"},
    {"id": 4, "nome": "Grace Hopper", "categoria": "Pioneira", "imagem_url": "/figurinhas/30/imagem"},
     {"id": 5, "nome": "Grace Hopper", "categoria": "Pioneira", "imagem_url": "/figurinhas/38/imagem"},
]

# Endpoint GET "/figurinhas" que retorna a lista de figurinhas
@app.get("/figurinhas")
async def listar_figurinhas():
    return figurinhas

# Endpoint GET "/figurinhas/{id}/imagem" que retorna a imagem de uma figurinha pelo ID
@app.get("/figurinhas/{id}/imagem")
async def obter_imagem(id: int):
    # Busca o arquivo correspondente ao ID na pasta de figurinhas
    padrao_busca = os.path.join(PASTA_IMAGENS, f"{id:02d}*")  # Exemplo: "01*", "02*"
    arquivos = glob.glob(padrao_busca)

    if not arquivos:
        # Retorna 404 se nenhum arquivo for encontrado
        raise HTTPException(status_code=404, detail="Imagem não encontrada")

    # Retorna o primeiro arquivo encontrado
    return FileResponse(arquivos[0])


#@app.get("/figurinhas")
#async def listar_figurinhas():
    #return [
        #{"id": 1, "nome": "Figurinha A", "categoria": "Categoria 1"},
        #{"id": 2, "nome": "Figurinha B", "categoria": "Categoria 2"}
    #]