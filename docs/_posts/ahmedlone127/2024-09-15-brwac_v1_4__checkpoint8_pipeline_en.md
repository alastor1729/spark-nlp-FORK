---
layout: model
title: English brwac_v1_4__checkpoint8_pipeline pipeline RoBertaEmbeddings from eduagarcia-temp
author: John Snow Labs
name: brwac_v1_4__checkpoint8_pipeline
date: 2024-09-15
tags: [en, open_source, pipeline, onnx]
task: Embeddings
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

Pretrained RoBertaEmbeddings, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`brwac_v1_4__checkpoint8_pipeline` is a English model originally trained by eduagarcia-temp.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/brwac_v1_4__checkpoint8_pipeline_en_5.5.0_3.0_1726413849570.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/brwac_v1_4__checkpoint8_pipeline_en_5.5.0_3.0_1726413849570.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("brwac_v1_4__checkpoint8_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("brwac_v1_4__checkpoint8_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|brwac_v1_4__checkpoint8_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|297.8 MB|

## References

https://huggingface.co/eduagarcia-temp/brwac_v1_4__checkpoint8

## Included Models

- DocumentAssembler
- TokenizerModel
- RoBertaEmbeddings