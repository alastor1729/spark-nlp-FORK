---
layout: model
title: English jdrt_byclass_rinnna_hubert_asr_2_pipeline pipeline HubertForCTC from mskhattori
author: John Snow Labs
name: jdrt_byclass_rinnna_hubert_asr_2_pipeline
date: 2024-12-16
tags: [en, open_source, pipeline, onnx]
task: Automatic Speech Recognition
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

Pretrained HubertForCTC, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`jdrt_byclass_rinnna_hubert_asr_2_pipeline` is a English model originally trained by mskhattori.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/jdrt_byclass_rinnna_hubert_asr_2_pipeline_en_5.5.1_3.0_1734381101995.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/jdrt_byclass_rinnna_hubert_asr_2_pipeline_en_5.5.1_3.0_1734381101995.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("jdrt_byclass_rinnna_hubert_asr_2_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("jdrt_byclass_rinnna_hubert_asr_2_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jdrt_byclass_rinnna_hubert_asr_2_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|708.9 MB|

## References

https://huggingface.co/mskhattori/jdrt_byclass_rinnna_hubert_asr_2

## Included Models

- AudioAssembler
- HubertForCTC