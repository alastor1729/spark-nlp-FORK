---
layout: model
title: Kannada XlmRobertaForSequenceClassification Cased model (from Hate-speech-CNERG)
author: John Snow Labs
name: xlmroberta_classifier_deoffxlmr_mono_kannada
date: 2024-09-01
tags: [kn, open_source, xlm_roberta, sequence_classification, classification, onnx]
task: Text Classification
language: kn
edition: Spark NLP 5.4.2
spark_version: 3.0
supported: true
engine: onnx
annotator: XlmRoBertaForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained XlmRobertaForSequenceClassification model, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP. `deoffxlmr-mono-kannada` is a Kannada model originally trained by `Hate-speech-CNERG`.

## Predicted Entities

`Not_offensive`, `Off_target_other`, `Off_target_group`, `Profanity`, `Off_target_ind`, `Not_in_intended_language`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/xlmroberta_classifier_deoffxlmr_mono_kannada_kn_5.4.2_3.0_1725170193518.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/xlmroberta_classifier_deoffxlmr_mono_kannada_kn_5.4.2_3.0_1725170193518.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = Tokenizer() \
    .setInputCols("document") \
    .setOutputCol("token")

seq_classifier = XlmRoBertaForSequenceClassification.pretrained("xlmroberta_classifier_deoffxlmr_mono_kannada","kn") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("class")

pipeline = Pipeline(stages=[documentAssembler, tokenizer, seq_classifier])

data = spark.createDataFrame([["PUT YOUR STRING HERE"]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
      .setInputCols(Array("text"))
      .setOutputCols(Array("document"))

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val seq_classifier = XlmRoBertaForSequenceClassification.pretrained("xlmroberta_classifier_deoffxlmr_mono_kannada","kn")
    .setInputCols(Array("document", "token"))
    .setOutputCol("class")

val pipeline = new Pipeline().setStages(Array(documentAssembler, tokenizer, seq_classifier))

val data = Seq("PUT YOUR STRING HERE").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```

{:.nlu-block}
```python
import nlu
nlu.load("kn.classify.xlmr_roberta").predict("""PUT YOUR STRING HERE""")
```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|xlmroberta_classifier_deoffxlmr_mono_kannada|
|Compatibility:|Spark NLP 5.4.2+|
|License:|Open Source|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[class]|
|Language:|kn|
|Size:|1.0 GB|

## References

References

- https://huggingface.co/Hate-speech-CNERG/deoffxlmr-mono-kannada
- https://www.aclweb.org/anthology/2021.dravidianlangtech-1.38/