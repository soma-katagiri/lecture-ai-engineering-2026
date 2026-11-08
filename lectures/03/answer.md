# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：
第３回の回答　モデル：gemini-3.5-flash-lite
AIE2026の講座における「3レベル」とは、宿題の難易度や取り組み方の構成を指しています。

宿題は以下の3段階（レベル）に分かれており、ご自身の学習状況に合わせて**どれか1つ**に取り組めば、その回の宿題は完了となります。

1. **基礎**：講義内容の確認を中心とした問題
2. **実装**：自分で実際にコードを書く問題
3. **発展**：より踏み込んだ調査や新しい試みを行う課題

原則として、宿題の採点などは行われませんので、ご自身のペースや目的に合ったレベルを選んで取り組んでみてください。

関連する回：第1回

第一回の回答では、一般的な内容が書かれており正しい意味とは異なってはいたが、今回のエージェントの回答は、実際の用語の定義と合っていた。また関連する回についても記述があった。

- `--trace` で見えたツール呼び出し（ツール名と引数）：
[tool call]   search_glossary({'query': 'LoRA'})
[tool call]   search_glossary({'query': 'QLoRA'})

search_glossaryというツールを呼び出し、LoRA, QLoRAの二つの引数を用いていた

- 1つの質問での LLM 呼び出し回数（`requests`）：
[usage] RunUsage(cost=Decimal('0.0008469'), details={'text_prompt_tokens': 1198}, input_text_tokens=1198, input_tokens=1198, output_tokens=195, requests=2, tool_calls=2)

呼び出回数は「2」回であった

- 追加したツールと、docstring に書いた説明：
追加したツール：make_quiz

docstringの内容
”””
指定した回の用語から1つを選び、確認問題と答えを返す。
    
「第2回の確認問題を出して」のように、復習用の問題を求められたときに使う。
”””

## 宿題

- 取り組んだレベル：基礎
- やったこと：INSTRUCTIONSを変更しツールの呼ばれ方や回答がどう変わるか確認した。質問とモデルは以下のもので統一する。gemini-3.5-flash-lite, "LoRA とQLoRAの違いは？"
- 結果：
変更前：
INSTRUCTIONS = """\
あなたはAIエンジニアリング講座（AIE2026）の学習支援エージェントです。
- 用語や講座に固有のことを答える前に、必ず search_glossary で用語集を確認する。
- 回の内容を聞かれたら get_lecture_summary を使う。
- 用語集に見つからないことは、推測で断定せず「用語集にはない」と伝える。
- 回答の最後に、関係する回（第N回）を示す。
- 宿題の答えそのものは書かず、考え方のヒントで導く。
"""
]search_glossary:
"""講座の用語集から用語を検索し、定義と、どの回で扱うかを返す。

AIエンジニアリングの用語や、この講座（AIE2026）に固有の言葉について
答える前に使うこと。query には調べたい用語を1つだけ入れる（例: "LoRA"）。
"""

回答：
LoRAとQLoRAの違いは、ベースモデルの重みの扱い方（量子化）にあります。

* **LoRA**: 事前学習済みの重みは固定したまま、更新分を表す小さな低ランク行列（アダプタ）だけを学習するPEFT（Parameter-Efficient Fine-Tuning）手法です。学習パラメータを大幅に削減できます。
* **QLoRA**: ベースモデルの重みを4ビットなどに量子化（Quantization）してメモリをさらに節約したうえで、LoRAによるファインチューニングを行う手法です。これにより、より大きなモデルを比較的小さなGPUメモリでも扱えるようになります。

関係する回：第2回

--- trace ---
[tool call]   search_glossary({'query': 'LoRA'})
[tool call]   search_glossary({'query': 'QLoRA'})
[tool return] search_glossary -> [{"term": "LoRA", "lecture": 2, "definition": "事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク行列）で表し、その小さな行列だけを学習するPEFT手法。学習するパラ…
[tool return] search_glossary -> [{"term": "QLoRA", "lecture": 2, "definition": "ベースモデルの重みを4ビットなどに量子化してメモリを節約したうえで、LoRAで学習する手法。より大きなモデルを小さなGPUで扱える。本講座の第2…
[usage] RunUsage(cost=Decimal('0.0008663'), details={'text_prompt_tokens': 1346}, input_text_tokens=1346, input_tokens=1346, output_tokens=185, requests=2, tool_calls=2)

1.INSTRUCTIONS変更：
INSTRUCTIONS = """\
あなたはAIエンジニアリング講座（AIE2026）の学習支援エージェントです。
- 用語や講座に固有のことを答える前に、必ず search_glossary で用語集を確認する。
- 回の内容を聞かれたら get_lecture_summary を使う。
- 用語集に見つからないことは、推測で断定せず「用語集にはない」と伝える。
- 回答の最後に、関係する回（第N回）を示す。
- 加えて必ず関係する回から make_quiz を用いて一問問題を出す。
- 宿題の答えそのものは書かず、考え方のヒントで導く。
"""

- 加えて必ず関係する回から make_quiz を用いて一問問題を出す。
を追加した。

回答：
LoRAとQLoRAの違いは、ベースモデルの重みの持ち方（量子化）にあります。

- **LoRA**
  事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク行列）で表し、その小さな行列だけを学習するPEFT手法です。学習するパラメータが少なく、学習結果も小さなファイルで保存できます。

- **QLoRA**
  ベースモデルの重みを4ビットなどに量子化してメモリを大きく節約したうえで、LoRAによる学習を行う手法です。これにより、さらに大きなモデルをより小さなGPUメモリで扱えるようになります。

---

**【関係する回】**
第2回

**【確認問題】**
Q. 「学習率」の意味は？
（※答えは考えてみましょう）

--- trace ---
[tool call]   search_glossary({'query': 'LoRA'})
[tool call]   search_glossary({'query': 'QLoRA'})
[tool return] search_glossary -> [{"term": "LoRA", "lecture": 2, "definition": "事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク行列）で表し、その小さな行列だけを学習するPEFT手法。学習するパラ…
[tool return] search_glossary -> [{"term": "QLoRA", "lecture": 2, "definition": "ベースモデルの重みを4ビットなどに量子化してメモリを節約したうえで、LoRAで学習する手法。より大きなモデルを小さなGPUで扱える。本講座の第2…
[tool call]   make_quiz({'lecture': 2})
[tool return] make_quiz -> {"question": "「学習率」の意味は？", "answer": "1回の更新でパラメータをどれだけ動かすかを決めるハイパーパラメータ。大きすぎると学習が不安定になり、小さすぎると進みが遅い。"}…
[usage] RunUsage(cost=Decimal('0.0013139'), details={'text_prompt_tokens': 2438}, input_text_tokens=2438, input_tokens=2438, output_tokens=233, requests=3, tool_calls=3)

- 気づき・疑問：
回答を比較すると、変更後はINSTRUCTIONSに追加した内容からmake_quizを用いて関連した回による
問題が一問を出すようになった。toolとして加えてmake_quizを用いるようになった。
