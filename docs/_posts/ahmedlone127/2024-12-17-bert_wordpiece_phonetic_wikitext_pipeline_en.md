---
layout: model
title: English bert_wordpiece_phonetic_wikitext_pipeline pipeline BertEmbeddings from psktoure
author: John Snow Labs
name: bert_wordpiece_phonetic_wikitext_pipeline
date: 2024-12-17
tags: [en, open_source, pipeline, onnx]
task: Embeddings
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

Pretrained BertEmbeddings, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`bert_wordpiece_phonetic_wikitext_pipeline` is a English model originally trained by psktoure.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_wordpiece_phonetic_wikitext_pipeline_en_5.5.1_3.0_1734416413759.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/bert_wordpiece_phonetic_wikitext_pipeline_en_5.5.1_3.0_1734416413759.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("bert_wordpiece_phonetic_wikitext_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("bert_wordpiece_phonetic_wikitext_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_wordpiece_phonetic_wikitext_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|408.3 MB|

## References

https://huggingface.co/psktoure/BERT_WordPiece_phonetic_wikitext

## Included Models

- DocumentAssembler
- TokenizerModel
- BertEmbeddings