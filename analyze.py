"""Analyze Aura Cortex vs Base Model results — paired bootstrap MAE.

Inputs: results-v2.csv with columns sample_id, label, class, claude_score, model, condition, score, model_used, error.
Outputs: per-model MAE + bootstrap 95% CI on (MAE_native - MAE_cortex), class-stratified breakdown.
"""
import csv, random, statistics
from pathlib import Path
from collections import defaultdict

CSV = Path("data/results-v2.csv")

def load():
    rows = []
    with CSV.open() as f:
        for row in csv.DictReader(f):
            try:
                row["score"] = int(row["score"]) if row["score"] not in ("", "None") else None
                row["claude_score"] = int(row["claude_score"])
                row["sample_id"] = int(row["sample_id"])
                rows.append(row)
            except Exception:
                pass
    return rows

def bootstrap_ci(values, iters=10000, alpha=0.05):
    if not values:
        return None, None
    n = len(values)
    means = []
    for _ in range(iters):
        sample = [values[random.randrange(n)] for _ in range(n)]
        means.append(sum(sample) / n)
    means.sort()
    lo = means[int(iters * (alpha/2))]
    hi = means[int(iters * (1 - alpha/2))]
    return lo, hi

def per_model_paired(rows, model):
    """Return per-sample (cortex_err, native_err, diff) tuples for one model."""
    by_id = defaultdict(dict)
    for r in rows:
        if r["model"] != model:
            continue
        if r["score"] is None:
            continue
        by_id[r["sample_id"]][r["condition"]] = (r["score"], r["claude_score"])
    paired = []
    for sid, d in by_id.items():
        if "cortex" in d and "native" in d:
            cs, cl = d["cortex"]
            ns, _ = d["native"]
            cortex_err = abs(cs - cl)
            native_err = abs(ns - cl)
            paired.append((sid, cortex_err, native_err, native_err - cortex_err))
    return paired

def main():
    rows = load()
    models = sorted(set(r["model"] for r in rows))
    print(f"Loaded {len(rows)} rows. Models: {models}\n")

    overall_diffs = []  # native_err - cortex_err, pooled across models for the cross-model claim

    for model in models:
        paired = per_model_paired(rows, model)
        if not paired:
            print(f"=== {model} ===\n  No paired data\n")
            continue
        cortex_errs = [p[1] for p in paired]
        native_errs = [p[2] for p in paired]
        diffs = [p[3] for p in paired]
        overall_diffs.extend(diffs)

        cortex_mae = sum(cortex_errs) / len(cortex_errs)
        native_mae = sum(native_errs) / len(native_errs)
        diff_mean = sum(diffs) / len(diffs)
        lo, hi = bootstrap_ci(diffs)

        print(f"=== {model}  (N={len(paired)}) ===")
        print(f"  Cortex MAE: {cortex_mae:.2f}")
        print(f"  Native MAE: {native_mae:.2f}")
        print(f"  Mean (Native − Cortex) per-sample diff: {diff_mean:+.2f}")
        print(f"  95% CI on (Native − Cortex): [{lo:+.2f}, {hi:+.2f}]")
        verdict = "Cortex meaningfully better" if lo >= 2.0 else \
                  "Cortex marginally better" if lo > 0 else \
                  "Cortex hurts" if hi <= 0 else \
                  "Cortex no different"
        print(f"  Verdict: {verdict}\n")

        # Class-stratified
        print(f"  Class breakdown:")
        cls_paired = defaultdict(dict)
        for r in rows:
            if r["model"] != model or r["score"] is None:
                continue
            cls_paired[(r["sample_id"], r["class"])][r["condition"]] = r["score"]
        # rebuild grouped by class
        class_diffs = defaultdict(list)
        for (sid, cls), d in cls_paired.items():
            if "cortex" in d and "native" in d:
                cl = next(rr["claude_score"] for rr in rows if rr["sample_id"] == sid)
                cortex_err = abs(d["cortex"] - cl)
                native_err = abs(d["native"] - cl)
                class_diffs[cls].append((cortex_err, native_err))
        for cls in ["clear_ai", "human", "ambig"]:
            ds = class_diffs.get(cls, [])
            if not ds:
                print(f"    {cls}: no data")
                continue
            cmae = sum(c for c, _ in ds) / len(ds)
            nmae = sum(n for _, n in ds) / len(ds)
            print(f"    {cls:10s} (n={len(ds)}): cortex_MAE={cmae:5.2f}  native_MAE={nmae:5.2f}  Δ={nmae-cmae:+.2f}")
        print()

    # Cross-model meta-analysis
    if overall_diffs:
        n = len(overall_diffs)
        mean = sum(overall_diffs) / n
        lo, hi = bootstrap_ci(overall_diffs)
        print(f"=== Cross-model meta-analysis (pooled paired diffs, N={n}) ===")
        print(f"  Mean (Native − Cortex): {mean:+.2f}")
        print(f"  95% CI: [{lo:+.2f}, {hi:+.2f}]")
        verdict = "Cortex meaningfully better across models" if lo >= 2.0 else \
                  "Cortex marginally better across models" if lo > 0 else \
                  "Cortex hurts across models" if hi <= 0 else \
                  "Cortex no different across models"
        print(f"  Verdict: {verdict}")

if __name__ == "__main__":
    random.seed(42)
    main()
