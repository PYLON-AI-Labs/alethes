import argparse, json
from ..generator.modeling import AlethesGenerator, GenerationConfig

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model_name_or_path", default="gpt2")
    ap.add_argument("--title", required=True)
    ap.add_argument("--domain", default="general")
    ap.add_argument("--date", required=True)
    ap.add_argument("--authors", default="Unknown")
    ap.add_argument("--max_new_tokens", type=int, default=400)
    args = ap.parse_args()

    config = GenerationConfig(model_name_or_path=args.model_name_or_path,
                              max_new_tokens=args.max_new_tokens)
    gen = AlethesGenerator(config)
    article = gen.generate(args.title, args.domain, args.date, args.authors)
    print(json.dumps({
        "title": args.title,
        "domain": args.domain,
        "date": args.date,
        "authors": args.authors,
        "article": article
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
