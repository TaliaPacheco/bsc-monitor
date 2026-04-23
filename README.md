 # BSC Monitor                                                                                                                                                                                                   
                  
  Sistema de monitoramento de wallets na Binance Smart Chain (BSC).                                                                                                                                               
  Composto por 3 projetos independentes que juntos formam um pipeline completo
  de coleta, armazenamento e visualização de saldos on-chain.                                                                                                                                                     
                  
  ## Projetos                                                                                                                                                                                                     
                  
  | # | Pasta | Descrição |                                                                                                                                                                                       
  |---|-------|-----------|
  | 1 | [`projeto-1-script`](./projeto-1-script) | Script de consulta de saldos na BSC (BNB nativo + BEP-20) |                                                                                                    
  | 2 | `projeto-2-api` | Pipeline de coleta + PostgreSQL + API FastAPI *(em breve)* |                                                                                                                            
  | 3 | `projeto-3-grafana` | Dashboard Grafana consumindo o banco do projeto 2 *(em breve)* |                                                                                                                    
                                                                                                                                                                                                                  
  ## Stack                                                                                                                                                                                                        
                                                                                                                                                                                                                  
  - **Python 3.11+**
  - **web3.py** — interação com a BSC
  - **FastAPI** — API REST *(projeto 2)*                                                                                                                                                                          
  - **PostgreSQL** — persistência *(projeto 2)*                                                                                                                                                                   
  - **Grafana** — visualização *(projeto 3)*                                                                                                                                                                      
                                                                                                                                                                                                                  
  ## Como usar                                                                                                                                                                                                    
   
  Cada projeto é independente e tem seu próprio `README.md` com instruções.                                                                                                                                       
  Comece pelo [projeto 1](./projeto-1-script).
                                                                                                                                                                                                                  
  --- 