---
layout: model
title: English image_captioning_vit_gpt2_pipeline pipeline VisionEncoderDecoderForImageCaptioning from nlpconnect
author: John Snow Labs
name: image_captioning_vit_gpt2_pipeline
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

Pretrained VisionEncoderDecoderForImageCaptioning, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`image_captioning_vit_gpt2_pipeline` is a English model originally trained by nlpconnect.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/image_captioning_vit_gpt2_pipeline_en_5.5.1_3.0_1734225676600.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/image_captioning_vit_gpt2_pipeline_en_5.5.1_3.0_1734225676600.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("image_captioning_vit_gpt2_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("image_captioning_vit_gpt2_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|image_captioning_vit_gpt2_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|1.0 GB|

## References

https://huggingface.co/nlpconnect/vit-gpt2-image-captioning

## Included Models

- ImageAssembler
- VisionEncoderDecoderForImageCaptioning