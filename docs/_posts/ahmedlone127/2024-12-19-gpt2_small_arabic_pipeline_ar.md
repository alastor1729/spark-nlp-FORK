---
layout: model
title: Arabic gpt2_small_arabic_pipeline pipeline GPT2Transformer from akhooli
author: John Snow Labs
name: gpt2_small_arabic_pipeline
date: 2024-12-19
tags: [ar, open_source, pipeline, onnx]
task: [Question Answering, Summarization, Translation, Text Generation]
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

Pretrained GPT2Transformer, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`gpt2_small_arabic_pipeline` is a Arabic model originally trained by akhooli.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/gpt2_small_arabic_pipeline_ar_5.5.1_3.0_1734591332527.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/gpt2_small_arabic_pipeline_ar_5.5.1_3.0_1734591332527.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("gpt2_small_arabic_pipeline", lang = "ar")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("gpt2_small_arabic_pipeline", lang = "ar")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|gpt2_small_arabic_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|ar|
|Size:|299.0 MB|

## References

https://huggingface.co/akhooli/gpt2-small-arabic

## Included Models

- DocumentAssembler
- GPT2Transformer