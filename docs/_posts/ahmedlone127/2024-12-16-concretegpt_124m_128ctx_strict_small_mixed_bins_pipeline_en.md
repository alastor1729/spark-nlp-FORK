---
layout: model
title: English concretegpt_124m_128ctx_strict_small_mixed_bins_pipeline pipeline GPT2Transformer from colinglab
author: John Snow Labs
name: concretegpt_124m_128ctx_strict_small_mixed_bins_pipeline
date: 2024-12-16
tags: [en, open_source, pipeline, onnx]
task: [Question Answering, Summarization, Translation, Text Generation]
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

Pretrained GPT2Transformer, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`concretegpt_124m_128ctx_strict_small_mixed_bins_pipeline` is a English model originally trained by colinglab.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/concretegpt_124m_128ctx_strict_small_mixed_bins_pipeline_en_5.5.1_3.0_1734388709573.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/concretegpt_124m_128ctx_strict_small_mixed_bins_pipeline_en_5.5.1_3.0_1734388709573.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("concretegpt_124m_128ctx_strict_small_mixed_bins_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("concretegpt_124m_128ctx_strict_small_mixed_bins_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|concretegpt_124m_128ctx_strict_small_mixed_bins_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|609.8 MB|

## References

https://huggingface.co/colinglab/ConcreteGPT-124M-128ctx-Strict-Small-mixed_bins

## Included Models

- DocumentAssembler
- GPT2Transformer