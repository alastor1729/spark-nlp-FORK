---
layout: model
title: Italian t5_it5_efficient_small_el32_formal_tonga_tonga_islands_informal_pipeline pipeline T5Transformer from it5
author: John Snow Labs
name: t5_it5_efficient_small_el32_formal_tonga_tonga_islands_informal_pipeline
date: 2024-08-05
tags: [it, open_source, pipeline, onnx]
task: [Question Answering, Summarization, Translation, Text Generation]
language: it
edition: Spark NLP 5.4.2
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained T5Transformer, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`t5_it5_efficient_small_el32_formal_tonga_tonga_islands_informal_pipeline` is a Italian model originally trained by it5.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/t5_it5_efficient_small_el32_formal_tonga_tonga_islands_informal_pipeline_it_5.4.2_3.0_1722896397026.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/t5_it5_efficient_small_el32_formal_tonga_tonga_islands_informal_pipeline_it_5.4.2_3.0_1722896397026.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("t5_it5_efficient_small_el32_formal_tonga_tonga_islands_informal_pipeline", lang = "it")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("t5_it5_efficient_small_el32_formal_tonga_tonga_islands_informal_pipeline", lang = "it")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|t5_it5_efficient_small_el32_formal_tonga_tonga_islands_informal_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.4.2+|
|License:|Open Source|
|Edition:|Official|
|Language:|it|
|Size:|654.4 MB|

## References

https://huggingface.co/it5/it5-efficient-small-el32-formal-to-informal

## Included Models

- DocumentAssembler
- T5Transformer