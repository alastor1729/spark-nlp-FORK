---
layout: model
title: English bert_tiny_lda_20_cola_pipeline pipeline DistilBertForSequenceClassification from gokulsrinivasagan
author: John Snow Labs
name: bert_tiny_lda_20_cola_pipeline
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

Pretrained DistilBertForSequenceClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`bert_tiny_lda_20_cola_pipeline` is a English model originally trained by gokulsrinivasagan.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_tiny_lda_20_cola_pipeline_en_5.5.1_3.0_1734248482638.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/bert_tiny_lda_20_cola_pipeline_en_5.5.1_3.0_1734248482638.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("bert_tiny_lda_20_cola_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("bert_tiny_lda_20_cola_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_tiny_lda_20_cola_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|123.9 MB|

## References

https://huggingface.co/gokulsrinivasagan/bert_tiny_lda_20_cola

## Included Models

- DocumentAssembler
- TokenizerModel
- DistilBertForSequenceClassification