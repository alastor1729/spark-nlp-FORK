---
layout: model
title: English db_fe2_5_2_1_pipeline pipeline DistilBertForSequenceClassification from exala
author: John Snow Labs
name: db_fe2_5_2_1_pipeline
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

Pretrained DistilBertForSequenceClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`db_fe2_5_2_1_pipeline` is a English model originally trained by exala.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/db_fe2_5_2_1_pipeline_en_5.5.1_3.0_1734249543652.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/db_fe2_5_2_1_pipeline_en_5.5.1_3.0_1734249543652.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("db_fe2_5_2_1_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("db_fe2_5_2_1_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|db_fe2_5_2_1_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|249.7 MB|

## References

https://huggingface.co/exala/db_fe2_5.2.1

## Included Models

- DocumentAssembler
- TokenizerModel
- DistilBertForSequenceClassification