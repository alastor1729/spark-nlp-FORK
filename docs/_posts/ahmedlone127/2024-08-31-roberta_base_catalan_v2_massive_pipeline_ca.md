---
layout: model
title: Catalan, Valencian roberta_base_catalan_v2_massive_pipeline pipeline RoBertaForSequenceClassification from projecte-aina
author: John Snow Labs
name: roberta_base_catalan_v2_massive_pipeline
date: 2024-08-31
tags: [ca, open_source, pipeline, onnx]
task: Text Classification
language: ca
edition: Spark NLP 5.4.2
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained RoBertaForSequenceClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`roberta_base_catalan_v2_massive_pipeline` is a Catalan, Valencian model originally trained by projecte-aina.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/roberta_base_catalan_v2_massive_pipeline_ca_5.4.2_3.0_1725122884833.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/roberta_base_catalan_v2_massive_pipeline_ca_5.4.2_3.0_1725122884833.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("roberta_base_catalan_v2_massive_pipeline", lang = "ca")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("roberta_base_catalan_v2_massive_pipeline", lang = "ca")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|roberta_base_catalan_v2_massive_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.4.2+|
|License:|Open Source|
|Edition:|Official|
|Language:|ca|
|Size:|421.7 MB|

## References

https://huggingface.co/projecte-aina/roberta-base-ca-v2-massive

## Included Models

- DocumentAssembler
- TokenizerModel
- RoBertaForSequenceClassification