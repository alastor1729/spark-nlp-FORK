---
layout: model
title: English text_subject_classification_deberta_v3_base_single_label_textbooks_zg_pipeline pipeline DeBertaForSequenceClassification from acuvity
author: John Snow Labs
name: text_subject_classification_deberta_v3_base_single_label_textbooks_zg_pipeline
date: 2024-08-31
tags: [en, open_source, pipeline, onnx]
task: Text Classification
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

Pretrained DeBertaForSequenceClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`text_subject_classification_deberta_v3_base_single_label_textbooks_zg_pipeline` is a English model originally trained by acuvity.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/text_subject_classification_deberta_v3_base_single_label_textbooks_zg_pipeline_en_5.4.2_3.0_1725133738360.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/text_subject_classification_deberta_v3_base_single_label_textbooks_zg_pipeline_en_5.4.2_3.0_1725133738360.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("text_subject_classification_deberta_v3_base_single_label_textbooks_zg_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("text_subject_classification_deberta_v3_base_single_label_textbooks_zg_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|text_subject_classification_deberta_v3_base_single_label_textbooks_zg_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.4.2+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|628.4 MB|

## References

https://huggingface.co/acuvity/text-subject_classification-deberta-v3-base-single-label-textbooks-zg

## Included Models

- DocumentAssembler
- TokenizerModel
- DeBertaForSequenceClassification