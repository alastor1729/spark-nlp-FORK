#  Copyright 2017-2022 John Snow Labs
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import unittest

import pytest
import os

from sparknlp.annotator import *
from sparknlp.base import *
from test.util import SparkContextForTest


@pytest.mark.slow
class SnowFlakeEmbeddingsTestSpec(unittest.TestCase):
	def setUp(self):
		self.spark = SparkContextForTest.spark
		self.tested_annotator = SnowFlakeEmbeddings \
			.loadSavedModel("1",
							SparkContextForTest.spark) \
			.setInputCols(["documents"]) \
			.setOutputCol("embeddings") \
			.setPoolingStrategy("cls_avg")

	def test_run(self):
		data = SparkContextForTest.spark.read.option("header", "true") \
			.csv(path="file:///" + os.getcwd() + "/../src/test/resources/embeddings/sentence_embeddings.csv")

		document_assembler = DocumentAssembler() \
			.setInputCol("text") \
			.setOutputCol("documents")

		embeddings_finisher = EmbeddingsFinisher().setInputCols("embeddings").setOutputCols("embeddings")

		snowflake = self.tested_annotator

		pipeline = Pipeline().setStages([document_assembler, snowflake, embeddings_finisher])
		results = pipeline.fit(data).transform(data)

		results.selectExpr("explode(embeddings) as result").show(truncate=False)