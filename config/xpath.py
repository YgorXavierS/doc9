from config.log import setup_logging
import logging


setup_logging()
logger = logging.getLogger(__name__)

class Xpath():        
  classmethod
  def espera_elemento_Xpath_aparecer(pagina, seletor, tempo_limite=40000):
      try:
          elemento = pagina.wait_for_selector(seletor, timeout=tempo_limite)
          logger.info(f"elemento procurado:{elemento}")
          return elemento
      except:
          logger.error(f"elemento procurado:{elemento}")
