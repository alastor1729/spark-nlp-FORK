---
layout: model
title: Turkish roberta_base_turkish_uncased_stance_pipeline pipeline RoBertaForSequenceClassification from byunal
author: John Snow Labs
name: roberta_base_turkish_uncased_stance_pipeline
date: 2024-09-22
tags: [tr, open_source, pipeline, onnx]
task: Text Classification
language: tr
edition: Spark NLP 5.5.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained RoBertaForSequenceClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`roberta_base_turkish_uncased_stance_pipeline` is a Turkish model originally trained by byunal.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/roberta_base_turkish_uncased_stance_pipeline_tr_5.5.0_3.0_1727017395547.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/roberta_base_turkish_uncased_stance_pipeline_tr_5.5.0_3.0_1727017395547.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("roberta_base_turkish_uncased_stance_pipeline", lang = "tr")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("roberta_base_turkish_uncased_stance_pipeline", lang = "tr")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|roberta_base_turkish_uncased_stance_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|tr|
|Size:|463.7 MB|

## References

https://huggingface.co/byunal/roberta-base-turkish-uncased-stance

## Included Models

- DocumentAssembler
- TokenizerModel
- RoBertaForSequenceClassification