"""N=100 paired Cortex vs Native experiment runner."""
import json, os, sys, subprocess, re, time, csv, urllib.request, urllib.error
from pathlib import Path

LABELS_PATH = Path("/tmp/labels-v2.json")
RESULTS_PATH = Path("/tmp/results-v2.csv")
COMPOSE_PATH = "/home/deploy/repos/darke-studio/docker-compose.alpha.yml"

MODELS = [
    "anthropic/claude-haiku-4.5",
    "deepseek/deepseek-v3.2",
    "openai/gpt-5.4-mini",
]

NATIVE_SYSTEM = (
    "Rate the following text on a 0-100 scale for AI-likeness. "
    "0 means obviously human-written. 100 means obviously AI-generated. "
    "Respond with ONLY a single integer between 0 and 100. No explanation, no other text."
)

def get_openrouter_key():
    out = subprocess.run(["bash","-lc","grep OPENROUTER_API_KEY /home/deploy/repos/darke-studio/.env | cut -d= -f2"], capture_output=True, text=True)
    return out.stdout.strip()

def set_model_and_recreate(model):
    py = ("import re;"
          f"p=open('{COMPOSE_PATH}').read();"
          f"p=re.sub(r'OPENROUTER_MODEL: [^\\n]+', 'OPENROUTER_MODEL: {model}', p);"
          f"open('{COMPOSE_PATH}','w').write(p)")
    subprocess.run(["python3","-c",py], check=True)
    subprocess.run(["bash","-lc","cd /home/deploy/repos/darke-studio && docker compose -f docker-compose.alpha.yml up -d --force-recreate voxsigil > /dev/null 2>&1"], check=True)
    print(f"  recreated voxsigil with {model}, waiting 15s...", flush=True)
    time.sleep(15)

def post_json(url, body, headers, timeout=90):
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    for k, v in headers.items():
        req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")
    except Exception as e:
        return 0, f"EXC: {e}"

def cortex_call(text, sample_id):
    status, raw = post_json("http://127.0.0.1:3031/api/check", {"text": text},
                            {"Cookie": f"voxsigil_check_id=v2-{sample_id}-{int(time.time())}"})
    if status != 200:
        return None, "", f"http_{status}: {raw[:200]}"
    try:
        d = json.loads(raw)
        return d.get("score"), d.get("meta",{}).get("modelUsed",""), None
    except Exception as e:
        return None, "", f"parse: {e}: {raw[:200]}"

def native_call(text, model, key):
    body = {"model": model, "messages": [
        {"role":"system","content": NATIVE_SYSTEM},
        {"role":"user","content": text}],
        "temperature": 0.2, "max_tokens": 40, "provider": {"data_collection":"allow"}}
    status, raw = post_json("https://openrouter.ai/api/v1/chat/completions", body, {"Authorization": f"Bearer {key}"})
    if status != 200:
        return None, model, f"http_{status}: {raw[:200]}"
    try:
        d = json.loads(raw)
        content = d["choices"][0]["message"]["content"].strip()
        m = re.search(r"\d+", content)
        if m: return int(m.group(0)), model, None
        return None, model, f"no_int: {content[:60]}"
    except Exception as e:
        return None, model, f"parse: {e}: {raw[:200]}"

def save_rows(rows):
    with RESULTS_PATH.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["sample_id","label","class","claude_score","model","condition","score","model_used","error"])
        w.writeheader()
        w.writerows(rows)

def main():
    labels = json.loads(LABELS_PATH.read_text())
    samples = labels["samples"]
    key = get_openrouter_key()
    print(f"N={len(samples)} samples. Key: {key[:12]}...", flush=True)

    rows = []
    for model in MODELS:
        print(f"\n=== {model} ===", flush=True)
        set_model_and_recreate(model)

        for s in samples:
            score, mu, err = cortex_call(s["text"], s["id"])
            print(f"  #{s['id']:3d} cortex={score} mu={mu[:30]}", flush=True)
            if err: print(f"      ERR: {err[:120]}", flush=True)
            rows.append({"sample_id": s["id"], "label": s["label"], "class": s["class"],
                         "claude_score": s["claude_score"], "model": model, "condition": "cortex",
                         "score": score, "model_used": mu, "error": err or ""})
            score, mu, err = native_call(s["text"], model, key)
            print(f"  #{s['id']:3d} native={score}", flush=True)
            if err: print(f"      ERR: {err[:120]}", flush=True)
            rows.append({"sample_id": s["id"], "label": s["label"], "class": s["class"],
                         "claude_score": s["claude_score"], "model": model, "condition": "native",
                         "score": score, "model_used": mu, "error": err or ""})
            if s["id"] % 10 == 0: save_rows(rows)
            time.sleep(0.3)

    save_rows(rows)
    print(f"\nWrote {len(rows)} rows to {RESULTS_PATH}", flush=True)

if __name__ == "__main__":
    main()
