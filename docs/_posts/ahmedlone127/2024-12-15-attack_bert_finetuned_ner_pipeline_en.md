---
layout: model
title: English attack_bert_finetuned_ner_pipeline pipeline MPNetForTokenClassification from zohreaz
author: John Snow Labs
name: attack_bert_finetuned_ner_pipeline
date: 2024-12-15
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

Pretrained MPNetForTokenClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`attack_bert_finetuned_ner_pipeline` is a English model originally trained by zohreaz.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/attack_bert_finetuned_ner_pipeline_en_5.5.1_3.0_1734290726087.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/attack_bert_finetuned_ner_pipeline_en_5.5.1_3.0_1734290726087.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("attack_bert_finetuned_ner_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("attack_bert_finetuned_ner_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|attack_bert_finetuned_ner_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|407.2 MB|

## References

https://huggingface.co/zohreaz/ATTACK-BERT-finetuned-ner

## Included Models

- DocumentAssembler
- TokenizerModel
- MPNetForTokenClassification