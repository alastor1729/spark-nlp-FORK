---
layout: model
title: English clasificador_muchocine_modeloalbert_pipeline pipeline AlbertForSequenceClassification from martagrueso
author: John Snow Labs
name: clasificador_muchocine_modeloalbert_pipeline
date: 2024-09-05
tags: [en, open_source, pipeline, onnx]
task: Text Classification
language: en
edition: Spark NLP 5.5.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained AlbertForSequenceClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`clasificador_muchocine_modeloalbert_pipeline` is a English model originally trained by martagrueso.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/clasificador_muchocine_modeloalbert_pipeline_en_5.5.0_3.0_1725543225526.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/clasificador_muchocine_modeloalbert_pipeline_en_5.5.0_3.0_1725543225526.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("clasificador_muchocine_modeloalbert_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("clasificador_muchocine_modeloalbert_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clasificador_muchocine_modeloalbert_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|44.7 MB|

## References

https://huggingface.co/martagrueso/clasificador-muchocine-modeloalbert

## Included Models

- DocumentAssembler
- TokenizerModel
- AlbertForSequenceClassification