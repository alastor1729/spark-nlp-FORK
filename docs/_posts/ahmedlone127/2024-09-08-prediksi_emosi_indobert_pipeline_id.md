---
layout: model
title: Indonesian prediksi_emosi_indobert_pipeline pipeline BertForSequenceClassification from azizp128
author: John Snow Labs
name: prediksi_emosi_indobert_pipeline
date: 2024-09-08
tags: [id, open_source, pipeline, onnx]
task: Text Classification
language: id
edition: Spark NLP 5.5.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained BertForSequenceClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`prediksi_emosi_indobert_pipeline` is a Indonesian model originally trained by azizp128.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/prediksi_emosi_indobert_pipeline_id_5.5.0_3.0_1725825888549.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/prediksi_emosi_indobert_pipeline_id_5.5.0_3.0_1725825888549.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("prediksi_emosi_indobert_pipeline", lang = "id")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("prediksi_emosi_indobert_pipeline", lang = "id")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|prediksi_emosi_indobert_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|id|
|Size:|466.4 MB|

## References

https://huggingface.co/azizp128/prediksi-emosi-indobert

## Included Models

- DocumentAssembler
- TokenizerModel
- BertForSequenceClassification