---
layout: model
title: Vietnamese t5_vit5_base_pipeline pipeline T5Transformer from VietAI
author: John Snow Labs
name: t5_vit5_base_pipeline
date: 2024-08-18
tags: [vi, open_source, pipeline, onnx]
task: [Question Answering, Summarization, Translation, Text Generation]
language: vi
edition: Spark NLP 5.4.2
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained T5Transformer, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`t5_vit5_base_pipeline` is a Vietnamese model originally trained by VietAI.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/t5_vit5_base_pipeline_vi_5.4.2_3.0_1724009069527.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/t5_vit5_base_pipeline_vi_5.4.2_3.0_1724009069527.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("t5_vit5_base_pipeline", lang = "vi")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("t5_vit5_base_pipeline", lang = "vi")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|t5_vit5_base_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.4.2+|
|License:|Open Source|
|Edition:|Official|
|Language:|vi|
|Size:|537.3 MB|

## References

https://huggingface.co/VietAI/vit5-base

## Included Models

- DocumentAssembler
- T5Transformer