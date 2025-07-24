import argparse, json
from ..discriminator.classifier import AlethesDiscriminator, DiscriminatorConfig

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model_name_or_path", required=True)
    ap.add_argument("--input_file", required=True, help="JSONL with {id,text}")
    ap.add_argument("--output_file", required=True)
    args = ap.parse_args()

    disc = AlethesDiscriminator(DiscriminatorConfig(args.model_name_or_path))
    with open(args.input_file) as f:
        records = [json.loads(line) for line in f]
    texts = [r["text"] for r in records]
    scores = disc.predict(texts)
    with open(args.output_file, "w") as out:
        for r, s in zip(records, scores):
            out.write(json.dumps({"id": r.get("id"), "score": s, "is_synthetic": s > 0.5}) + "\\n")
    print(f"Wrote {len(records)} predictions to {args.output_file}")

if __name__ == "__main__":
    main()
