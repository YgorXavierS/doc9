from datetime import datetime
from config.log import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

class Data():
    def __init__(self,dataDevalidacao):
        self.dataDevalidacao = dataDevalidacao

    @classmethod
    def formatacao_de_texto_link(self,link):
        try:
            return link
        except Exception as e:
            logger.error(f"Erro de fortatacao de texto: {str(e)}")
            return False
            
       
        
  
    def tratamento_de_dados(self,dadosBrutos):
        try:
            dadosTratados = []
            for fatura in dadosBrutos:
             
                dataDaFatura =  datetime.strptime(fatura[2], '%d-%m-%Y').date()
               
                if (dataDaFatura >= self.dataDevalidacao):
                    if(fatura in dadosTratados):
                        continue
                    fatura[3] = self.formatacao_de_texto_link(fatura[3])
                    dadosTratados.append(fatura)
                    logger.info(f"dados tratados {fatura} - sucesso")
            
            return (dadosTratados)
        
        except Exception as e:
            logger.error(f"Erro de dados: {str(e)}")
            return False
    
 