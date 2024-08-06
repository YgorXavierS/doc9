from config.xpath import Xpath
import time
class Download():
    def __init__(self,pagina,downLoadList):
        self.pagina = pagina
        self.downLoadList = downLoadList

    
    
    def downLoadFatura(self):
        for downLoadURL in self.downLoadList:
            try:
                nomeDoArquivo = (downLoadURL[3].split(' ')[1]).split('/')[2]
                elemento = self.pagina.query_selector(f"a[{downLoadURL[3].split(' ')[1]}]")

                elemento.click()
                with self.pagina.expect_popup() as popup_info:
                    popup = popup_info.value

                # Verifica se a nova aba foi aberta e interage com ela
                if popup:
                    popup.wait_for_load_state()
                    popup.screenshot(path=f"doc9/arquivos/{nomeDoArquivo.split('.')[0]}.jpg") 
                     # Captura uma screenshot da nova aba
                    popup.close()
                time.sleep(2)
            
                
            #document.querySelector('a[href="/invoices/10.jpg"]').click()
            except Exception as e:
                continue
                

        #Xpath.espera_elemento_Xpath_aparecer(self.pagina)


        
        
        