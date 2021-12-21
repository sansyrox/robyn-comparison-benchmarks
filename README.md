# A set of simple and equal benchmarks.
This compares Robyn, Starlette and FastAPI.

This is run on a dual core MacBook(2017), servers are ran as they
are expected to be used in prod i.e uvicorn runs the ASGI apps with n workers 
equal to the logical CPU count. Robyn workers and processes are toggled manually at the moment for max performance.

Results done via oha and the CLI command is as follows:

# Robyn 
#### `oha --no-tui --insecure -c 100 -n 100000 http://127.0.0.1:5000`


Command to run robyn(for the max throughput on a dual core macbook): `python3 test_robyn.py --workers=6 --processes=2`

```
Summary:
  Success rate:	1.0000
  Total:	10.0448 secs
  Slowest:	0.1306 secs
  Fastest:	0.0006 secs
  Average:	0.0100 secs
  Requests/sec:	9955.4351

  Total data:	1.24 MiB
  Size/request:	13 B
  Size/sec:	126.39 KiB

Response time histogram:
  0.003 [12604] |■■■■■■■■■■■■
  0.005 [33362] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.008 [21189] |■■■■■■■■■■■■■■■■■■■■
  0.011 [14714] |■■■■■■■■■■■■■■
  0.013 [5258]  |■■■■■
  0.016 [2050]  |■
  0.019 [1408]  |■
  0.021 [1033]  |
  0.024 [847]   |
  0.027 [771]   |
  0.029 [6764]  |■■■■■■

Latency distribution:
  10% in 0.0031 secs
  25% in 0.0040 secs
  50% in 0.0065 secs
  75% in 0.0098 secs
  90% in 0.0181 secs
  95% in 0.0349 secs
  99% in 0.0723 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0049 secs, 0.0033 secs, 0.0070 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0000 secs

Status code distribution:
  [200] 100000 responses
```

# Starlette
#### `oha --no-tui --insecure -c 100 -n 100000 http://127.0.0.1:8000`
```
Summary:
  Success rate:	1.0000
  Total:	12.8869 secs
  Slowest:	0.0485 secs
  Fastest:	0.0004 secs
  Average:	0.0129 secs
  Requests/sec:	7759.7922

  Total data:	1.24 MiB
  Size/request:	13 B
  Size/sec:	98.51 KiB

Response time histogram:
  0.003 [28763] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.007 [3215]  |■■■
  0.010 [2062]  |■■
  0.014 [8630]  |■■■■■■■■■
  0.017 [25856] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.021 [22909] |■■■■■■■■■■■■■■■■■■■■■■■■■
  0.024 [6511]  |■■■■■■■
  0.028 [1450]  |■
  0.031 [266]   |
  0.035 [214]   |
  0.038 [124]   |

Latency distribution:
  10% in 0.0024 secs
  25% in 0.0033 secs
  50% in 0.0152 secs
  75% in 0.0188 secs
  90% in 0.0210 secs
  95% in 0.0223 secs
  99% in 0.0264 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0092 secs, 0.0062 secs, 0.0113 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0000 secs

Status code distribution:
  [200] 100000 responses
 ```
  

# FastAPI
#### `oha --no-tui --insecure -c 100 -n 100000 http://127.0.0.1:8800`
```
Summary:
  Success rate:	1.0000
  Total:	14.2595 secs
  Slowest:	0.0328 secs
  Fastest:	0.0005 secs
  Average:	0.0142 secs
  Requests/sec:	7012.8769

  Total data:	1.24 MiB
  Size/request:	13 B
  Size/sec:	89.03 KiB

Response time histogram:
  0.003 [423]   |
  0.006 [9524]  |■■■■■■■■■■
  0.009 [23313] |■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.012 [2733]  |■■■
  0.015 [3932]  |■■■■
  0.018 [28203] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.021 [27592] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.023 [3477]  |■■■
  0.026 [539]   |
  0.029 [184]   |
  0.032 [80]    |

Latency distribution:
  10% in 0.0064 secs
  25% in 0.0077 secs
  50% in 0.0167 secs
  75% in 0.0186 secs
  90% in 0.0201 secs
  95% in 0.0208 secs
  99% in 0.0236 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0072 secs, 0.0065 secs, 0.0084 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0001 secs

Status code distribution:
  [200] 100000 responses
```
