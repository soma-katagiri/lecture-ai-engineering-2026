# 第2回 解答

## 演習

- 使ったモデル・設定（`result.json` の `config` から）：
"config": {
    "base_model": "Qwen/Qwen3.5-0.8B",
    "revision": "2fc06364715b967f1860aea9cf38778875588b17",
    "seed": 42,
    "num_train_epochs": 20,
    "warmup_steps": 6,
    "lr": 0.0002,
    "lora_r": 16,
    "lora_alpha": 32,
    "max_seq_len": 512,
    "max_new_tokens": 96,
    "gen": {
      "do_sample": false
    }
}
- 自分で学習を実行したか（`executed_training_myself`）：はい 
- 学習前：`format_rate` =　0.095238 / `content_rate` =　0.000000	
- 学習後：`format_rate` =　1.000000	 / `content_rate` =　0.952381
- 退行した質問： []
- 学習後に残った失敗と、その型（根拠なしの質問に断定した / 根拠ありの質問に確認要求で逃げた / 形式の崩れ）：
    20のオフィスアワーに事前予約が必要ですか、という質問に対して失敗が残っていた。
    型は "根拠なしの質問に断定した"
- 知識を問う質問（セクション 6）の結果（学習前の分類 → 学習後の分類）と気づいたこと：
    学習前では全てfomat_errorだったのが、assertedが2つとneeds_reviewの2つに変化した。
    これより、学習後は正解も出すようになったが、嘘もつくようになった。

- 学習で変わったこと・変わらなかったこと：
    変わったことは、まず正答率が上がったこと、回答の文が長く詳細になった。
    内容正答率については、一気に上がり、0%だったのが95%までになった。
    またsecondsについて3秒と数秒であるが学習後の方が長くなった。
    変わらなかったことについてはほとんど無い

## 宿題

- 取り組んだレベル：基礎
- 変えた設定やデータ：
    num_train_epochsを20から40へ変更した。以下にconfigの内容を記載する
"config": {
    "base_model": "Qwen/Qwen3.5-0.8B",
    "revision": "2fc06364715b967f1860aea9cf38778875588b17",
    "seed": 42,
    "num_train_epochs": 40,
    "warmup_steps": 6,
    "lr": 0.0002,
    "lora_r": 16,
    "lora_alpha": 32,
    "max_seq_len": 512,
    "max_new_tokens": 96,
    "gen": {
      "do_sample": false
    }
  }

- 結果（比較表や数字）：
| num_train_epochs | format_rate | content_rate | 最終loss | 学習時間(sec) |
| 20 | 1.000000 | 0.952381 | 0.011015 | 453 |
| 40 | 1.000000 | 0.857143 | 0.011049 | 483 |


