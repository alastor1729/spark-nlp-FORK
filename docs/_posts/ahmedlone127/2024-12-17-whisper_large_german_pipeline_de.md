---
layout: model
title: German whisper_large_german_pipeline pipeline WhisperForCTC from Krish03
author: John Snow Labs
name: whisper_large_german_pipeline
date: 2024-12-17
tags: [de, open_source, pipeline, onnx]
task: Automatic Speech Recognition
language: de
edition: Spark NLP 5.5.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained WhisperForCTC, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`whisper_large_german_pipeline` is a German model originally trained by Krish03.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/whisper_large_german_pipeline_de_5.5.1_3.0_1734404357527.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/whisper_large_german_pipeline_de_5.5.1_3.0_1734404357527.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("whisper_large_german_pipeline", lang = "de")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("whisper_large_german_pipeline", lang = "de")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|whisper_large_german_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|de|
|Size:|642.2 MB|

## References

https://huggingface.co/Krish03/whisper-large-de

## Included Models

- AudioAssembler
- WhisperForCTC