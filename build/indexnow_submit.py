# -*- coding: utf-8 -*-
"""indexnow_submit.py - re-submit all sitemap URLs to IndexNow.
The api.indexnow.org aggregator distributes to Bing, Yandex, Seznam, and Naver.
Run with the seo-intel venv python (truststore handles the corporate TLS proxy):
  "C:/Users/mattb/Documents/Claude Brain/seo-intel/.venv/Scripts/python.exe" indexnow_submit.py
"""
import os, re
try:
    import truststore; truststore.inject_into_ssl()
except Exception as e:
    print("WARN truststore unavailable:", e)
import requests

HOST   = "digitalinformationgovernance.com"
KEY    = "2d62304c737389ee609eecfa509ca2f0"
KEYLOC = "https://%s/%s.txt" % (HOST, KEY)
SITEMAP = os.path.join(os.path.dirname(__file__), "..", "site", "sitemap.xml")

urls = re.findall(r"<loc>(.*?)</loc>", open(SITEMAP, encoding="utf-8").read())
print("Sitemap URLs: %d" % len(urls))

# confirm the key file is reachable (IndexNow validates ownership against it)
try:
    kf = requests.get(KEYLOC, timeout=20)
    print("Key file %s -> HTTP %d (%s)" % (KEYLOC, kf.status_code, kf.text.strip()[:40]))
except Exception as e:
    print("Key file check ERROR:", e)

body = {"host": HOST, "key": KEY, "keyLocation": KEYLOC, "urlList": urls}
try:
    r = requests.post("https://api.indexnow.org/indexnow", json=body, timeout=30,
                      headers={"Content-Type": "application/json; charset=utf-8"})
    print("IndexNow aggregator -> HTTP %d  %r" % (r.status_code, r.text[:200]))
    print("(200/202 = accepted)")
except Exception as e:
    print("IndexNow POST ERROR:", e)
