---
layout: model
title: English english_tonga_tonga_islands_dzo_helsinki_nlp_m2_norphel_pipeline pipeline MarianTransformer from Norphel
author: John Snow Labs
name: english_tonga_tonga_islands_dzo_helsinki_nlp_m2_norphel_pipeline
date: 2024-12-19
tags: [en, open_source, pipeline, onnx]
task: Translation
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

Pretrained MarianTransformer, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`english_tonga_tonga_islands_dzo_helsinki_nlp_m2_norphel_pipeline` is a English model originally trained by Norphel.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/english_tonga_tonga_islands_dzo_helsinki_nlp_m2_norphel_pipeline_en_5.5.1_3.0_1734588317620.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/english_tonga_tonga_islands_dzo_helsinki_nlp_m2_norphel_pipeline_en_5.5.1_3.0_1734588317620.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("english_tonga_tonga_islands_dzo_helsinki_nlp_m2_norphel_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("english_tonga_tonga_islands_dzo_helsinki_nlp_m2_norphel_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|english_tonga_tonga_islands_dzo_helsinki_nlp_m2_norphel_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|1.2 GB|

## References

https://huggingface.co/Norphel/en_to_dzo_helsinki_nlp_m2

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- MarianTransformer