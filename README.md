# A set of simple and equal benchmarks.
This compares Robyn, Starlette and FastAPI.

Results done via oha and the CLI command is as follows:

# Robyn oha --no-tui --insecure --latency-correction -c 500 -n 100000 http://127.0.0.1:5000
```Summary:
  Success rate:	1.0000
  Total:	4.1176 secs
  Slowest:	0.0643 secs
  Fastest:	0.0039 secs
  Average:	0.0204 secs
  Requests/sec:	24286.1496

  Total data:	1.24 MiB
  Size/request:	13 B
  Size/sec:	308.32 KiB

Response time histogram:
  0.005 [840]   |
  0.010 [9347]  |■■■■■■■
  0.016 [41611] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.021 [22384] |■■■■■■■■■■■■■■■■■
  0.026 [21734] |■■■■■■■■■■■■■■■■
  0.031 [3715]  |■■
  0.037 [202]   |
  0.042 [43]    |
  0.047 [44]    |
  0.052 [58]    |
  0.057 [22]    |

Latency distribution:
  10% in 0.0143 secs
  25% in 0.0165 secs
  50% in 0.0193 secs
  75% in 0.0250 secs
  90% in 0.0281 secs
  95% in 0.0296 secs
  99% in 0.0323 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0120 secs, 0.0001 secs, 0.0386 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0027 secs

Status code distribution:
  [200] 100000 responses
```

# Starlette oha --no-tui --insecure --latency-correction -c 500 -n 100000 http://127.0.0.1:8000
```Summary:
  Success rate:	1.0000
  Total:	0.9011 secs
  Slowest:	0.1057 secs
  Fastest:	0.0001 secs
  Average:	0.0043 secs
  Requests/sec:	110974.6662

  Total data:	1.24 MiB
  Size/request:	13 B
  Size/sec:	1.38 MiB

Response time histogram:
  0.001 [3428]  |■■■
  0.002 [19031] |■■■■■■■■■■■■■■■■■■
  0.004 [33125] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.005 [23393] |■■■■■■■■■■■■■■■■■■■■■■
  0.006 [9320]  |■■■■■■■■■
  0.007 [3834]  |■■■
  0.008 [2155]  |■■
  0.009 [1066]  |■
  0.011 [760]   |
  0.012 [615]   |
  0.013 [3273]  |■■■

Latency distribution:
  10% in 0.0019 secs
  25% in 0.0026 secs
  50% in 0.0034 secs
  75% in 0.0045 secs
  90% in 0.0064 secs
  95% in 0.0091 secs
  99% in 0.0202 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0373 secs, 0.0003 secs, 0.0915 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0021 secs

Status code distribution:
  [200] 100000 responses```
  

# FastAPI oha --no-tui --insecure --latency-correction -c 500 -n 100000 http://127.0.0.1:8800
```
Summary:
  Success rate:	1.0000
  Total:	1.1920 secs
  Slowest:	0.0484 secs
  Fastest:	0.0001 secs
  Average:	0.0059 secs
  Requests/sec:	83891.1719

  Total data:	1.24 MiB
  Size/request:	13 B
  Size/sec:	1.04 MiB

Response time histogram:
  0.002 [5549]  |■■■■■■■■
  0.003 [19647] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.005 [20332] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.006 [15749] |■■■■■■■■■■■■■■■■■■■■■■■■
  0.008 [16418] |■■■■■■■■■■■■■■■■■■■■■■■■■
  0.010 [14209] |■■■■■■■■■■■■■■■■■■■■■■
  0.011 [4502]  |■■■■■■■
  0.013 [1070]  |■
  0.014 [403]   |
  0.016 [378]   |
  0.017 [1743]  |■■

Latency distribution:
  10% in 0.0022 secs
  25% in 0.0033 secs
  50% in 0.0054 secs
  75% in 0.0078 secs
  90% in 0.0094 secs
  95% in 0.0104 secs
  99% in 0.0193 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0191 secs, 0.0001 secs, 0.0388 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0000 secs

Status code distribution:
  [200] 100000 responses
```