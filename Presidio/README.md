import pymupdf, numpy as np, hashlib

def feats(raw):
    with pymupdf.open(stream=raw, filetype="pdf") as d:
        md, p = d.metadata or {}, d[0]
        im = max(p.get_image_info(), key=lambda i: i["width"] * i["height"], default={})
        pix = p.get_pixmap(dpi=50, colorspace=pymupdf.csGRAY)
        a = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width)
        ink = a < 128
        rows, cols = ink.any(1), ink.any(0)
        return {
            "producer": (md.get("producer") or "")[:40],
            "creator": (md.get("creator") or "")[:40],
            "pw": round(p.rect.width), "ph": round(p.rect.height), "rot": p.rotation,
            "img_w": im.get("width", 0), "img_h": im.get("height", 0),
            "img_dpi": round(im.get("xres", 0)), "img_bpc": im.get("bpc", 0),
            "img_cs": im.get("colorspace", 0), "img_bytes": im.get("size", 0),
            "ink": float(ink.mean()),
            "top_margin": float(np.argmax(rows)) / pix.height if rows.any() else 1.0,
            "left_margin": float(np.argmax(cols)) / pix.width if cols.any() else 1.0,
            "blank": float(ink.mean()) < 0.002,
            "md5": hashlib.md5(raw).hexdigest(),
        }



def feats_path(path):
    try:
        with open(path, "rb") as f:
            raw = f.read()
        r = feats(raw)
        r["path"], r["size"] = path, len(raw)
        return r
    except Exception as e:
        return {"path": path, "err": str(e)[:100]}



import os
from pyspark.sql import Row

def run_partition(paths):
    for p in paths:
        yield Row(**{k: (v if not isinstance(v, (np.floating, np.integer, np.bool_)) else v.item())
                     for k, v in feats_path(p).items()})

paths_rdd = spark.sparkContext.parallelize(paths, 2000)     # about 1,000 paths per partition
feat_df = paths_rdd.mapPartitions(run_partition).toDF()
feat_df.write.mode("overwrite").parquet("feat_out/")
