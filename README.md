# KOSA_BIGDATA_DEEPLEARNING
KOSA Bigdata DeepLearning Analysis


![0_BIGDATA_ML](https://user-images.githubusercontent.com/54794815/159915464-ddc9c0bd-0ff5-41d9-b8d0-2423152acd9a.jpg)


### 빅데이터 파이럿 아키텍처?

  빅데이터 파이럿 프로젝트의 아키텍처는 일반적으로 다음과 같은 구성 요소를 포함합니다:

  1. **데이터 수집**: 이 단계에서는 다양한 소스에서 데이터를 수집합니다. 이는 로그 파일, 데이터베이스, 실시간 피드 등이 될 수 있습니다. Apache Flume, Logstash 또는 Kafka와 같은 도구가 이 단계에서 사용될 수 있습니다.

  2. **데이터 저장**: 수집된 데이터는 처리를 위해 저장됩니다. 이는 일반적으로 분산 파일 시스템, 예를 들어 Hadoop의 HDFS나 Amazon의 S3와 같은 클라우드 기반 스토리지에 저장됩니다.

  3. **데이터 처리**: 저장된 데이터는 분석을 위해 처리됩니다. 이는 일반적으로 MapReduce, Spark, Flink 등의 프레임워크를 사용하여 수행됩니다.

  4. **데이터 분석**: 처리된 데이터는 분석 도구를 사용하여 분석됩니다. 이는 SQL 쿼리 도구(Hive, Impala), 머신러닝 라이브러리(Spark MLlib, H2O) 또는 데이터 시각화 도구(Tableau, PowerBI) 등이 될 수 있습니다.

  5. **데이터 관리**: 모든 이러한 단계를 관리하고 조정하는 데는 데이터 관리 도구가 필요합니다. 이는 일반적으로 워크플로우 관리 시스템(Airflow, Oozie), 데이터 카탈로그(Hive Metastore, AWS Glue), 또는 데이터 라인리지 도구(Apache Atlas) 등을 포함합니다.

  이러한 아키텍처는 파이럿 프로젝트의 시작점일 뿐이며, 특정 요구 사항에 따라 조정되거나 확장될 수 있습니다. 또한, 이러한 각 단계는 보안, 거버넌스, 데이터 품질 관리 등의 고려 사항을 포함해야 합니다.
