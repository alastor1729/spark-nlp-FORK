---
layout: model
title: English vit_gpt2_verifycode_caption_airis_channel_pipeline pipeline VisionEncoderDecoderForImageCaptioning from AIris-Channel
author: John Snow Labs
name: vit_gpt2_verifycode_caption_airis_channel_pipeline
date: 2024-12-16
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

Pretrained VisionEncoderDecoderForImageCaptioning, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`vit_gpt2_verifycode_caption_airis_channel_pipeline` is a English model originally trained by AIris-Channel.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/vit_gpt2_verifycode_caption_airis_channel_pipeline_en_5.5.1_3.0_1734319245533.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/vit_gpt2_verifycode_caption_airis_channel_pipeline_en_5.5.1_3.0_1734319245533.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("vit_gpt2_verifycode_caption_airis_channel_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("vit_gpt2_verifycode_caption_airis_channel_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|vit_gpt2_verifycode_caption_airis_channel_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|1.0 GB|

## References

https://huggingface.co/AIris-Channel/vit-gpt2-verifycode-caption

## Included Models

- ImageAssembler
- VisionEncoderDecoderForImageCaptioning