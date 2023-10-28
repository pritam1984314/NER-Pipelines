import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"pipeline.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO  
)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("ner_pipelines")