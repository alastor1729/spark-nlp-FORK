---
layout: model
title: Dutch, Flemish robbert_dutch_cola_hylkebr_pipeline pipeline RoBertaForSequenceClassification from HylkeBr
author: John Snow Labs
name: robbert_dutch_cola_hylkebr_pipeline
date: 2024-09-09
tags: [nl, open_source, pipeline, onnx]
task: Text Classification
language: nl
edition: Spark NLP 5.5.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained RoBertaForSequenceClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`robbert_dutch_cola_hylkebr_pipeline` is a Dutch, Flemish model originally trained by HylkeBr.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/robbert_dutch_cola_hylkebr_pipeline_nl_5.5.0_3.0_1725911554756.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/robbert_dutch_cola_hylkebr_pipeline_nl_5.5.0_3.0_1725911554756.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("robbert_dutch_cola_hylkebr_pipeline", lang = "nl")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("robbert_dutch_cola_hylkebr_pipeline", lang = "nl")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|robbert_dutch_cola_hylkebr_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|nl|
|Size:|438.0 MB|

## References

https://huggingface.co/HylkeBr/robbert_dutch-cola

## Included Models

- DocumentAssembler
- TokenizerModel
- RoBertaForSequenceClassification