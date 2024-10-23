import logging

# Configurazione del logging
logging.basicConfig(
    filename='log.log',  # Nome del file di log
    level=logging.DEBUG,      # Livello di log
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato del log
    filemode='w'             # Sovrascrive il file ogni volta che si apre
)

# Esempi di messaggi di log
# logging.debug('Questo è un messaggio di debug')
# logging.info('Questo è un messaggio informativo')
# logging.warning('Questo è un avviso')
# logging.error('Questo è un messaggio di errore')
# logging.critical('Questo è un messaggio critico')