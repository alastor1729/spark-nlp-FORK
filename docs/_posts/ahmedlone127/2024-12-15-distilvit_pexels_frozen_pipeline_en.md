---
layout: model
title: English distilvit_pexels_frozen_pipeline pipeline VisionEncoderDecoderForImageCaptioning from tarekziade
author: John Snow Labs
name: distilvit_pexels_frozen_pipeline
date: 2024-12-15
tags: [en, open_source, pipeline, onnx]
task: Image Captioning
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

Pretrained VisionEncoderDecoderForImageCaptioning, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`distilvit_pexels_frozen_pipeline` is a English model originally trained by tarekziade.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/distilvit_pexels_frozen_pipeline_en_5.5.1_3.0_1734224769030.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/distilvit_pexels_frozen_pipeline_en_5.5.1_3.0_1734224769030.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("distilvit_pexels_frozen_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("distilvit_pexels_frozen_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|distilvit_pexels_frozen_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|825.6 MB|

## References

https://huggingface.co/tarekziade/distilvit-pexels-frozen

## Included Models

- ImageAssembler
- VisionEncoderDecoderForImageCaptioning