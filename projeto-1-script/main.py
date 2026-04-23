import os       
import sys

from dotenv import load_dotenv
from web3 import Web3


def main() -> None:
    load_dotenv()
    
    rpc_url = os.getenv("RPC_URL")
    if not rpc_url:
        print("Variavel RPC_URL nao encontrada no .env")
        print("Copie .env.example para .env e preencha os valores.")
        sys.exit(1)
                                                                                                                                                                        
    print(f"Conectando ao RPC: {rpc_url}")
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    
    try:                                                                                                                                                                                                        
        block = w3.eth.block_number
        chain_id = w3.eth.chain_id                                                                                                                                                                              
    except Exception as e:                                                                                                                                                                                      
        print(f"Nao foi possivel falar com o RPC: {e}")
        sys.exit(1)

    print(f"Conectado. Chain ID: {chain_id}, bloco atual: {block:,}")

if __name__ == "__main__":                                                                                                                                                                                      
    main()