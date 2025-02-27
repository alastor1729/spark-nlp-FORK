---
layout: model
title: English autotrain_bertbase_imdb_1275748792_pipeline pipeline BertForSequenceClassification from sasha
author: John Snow Labs
name: autotrain_bertbase_imdb_1275748792_pipeline
date: 2024-09-25
tags: [en, open_source, pipeline, onnx]
task: Text Classification
language: en
edition: Spark NLP 5.5.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained BertForSequenceClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`autotrain_bertbase_imdb_1275748792_pipeline` is a English model originally trained by sasha.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/autotrain_bertbase_imdb_1275748792_pipeline_en_5.5.0_3.0_1727277487477.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/autotrain_bertbase_imdb_1275748792_pipeline_en_5.5.0_3.0_1727277487477.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("autotrain_bertbase_imdb_1275748792_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("autotrain_bertbase_imdb_1275748792_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|autotrain_bertbase_imdb_1275748792_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|409.4 MB|

## References

https://huggingface.co/sasha/autotrain-BERTBase-imdb-1275748792

## Included Models

- DocumentAssembler
- TokenizerModel
- BertForSequenceClassification