---
layout: model
title: French trocr_medieval_humanistica_pipeline pipeline VisionEncoderDecoderForImageCaptioning from medieval-data
author: John Snow Labs
name: trocr_medieval_humanistica_pipeline
date: 2024-12-18
tags: [fr, open_source, pipeline, onnx]
task: Image Captioning
language: fr
edition: Spark NLP 5.5.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained VisionEncoderDecoderForImageCaptioning, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`trocr_medieval_humanistica_pipeline` is a French model originally trained by medieval-data.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/trocr_medieval_humanistica_pipeline_fr_5.5.1_3.0_1734540511942.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/trocr_medieval_humanistica_pipeline_fr_5.5.1_3.0_1734540511942.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("trocr_medieval_humanistica_pipeline", lang = "fr")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("trocr_medieval_humanistica_pipeline", lang = "fr")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|trocr_medieval_humanistica_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|fr|
|Size:|1.4 GB|

## References

https://huggingface.co/medieval-data/trocr-medieval-humanistica

## Included Models

- ImageAssembler
- VisionEncoderDecoderForImageCaptioning