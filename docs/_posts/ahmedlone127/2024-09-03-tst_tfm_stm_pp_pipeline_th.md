---
layout: model
title: Thai tst_tfm_stm_pp_pipeline pipeline CamemBertForSequenceClassification from Ppxndpxdd
author: John Snow Labs
name: tst_tfm_stm_pp_pipeline
date: 2024-09-03
tags: [th, open_source, pipeline, onnx]
task: Text Classification
language: th
edition: Spark NLP 5.5.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained CamemBertForSequenceClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`tst_tfm_stm_pp_pipeline` is a Thai model originally trained by Ppxndpxdd.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/tst_tfm_stm_pp_pipeline_th_5.5.0_3.0_1725325286508.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/tst_tfm_stm_pp_pipeline_th_5.5.0_3.0_1725325286508.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("tst_tfm_stm_pp_pipeline", lang = "th")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("tst_tfm_stm_pp_pipeline", lang = "th")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|tst_tfm_stm_pp_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|th|
|Size:|394.4 MB|

## References

https://huggingface.co/Ppxndpxdd/tst_tfm_stm_pp

## Included Models

- DocumentAssembler
- TokenizerModel
- CamemBertForSequenceClassification