---
layout: model
title: English indonesian_bge_small_pipeline pipeline BGEEmbeddings from ingtech
author: John Snow Labs
name: indonesian_bge_small_pipeline
date: 2024-12-18
tags: [en, open_source, pipeline, onnx]
task: Embeddings
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

Pretrained BGEEmbeddings, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`indonesian_bge_small_pipeline` is a English model originally trained by ingtech.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/indonesian_bge_small_pipeline_en_5.5.1_3.0_1734562388032.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/indonesian_bge_small_pipeline_en_5.5.1_3.0_1734562388032.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
pipeline = PretrainedPipeline("indonesian_bge_small_pipeline", lang = "en")
annotations =  pipeline.transform(df)
```
```scala
val pipeline = new PretrainedPipeline("indonesian_bge_small_pipeline", lang = "en")
val annotations = pipeline.transform(df)
```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|indonesian_bge_small_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|117.1 MB|

## References

References

https://huggingface.co/ingtech/indonesian-bge-small

## Included Models

- DocumentAssembler
- BGEEmbeddings