from sensor.utils import get_collection_as_dataframe
from sensor.entity import config_entity
if __name__ == "__main__":
     try:
          training_pipeline_config = config_entity.TrainingPipelineConfig()
          data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
          #get_collection_as_dataframe(database_name='aps',collection_name='sensor')
     except:...