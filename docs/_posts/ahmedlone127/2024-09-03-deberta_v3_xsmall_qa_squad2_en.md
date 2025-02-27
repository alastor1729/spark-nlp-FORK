---
layout: model
title: English DebertaForQuestionAnswering model (from nbroad)
author: John Snow Labs
name: deberta_v3_xsmall_qa_squad2
date: 2024-09-03
tags: [open_source, deberta, question_answering, en, openvino]
task: Question Answering
language: en
edition: Spark NLP 5.4.2
spark_version: 3.0
supported: true
engine: openvino
annotator: CamemBertForTokenClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained Question Answering model, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP. `deberta-v3-xsmall-squad2` is a English model originally trained by `nbroad`.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/deberta_v3_xsmall_qa_squad2_en_5.4.2_3.0_1725401584818.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/deberta_v3_xsmall_qa_squad2_en_5.4.2_3.0_1725401584818.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = MultiDocumentAssembler() \
.setInputCols(["question", "context"]) \
.setOutputCols(["document_question", "document_context"])

spanClassifier = DebertaForQuestionAnswering.pretrained("deberta_v3_xsmall_qa_squad2","en") \
.setInputCols(["document_question", "document_context"]) \
.setOutputCol("answer")\
.setCaseSensitive(True)

pipeline = Pipeline(stages=[documentAssembler, spanClassifier])

data = spark.createDataFrame([["What is my name?", "My name is Clara and I live in Berkeley."]]).toDF("question", "context")

result = pipeline.fit(data).transform(data)
```
```scala
val documentAssembler = new MultiDocumentAssembler() 
.setInputCols(Array("question", "context")) 
.setOutputCols(Array("document_question", "document_context"))

val spanClassifer = DebertaForQuestionAnswering.pretrained("deberta_v3_xsmall_qa_squad2","en") 
.setInputCols(Array("document", "token")) 
.setOutputCol("answer")
.setCaseSensitive(true)

val pipeline = new Pipeline().setStages(Array(documentAssembler, spanClassifier))

val data = Seq("What is my name?", "My name is Clara and I live in Berkeley.").toDF("question", "context")

val result = pipeline.fit(data).transform(data)
```

{:.nlu-block}
```python
import nlu
nlu.load("en.answer_question.squadv2.deberta").predict("""What is my name?|||"My name is Clara and I live in Berkeley.""")
```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|deberta_v3_xsmall_qa_squad2|
|Compatibility:|Spark NLP 5.4.2+|
|License:|Open Source|
|Edition:|Official|
|Input Labels:|[token, document]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|411.6 MB|
|Case sensitive:|true|
|Max sentence length:|512|

## References

References

https://huggingface.co/nbroad/deberta-v3-xsmall-squad2