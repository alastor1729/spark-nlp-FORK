---
layout: model
title: English autonlp_predict_roi_1_29797730_pipeline pipeline RoBertaForSequenceClassification from ds198799
author: John Snow Labs
name: autonlp_predict_roi_1_29797730_pipeline
date: 2024-09-10
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

Pretrained RoBertaForSequenceClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`autonlp_predict_roi_1_29797730_pipeline` is a English model originally trained by ds198799.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/autonlp_predict_roi_1_29797730_pipeline_en_5.5.0_3.0_1725965883641.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/autonlp_predict_roi_1_29797730_pipeline_en_5.5.0_3.0_1725965883641.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("autonlp_predict_roi_1_29797730_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("autonlp_predict_roi_1_29797730_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|autonlp_predict_roi_1_29797730_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|424.2 MB|

## References

https://huggingface.co/ds198799/autonlp-predict_ROI_1-29797730

## Included Models

- DocumentAssembler
- TokenizerModel
- RoBertaForSequenceClassification