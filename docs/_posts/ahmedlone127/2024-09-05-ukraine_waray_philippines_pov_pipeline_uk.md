---
layout: model
title: Ukrainian ukraine_waray_philippines_pov_pipeline pipeline XlmRoBertaForSequenceClassification from YaraKyrychenko
author: John Snow Labs
name: ukraine_waray_philippines_pov_pipeline
date: 2024-09-05
tags: [uk, open_source, pipeline, onnx]
task: Text Classification
language: uk
edition: Spark NLP 5.5.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained XlmRoBertaForSequenceClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`ukraine_waray_philippines_pov_pipeline` is a Ukrainian model originally trained by YaraKyrychenko.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/ukraine_waray_philippines_pov_pipeline_uk_5.5.0_3.0_1725513879534.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/ukraine_waray_philippines_pov_pipeline_uk_5.5.0_3.0_1725513879534.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("ukraine_waray_philippines_pov_pipeline", lang = "uk")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("ukraine_waray_philippines_pov_pipeline", lang = "uk")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ukraine_waray_philippines_pov_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|uk|
|Size:|877.0 MB|

## References

https://huggingface.co/YaraKyrychenko/ukraine-war-pov

## Included Models

- DocumentAssembler
- TokenizerModel
- XlmRoBertaForSequenceClassification