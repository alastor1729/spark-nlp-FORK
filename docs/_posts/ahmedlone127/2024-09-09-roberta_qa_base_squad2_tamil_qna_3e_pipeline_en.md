---
layout: model
title: English roberta_qa_base_squad2_tamil_qna_3e_pipeline pipeline RoBertaForQuestionAnswering from venkateshdas
author: John Snow Labs
name: roberta_qa_base_squad2_tamil_qna_3e_pipeline
date: 2024-09-09
tags: [en, open_source, pipeline, onnx]
task: Question Answering
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

Pretrained RoBertaForQuestionAnswering, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`roberta_qa_base_squad2_tamil_qna_3e_pipeline` is a English model originally trained by venkateshdas.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/roberta_qa_base_squad2_tamil_qna_3e_pipeline_en_5.5.0_3.0_1725866921059.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/roberta_qa_base_squad2_tamil_qna_3e_pipeline_en_5.5.0_3.0_1725866921059.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("roberta_qa_base_squad2_tamil_qna_3e_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("roberta_qa_base_squad2_tamil_qna_3e_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|roberta_qa_base_squad2_tamil_qna_3e_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|463.6 MB|

## References

https://huggingface.co/venkateshdas/roberta-base-squad2-ta-qna-roberta3e

## Included Models

- MultiDocumentAssembler
- RoBertaForQuestionAnswering