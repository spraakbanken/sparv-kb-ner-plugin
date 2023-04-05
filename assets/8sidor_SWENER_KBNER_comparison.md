# Comparison between KBNER and SWENER

Example text: [8sidor example](./texts/8sidor-mini.xml)

All annotations are runned with `sparv run`.

Running times | mean | values | comment
| - | - | - | -
KBNER | ... | 1h23m34s | from xml, emitting 75 warnings
SWENER | 18m58s | 18m30s,19m26s | from xml

**Ouch!** correct but slow...

# Scaling problem

The mapping of tokens and ner_tags were rewritten to handle all cases in this example, but somewhere the speed from Ikea_example got loss (KBNER ~25s, SWENER ~60s). And that timing still holds with the rewritten mapping.

## How does SWENER scale?

### SWENER
| `#<text>` | mean | values | `s/<text>`
| - | - | - | - |
1 | 53s | 53s | 53.0
2 | 55s | 55s | 27.5
3 | 54s | 54s | 18.0
30 | 1m04s | 1m04s | 2.13
60 | 1m13s | 1m13s | 1.22
120 | 1m36s | 1m36s | 0.8
180 | 1m55s | 1m55s | 0.64
210 | 2m6s | 2m6s | 0.6
300 | 2m33s| 2m33s | 0.51
600 | 4m8s | 4m8s | 0.41
1000 | | |
3433 | 18m58s | 18m30s,19m26s | 0.33
## When does the KBNER-plugin lose speed?

### KBNER
| `#<text>` | mean | values | `s/<text>`
| - | - | - | - |
1 | 18s | 18s | 18.0
2 | 17s | 17s | 8.5
3 | 17s | 17s | 5.67
30 | 54s | 54s | 1.8
60 | 1m29s | 1m29s | 1.48
120 | 2m43s | 2m43s | 1.36
180 | 3m48s | 3m48s | 1.27
3433 | 1h23m24s | 1h23m24s | 1.46





```diff
```
