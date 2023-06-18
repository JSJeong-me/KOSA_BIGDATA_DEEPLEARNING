# KOSA_BIGDATA_DEEPLEARNING
KOSA Bigdata DeepLearning Analysis - 2023년 6월 20~24일 (4일간, 8시간x4일 총 32시간)
```
과정 소개

1일차: 생성형 AI를 이용한 Python 프로그램 코딩 및 Docker & Kubernetes 환경 구축

2일차: Docker 와 Fluentd를 이용한 데이터 수집(File, TCP, HTTP)

3일차: EFK를 이용한 Kubernetes 데이터 수집 및 시각화

4일차: 데이터 Featuring 및 딥러닝 모델 생성
```
<img width="1152" alt="curi" src="https://github.com/JSJeong-me/KOSA_BIGDATA_DEEPLEARNING/assets/54794815/f1cfd814-f2d6-4ae4-b32e-aaae19fcab52">

### 빅데이터 파이럿 아키텍처?

  빅데이터 파이럿 프로젝트의 아키텍처는 일반적으로 다음과 같은 구성 요소를 포함합니다:

  1. **데이터 수집**: 이 단계에서는 다양한 소스에서 데이터를 수집합니다. 이는 로그 파일, 데이터베이스, 실시간 피드 등이 될 수 있습니다. Apache Flume, Logstash 또는 Kafka와 같은 도구가 이 단계에서 사용될 수 있습니다.

  2. **데이터 저장**: 수집된 데이터는 처리를 위해 저장됩니다. 이는 일반적으로 분산 파일 시스템, 예를 들어 Hadoop의 HDFS나 Amazon의 S3와 같은 클라우드 기반 스토리지에 저장됩니다.

  3. **데이터 처리**: 저장된 데이터는 분석을 위해 처리됩니다. 이는 일반적으로 MapReduce, Spark, Flink 등의 프레임워크를 사용하여 수행됩니다.

  4. **데이터 분석**: 처리된 데이터는 분석 도구를 사용하여 분석됩니다. 이는 SQL 쿼리 도구(Hive, Impala), 머신러닝 라이브러리(Spark MLlib, H2O) 또는 데이터 시각화 도구(Tableau, PowerBI) 등이 될 수 있습니다.

  5. **데이터 관리**: 모든 이러한 단계를 관리하고 조정하는 데는 데이터 관리 도구가 필요합니다. 이는 일반적으로 워크플로우 관리 시스템(Airflow, Oozie), 데이터 카탈로그(Hive Metastore, AWS Glue), 또는 데이터 라인리지 도구(Apache Atlas) 등을 포함합니다.

  이러한 아키텍처는 파이럿 프로젝트의 시작점일 뿐이며, 특정 요구 사항에 따라 조정되거나 확장될 수 있습니다. 또한, 이러한 각 단계는 보안, 거버넌스, 데이터 품질 관리 등의 고려 사항을 포함해야 합니다.
