from types import SimpleNamespace

from app import ask


def test_ask_prints_input_and_output_token_counts(monkeypatch, capsys):
    response = SimpleNamespace(
        usage_metadata=SimpleNamespace(
            prompt_token_count=12,
            candidates_token_count=34,
        ),
        text="回答",
    )

    class FakeModels:
        def generate_content(self, *, model, contents):
            assert model == ask.MODEL
            assert contents == "質問"
            return response

    class FakeClient:
        models = FakeModels()

        def __init__(self, *, api_key):
            assert api_key == "test-key"

    monkeypatch.setattr(ask.genai, "Client", FakeClient)
    monkeypatch.setattr(ask, "get_api_key", lambda: "test-key")

    assert ask.ask("質問") == "回答"
    assert "[トークン] 入力: 12, 出力: 34" in capsys.readouterr().out


def test_ask_reports_missing_usage_metadata(monkeypatch, capsys):
    response = SimpleNamespace(usage_metadata=None, text="回答")

    class FakeModels:
        def generate_content(self, *, model, contents):
            assert model == ask.MODEL
            assert contents == "質問"
            return response

    class FakeClient:
        models = FakeModels()

        def __init__(self, *, api_key):
            assert api_key == "test-key"

    monkeypatch.setattr(ask.genai, "Client", FakeClient)
    monkeypatch.setattr(ask, "get_api_key", lambda: "test-key")

    assert ask.ask("質問") == "回答"
    assert "[トークン] 使用量情報を取得できませんでした" in capsys.readouterr().out
