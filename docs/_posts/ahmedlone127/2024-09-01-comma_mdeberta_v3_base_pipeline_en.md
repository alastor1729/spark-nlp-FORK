---
layout: model
title: English comma_mdeberta_v3_base_pipeline pipeline DeBertaForTokenClassification from aseifert
author: John Snow Labs
name: comma_mdeberta_v3_base_pipeline
date: 2024-09-01
tags: [en, open_source, pipeline, onnx]
task: Named Entity Recognition
language: en
edition: Spark NLP 5.4.2
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained DeBertaForTokenClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`comma_mdeberta_v3_base_pipeline` is a English model originally trained by aseifert.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/comma_mdeberta_v3_base_pipeline_en_5.4.2_3.0_1725197881048.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/comma_mdeberta_v3_base_pipeline_en_5.4.2_3.0_1725197881048.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("comma_mdeberta_v3_base_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("comma_mdeberta_v3_base_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|comma_mdeberta_v3_base_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.4.2+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|811.6 MB|

## References

https://huggingface.co/aseifert/comma-mdeberta-v3-base

## Included Models

- DocumentAssembler
- TokenizerModel
- DeBertaForTokenClassification