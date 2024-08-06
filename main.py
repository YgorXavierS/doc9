
from playwright.sync_api import sync_playwright,TimeoutError as PlaywrightTimeoutError
from config.log import setup_logging
import logging
import time
from datetime import datetime
from recursos.downLoad import Download
from recursos.relatorio import Relatorio

from model.data import Data




dataExecucao = ''

'''
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
'''







def main():
    with sync_playwright() as p:
        try:
            navegador = p.firefox.launch(args=['--start-maximized'],headless=False)#headless
            pagina = navegador.new_page(no_viewport=True)
        
            #pagina.set_viewport_size({"width": 1200, "height": 900})
        
            context = navegador.new_context(accept_downloads=True)
            pagina.context.clear_cookies()
            pagina.goto("https://rpachallengeocr.azurewebsites.net")
            logger.warning('Inicio do RPA')
            PAGINACAO = pagina.locator('.paginate_button')
            paginacao_quantidade =  PAGINACAO.count()
            TABELA = []
            for paginaSelecionada in range(paginacao_quantidade):
                PAGINACAO.nth(paginaSelecionada).click()
                linhas = pagina.query_selector_all('tr')
            
                for linha in linhas:
                    colunas = linha.query_selector_all('td')
                    
                    if(colunas == []):
                        continue

                    linha_valores = [coluna.inner_html() for coluna in colunas]
                    dataDaFatura =  datetime.strptime(linha_valores[2], '%d-%m-%Y').date()


                    nomeDoArquivo = (linha_valores[3].split(' ')[1]).split('/')[2]

                    if (dataDaFatura >= dataExecucao ):
                        if(linha_valores[0] in TABELA):
                            continue
                        
                        elemento = pagina.query_selector(f"a[{linha_valores[3].split(' ')[1]}]")

                        elemento.click()
                        with pagina.expect_popup() as popup_info:
                            popup = popup_info.value

                        # Verifica se a nova aba foi aberta e interage com ela
                        if popup:
                            popup.wait_for_load_state()
                            popup.screenshot(path=f"doc9/arquivos/{nomeDoArquivo.split('.')[0]}.jpg") 
                            # Captura uma screenshot da nova aba
                            popup.close()
                        time.sleep(2)

                   


                    TABELA.append(linha_valores)
                
            dadosTratados = Data(dataExecucao)
            Relatorio.criacao_de_relatorio(dadosTratados.tratamento_de_dados(TABELA))
            
            DownloadStatus = Download(pagina,dadosTratados.tratamento_de_dados(TABELA)).downLoadFatura()
    
        except Exception as e:
            logger.critical(f"Execucao inicial com erro - verificar informacoes do site principal {e}")
          


if __name__=="__main__":
    setup_logging()
    logger = logging.getLogger(__name__)
    dataExecucao = datetime.strptime('02-08-2024', '%d-%m-%Y').date()
    logger.info(f"Star Programa:{dataExecucao}")
    main()
