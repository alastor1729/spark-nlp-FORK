---
layout: model
title: Arabic whisper_small_eg_pipeline pipeline WhisperForCTC from abuelnasr
author: John Snow Labs
name: whisper_small_eg_pipeline
date: 2024-12-15
tags: [ar, open_source, pipeline, onnx]
task: Automatic Speech Recognition
language: ar
edition: Spark NLP 5.5.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained WhisperForCTC, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`whisper_small_eg_pipeline` is a Arabic model originally trained by abuelnasr.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/whisper_small_eg_pipeline_ar_5.5.1_3.0_1734237849304.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/whisper_small_eg_pipeline_ar_5.5.1_3.0_1734237849304.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
pipeline = PretrainedPipeline("whisper_small_eg_pipeline", lang = "ar")
annotations =  pipeline.transform(df)
```
```scala
val pipeline = new PretrainedPipeline("whisper_small_eg_pipeline", lang = "ar")
val annotations = pipeline.transform(df)
```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|whisper_small_eg_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|ar|
|Size:|1.7 GB|

## References

References

https://huggingface.co/abuelnasr/whisper-small-eg

## Included Models

- AudioAssembler
- WhisperForCTC