---
layout: model
title: English kaggle_nlp_with_desaster_tweets_01_pipeline pipeline DistilBertForSequenceClassification from RowekBrah
author: John Snow Labs
name: kaggle_nlp_with_desaster_tweets_01_pipeline
date: 2024-12-15
tags: [en, open_source, pipeline, onnx]
task: Text Classification
language: en
edition: Spark NLP 5.5.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained DistilBertForSequenceClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`kaggle_nlp_with_desaster_tweets_01_pipeline` is a English model originally trained by RowekBrah.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/kaggle_nlp_with_desaster_tweets_01_pipeline_en_5.5.1_3.0_1734248772587.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/kaggle_nlp_with_desaster_tweets_01_pipeline_en_5.5.1_3.0_1734248772587.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("kaggle_nlp_with_desaster_tweets_01_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("kaggle_nlp_with_desaster_tweets_01_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|kaggle_nlp_with_desaster_tweets_01_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|249.5 MB|

## References

https://huggingface.co/RowekBrah/Kaggle_NLP_with_desaster_tweets_01

## Included Models

- DocumentAssembler
- TokenizerModel
- DistilBertForSequenceClassification