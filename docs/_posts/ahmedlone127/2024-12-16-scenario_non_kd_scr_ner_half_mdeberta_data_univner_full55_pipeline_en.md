---
layout: model
title: English scenario_non_kd_scr_ner_half_mdeberta_data_univner_full55_pipeline pipeline DeBertaForTokenClassification from haryoaw
author: John Snow Labs
name: scenario_non_kd_scr_ner_half_mdeberta_data_univner_full55_pipeline
date: 2024-12-16
tags: [en, open_source, pipeline, onnx]
task: Named Entity Recognition
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

Pretrained DeBertaForTokenClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`scenario_non_kd_scr_ner_half_mdeberta_data_univner_full55_pipeline` is a English model originally trained by haryoaw.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/scenario_non_kd_scr_ner_half_mdeberta_data_univner_full55_pipeline_en_5.5.1_3.0_1734346971823.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/scenario_non_kd_scr_ner_half_mdeberta_data_univner_full55_pipeline_en_5.5.1_3.0_1734346971823.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("scenario_non_kd_scr_ner_half_mdeberta_data_univner_full55_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("scenario_non_kd_scr_ner_half_mdeberta_data_univner_full55_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|scenario_non_kd_scr_ner_half_mdeberta_data_univner_full55_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|403.5 MB|

## References

https://huggingface.co/haryoaw/scenario-non-kd-scr-ner-half-mdeberta_data-univner_full55

## Included Models

- DocumentAssembler
- TokenizerModel
- DeBertaForTokenClassification