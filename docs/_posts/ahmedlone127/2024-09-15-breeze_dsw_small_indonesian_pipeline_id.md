---
layout: model
title: Indonesian breeze_dsw_small_indonesian_pipeline pipeline WhisperForCTC from hanasim
author: John Snow Labs
name: breeze_dsw_small_indonesian_pipeline
date: 2024-09-15
tags: [id, open_source, pipeline, onnx]
task: Automatic Speech Recognition
language: id
edition: Spark NLP 5.5.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained WhisperForCTC, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`breeze_dsw_small_indonesian_pipeline` is a Indonesian model originally trained by hanasim.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/breeze_dsw_small_indonesian_pipeline_id_5.5.0_3.0_1726431106926.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/breeze_dsw_small_indonesian_pipeline_id_5.5.0_3.0_1726431106926.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("breeze_dsw_small_indonesian_pipeline", lang = "id")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("breeze_dsw_small_indonesian_pipeline", lang = "id")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|breeze_dsw_small_indonesian_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|id|
|Size:|1.1 GB|

## References

https://huggingface.co/hanasim/breeze-dsw-small-id

## Included Models

- AudioAssembler
- WhisperForCTC