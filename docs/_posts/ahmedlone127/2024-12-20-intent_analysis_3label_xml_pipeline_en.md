---
layout: model
title: English intent_analysis_3label_xml_pipeline pipeline XlmRoBertaForSequenceClassification from adriansanz
author: John Snow Labs
name: intent_analysis_3label_xml_pipeline
date: 2024-12-20
tags: [en, open_source, pipeline, onnx]
task: Text Classification
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

Pretrained XlmRoBertaForSequenceClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`intent_analysis_3label_xml_pipeline` is a English model originally trained by adriansanz.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/intent_analysis_3label_xml_pipeline_en_5.5.1_3.0_1734687384286.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/intent_analysis_3label_xml_pipeline_en_5.5.1_3.0_1734687384286.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("intent_analysis_3label_xml_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("intent_analysis_3label_xml_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|intent_analysis_3label_xml_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|796.3 MB|

## References

https://huggingface.co/adriansanz/intent_analysis-3label-xml

## Included Models

- DocumentAssembler
- TokenizerModel
- XlmRoBertaForSequenceClassification