from alethes.generator.modeling import AlethesGenerator, GenerationConfig

def test_generator_smoke():
    gen = AlethesGenerator(GenerationConfig(model_name_or_path="sshleifer/tiny-gpt2", max_new_tokens=5))
    text = gen.generate("Test Title", "tech", "2025-01-01", "Author")
    assert isinstance(text, str)
