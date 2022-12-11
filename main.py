from sensor.pipeline.training_pipeline import start_training_pipeline
from sensor.exception import SensorException
from sensor.pipeline.batch_prediction import start_batch_prediction
import os,sys
print(__name__)
if __name__ == "__main__":
     try:
          #start_training_pipeline()
          output_file = start_batch_prediction('/config/workspace/aps_failure_training_set1.csv')
          print(output_file)
     except Exception as e:
          raise SensorException(e, sys)