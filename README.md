# KOSA_BIGDATA_DEEPLEARNING
KOSA Bigdata DeepLearning Analysis - 2023년 6월 20~24일 (4일간, 8시간x4일 총 32시간)

### 수업 워크(공유) Sheet:  https://han.gl/peNAER
```
과정 소개

1일차: 생성형 AI를 이용한 Python 코딩 및 Docker & Kubernetes 환경 구축

생성형 AI 교안(2~5 교시): [https://han.gl/mEpGSV] 생성형 AI 교안(6 교시): 추상화  WSL, Docker 환경 구축 교안(7~8 교시): [https://han.gl/cxfwhR]

실습 파일 1: https://github.com/JSJeong-me/KOSA_ChatGPT_0531/blob/main/Chrome_Temperature.py

실습 파일 2:

> Act as your a excellent Python programmer, please write the python code using a scrapy to get the XPath in getElements method with the followings:

> URL: https://search.rakuten.co.jp/search/mall/air+purifier/
> XPath: //*[@id="root"]/div[3]/div[2]/div[5]/div/div/div/div[1]/div[2]/h2/a


실습 파일 3: Dockerfile 작성

> write a Dockerfile for node.js application
> explain exactly what  WORKDIR directive means in dockerfile
> use yarn instead of npm in dockerfile
> now only copy relevant application files, not everything to the app image
> use multi-stage build

![image](https://github.com/JSJeong-me/KOSA_BIGDATA_DEEPLEARNING/assets/54794815/adbb39e8-3f95-4356-9c83-f7b3d8fb0e3a)



2일차: Docker 와 Fluentd를 이용한 데이터 수집(File, TCP, HTTP)

Docker 와 Fluentd 교안: https://github.com/JSJeong-me/docker/blob/main/1-%EA%B5%90%EC%95%88-Docker(1%EC%9D%BC%EC%B0%A8).pdf


3일차: EFK를 이용한 Kubernetes 데이터 수집 및 시각화

EFK 교안: https://github.com/JSJeong-me/EFK/blob/main/01_Day/EFK_Elasticsearch(1%EC%9D%BC%EC%B0%A8).pdf


4일차: 데이터 Featuring 및 딥러닝 모델 생성

교안: https://github.com/JSJeong-me/KOSA_BIGDATA_DEEPLEARNING/blob/main/Feature_Engineering/5_ML(JSJeong).pdf

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
