---
layout: model
title: Multilingual BertForQuestionAnswering Base Uncased model (from roshnir)
author: John Snow Labs
name: bert_qa_base_multi_uncased
date: 2023-11-12
tags: [xx, open_source, bert, question_answering, onnx]
task: Question Answering
language: xx
edition: Spark NLP 5.2.0
spark_version: 3.0
supported: true
engine: onnx
annotator: BertForQuestionAnswering
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained Question Answering model, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP. `bert-base-multi-uncased-en-hi` is a Multilingual model originally trained by `roshnir`.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_qa_base_multi_uncased_xx_5.2.0_3.0_1699790863248.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/bert_qa_base_multi_uncased_xx_5.2.0_3.0_1699790863248.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = MultiDocumentAssembler() \
    .setInputCols(["question", "context"]) \
    .setOutputCols(["document_question", "document_context"])

spanClassifier = BertForQuestionAnswering.pretrained("bert_qa_base_multi_uncased","xx") \
    .setInputCols(["document_question", "document_context"]) \
    .setOutputCol("answer")\
    .setCaseSensitive(True)
    
pipeline = Pipeline(stages=[documentAssembler, spanClassifier])

data = spark.createDataFrame([["PUT YOUR QUESTION HERE", "PUT YOUR CONTEXT HERE"]]).toDF("question", "context")

result = pipeline.fit(data).transform(data)
```
```scala
val documentAssembler = new MultiDocumentAssembler() 
      .setInputCols(Array("question", "context")) 
      .setOutputCols(Array("document_question", "document_context"))
 
val spanClassifer = BertForQuestionAnswering.pretrained("bert_qa_base_multi_uncased","xx") 
    .setInputCols(Array("document", "token")) 
    .setOutputCol("answer")
    .setCaseSensitive(true)

val pipeline = new Pipeline().setStages(Array(documentAssembler, spanClassifier))

val data = Seq("PUT YOUR QUESTION HERE", "PUT YOUR CONTEXT HERE").toDF("question", "context")

val result = pipeline.fit(data).transform(data)
```

{:.nlu-block}
```python
import nlu
nlu.load("xx.answer_question.bert.uncased_base").predict("""PUT YOUR QUESTION HERE|||"PUT YOUR CONTEXT HERE""")
```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_qa_base_multi_uncased|
|Compatibility:|Spark NLP 5.2.0+|
|License:|Open Source|
|Edition:|Official|
|Input Labels:|[document_question, document_context]|
|Output Labels:|[answer]|
|Language:|xx|
|Size:|625.5 MB|
|Case sensitive:|false|
|Max sentence length:|512|

## References

References

- https://huggingface.co/roshnir/bert-base-multi-uncased-en-hi