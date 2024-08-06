import pandas as pd
from config.log import setup_logging
import logging
from datetime import date

setup_logging()
logger = logging.getLogger(__name__)

class Relatorio:
    
    @classmethod
    def criacao_de_relatorio(self,dados):
        try:
            nomeDoArquivo = (f'relatorio {date.today()}')
            df = pd.DataFrame(dados)
            df.to_csv(f'doc9/arquivos/{nomeDoArquivo}.csv')
            logger.info('Criacao de relatorio bem sucedida')
            return True
        
        except Exception as e:
            logger.error(f"Erro ao criar o relatório: {str(e)}")
            return False
    