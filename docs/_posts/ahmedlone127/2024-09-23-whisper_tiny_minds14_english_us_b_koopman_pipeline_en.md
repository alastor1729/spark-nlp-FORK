---
layout: model
title: English whisper_tiny_minds14_english_us_b_koopman_pipeline pipeline WhisperForCTC from b-koopman
author: John Snow Labs
name: whisper_tiny_minds14_english_us_b_koopman_pipeline
date: 2024-09-23
tags: [en, open_source, pipeline, onnx]
task: Automatic Speech Recognition
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

Pretrained WhisperForCTC, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`whisper_tiny_minds14_english_us_b_koopman_pipeline` is a English model originally trained by b-koopman.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/whisper_tiny_minds14_english_us_b_koopman_pipeline_en_5.5.0_3.0_1727051433077.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/whisper_tiny_minds14_english_us_b_koopman_pipeline_en_5.5.0_3.0_1727051433077.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("whisper_tiny_minds14_english_us_b_koopman_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("whisper_tiny_minds14_english_us_b_koopman_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|whisper_tiny_minds14_english_us_b_koopman_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|390.9 MB|

## References

https://huggingface.co/b-koopman/whisper-tiny-minds14-en-US

## Included Models

- AudioAssembler
- WhisperForCTC