---
layout: model
title: English e5_base_unsupervised_pseudo_gpl_fiqa_131a12_pipeline pipeline E5Embeddings from rithwik-db
author: John Snow Labs
name: e5_base_unsupervised_pseudo_gpl_fiqa_131a12_pipeline
date: 2024-12-17
tags: [en, open_source, pipeline, onnx]
task: Embeddings
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

Pretrained E5Embeddings, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`e5_base_unsupervised_pseudo_gpl_fiqa_131a12_pipeline` is a English model originally trained by rithwik-db.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/e5_base_unsupervised_pseudo_gpl_fiqa_131a12_pipeline_en_5.5.1_3.0_1734396871491.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/e5_base_unsupervised_pseudo_gpl_fiqa_131a12_pipeline_en_5.5.1_3.0_1734396871491.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("e5_base_unsupervised_pseudo_gpl_fiqa_131a12_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("e5_base_unsupervised_pseudo_gpl_fiqa_131a12_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|e5_base_unsupervised_pseudo_gpl_fiqa_131a12_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|402.7 MB|

## References

https://huggingface.co/rithwik-db/e5-base-unsupervised-pseudo-gpl-fiqa-131a12

## Included Models

- DocumentAssembler
- E5Embeddings