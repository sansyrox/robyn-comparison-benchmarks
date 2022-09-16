# A set of simple and equal benchmarks.
This compares Robyn, Starlette and FastAPI.

This is run on a dual core MacBook(2017), servers are ran as they
are expected to be used in prod i.e uvicorn runs the ASGI apps with n workers 
equal to the logical CPU count. Robyn workers and processes are toggled manually at the moment for max performance.

Results done via oha and the CLI command is as follows:


# Friday, September 16, 17:33

System Info
```
      eeeeeeeeeeeeeeeeeeeeeee         ------------------ 
    eeeee  eeeeeeeeeeee   eeeee       OS: elementary OS 6.1 Jólnir x86_64 
  eeee   eeeee       eee     eeee     Kernel: 5.15.0-46-generic 
 eeee   eeee          eee     eeee    Uptime: 5 hours, 11 mins 
eee    eee            eee       eee   Packages: 2239 (dpkg), 11 (flatpak), 16 (snap) 
eee   eee            eee        eee   Shell: zsh 5.8 
ee    eee           eeee       eeee   Resolution: 3840x2160, 2160x3840 
ee    eee         eeeee      eeeeee   DE: Pantheon 
ee    eee       eeeee      eeeee ee   WM: Mutter(Gala) 
eee   eeee   eeeeee      eeeee  eee   Terminal: kitty 
eee    eeeeeeeeee     eeeeee    eee   CPU: AMD Ryzen 9 5900X (24) @ 3.700GHz 
 eeeeeeeeeeeeeeeeeeeeeeee    eeeee    GPU: NVIDIA 09:00.0 NVIDIA Corporation Device 2489 
  eeeeeeee eeeeeeeeeeee      eeee     Memory: 5350MiB / 64213MiB 
    eeeee                 eeeee
      eeeeeee         eeeeeee                                 
         eeeeeeeeeeeeeeeee                                    
```

```bash
Go (GIN) server benchmarks

➜  go_web_server git:(master) ✗ oha http://127.0.0.1:8080 -n 100000 --no-tui
Summary:
  Success rate:	1.0000
  Total:	0.5406 secs
  Slowest:	0.0069 secs
  Fastest:	0.0000 secs
  Average:	0.0003 secs
  Requests/sec:	184995.9121

  Total data:	1.72 MiB
  Size/request:	18 B
  Size/sec:	3.18 MiB

Response time histogram:
  0.000 [1]     |
  0.001 [97095] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.001 [2629]  |
  0.002 [65]    |
  0.003 [40]    |
  0.003 [42]    |
  0.004 [25]    |
  0.005 [21]    |
  0.006 [33]    |
  0.006 [28]    |
  0.007 [21]    |

Latency distribution:
  10% in 0.0001 secs
  25% in 0.0001 secs
  50% in 0.0002 secs
  75% in 0.0004 secs
  90% in 0.0005 secs
  95% in 0.0006 secs
  99% in 0.0009 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0003 secs, 0.0002 secs, 0.0006 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0002 secs

Status code distribution:
  [404] 100000 responses
```

```bash
Robyn (10 Processes | Const Requests)

Summary:
  Success rate:	1.0000
  Total:	0.2477 secs
  Slowest:	0.0096 secs
  Fastest:	0.0000 secs
  Average:	0.0001 secs
  Requests/sec:	403746.4033

  Total data:	1.24 MiB
  Size/request:	13 B
  Size/sec:	5.01 MiB

Response time histogram:
  0.000 [1]     |
  0.001 [99880] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.002 [72]    |
  0.003 [0]     |
  0.004 [2]     |
  0.005 [8]     |
  0.006 [0]     |
  0.007 [0]     |
  0.008 [7]     |
  0.009 [18]    |
  0.010 [12]    |

Latency distribution:
  10% in 0.0000 secs
  25% in 0.0001 secs
  50% in 0.0001 secs
  75% in 0.0002 secs
  90% in 0.0002 secs
  95% in 0.0002 secs
  99% in 0.0005 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0003 secs, 0.0001 secs, 0.0007 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0000 secs

Status code distribution:
  [200] 100000 responses
```

```bash
Starlette ( 24 workers )

Summary:
  Success rate:	1.0000
  Total:	1.4629 secs
  Slowest:	0.0117 secs
  Fastest:	0.0002 secs
  Average:	0.0007 secs
  Requests/sec:	68355.6899

  Total data:	1.24 MiB
  Size/request:	13 B
  Size/sec:	867.80 KiB

Response time histogram:
  0.000 [1]     |
  0.001 [92393] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.002 [7458]  |■■
  0.004 [109]   |
  0.005 [13]    |
  0.006 [1]     |
  0.007 [1]     |
  0.008 [9]     |
  0.009 [4]     |
  0.011 [6]     |
  0.012 [5]     |

Latency distribution:
  10% in 0.0003 secs
  25% in 0.0004 secs
  50% in 0.0007 secs
  75% in 0.0010 secs
  90% in 0.0012 secs
  95% in 0.0015 secs
  99% in 0.0019 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0003 secs, 0.0001 secs, 0.0011 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0000 secs

Status code distribution:
  [200] 100000 responses
```

```bash
fastapi 48 workers uvicorn

Summary:
  Success rate:	1.0000
  Total:	1.6872 secs
  Slowest:	0.0128 secs
  Fastest:	0.0002 secs
  Average:	0.0008 secs
  Requests/sec:	59268.7685

  Total data:	1.24 MiB
  Size/request:	13 B
  Size/sec:	752.43 KiB

Response time histogram:
  0.000 [1]     |
  0.001 [78382] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.003 [19839] |■■■■■■■■
  0.004 [1633]  |
  0.005 [76]    |
  0.007 [18]    |
  0.008 [16]    |
  0.009 [17]    |
  0.010 [15]    |
  0.012 [1]     |
  0.013 [2]     |

Latency distribution:
  10% in 0.0003 secs
  25% in 0.0003 secs
  50% in 0.0005 secs
  75% in 0.0010 secs
  90% in 0.0020 secs
  95% in 0.0024 secs
  99% in 0.0029 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0008 secs, 0.0001 secs, 0.0029 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0010 secs

Status code distribution:
  [200] 100000 responses
```

```bash
express server with pm2 
Summary:
  Success rate:	1.0000
  Total:	8.5489 secs
  Slowest:	0.0512 secs
  Fastest:	0.0036 secs
  Average:	0.0043 secs
  Requests/sec:	11697.3641

  Total data:	1.14 MiB
  Size/request:	12 B
  Size/sec:	137.08 KiB

Response time histogram:
  0.004 [1]     |
  0.008 [99355] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.013 [584]   |
  0.018 [10]    |
  0.023 [0]     |
  0.027 [0]     |
  0.032 [0]     |
  0.037 [1]     |
  0.042 [11]    |
  0.046 [16]    |
  0.051 [22]    |

Latency distribution:
  10% in 0.0037 secs
  25% in 0.0038 secs
  50% in 0.0039 secs
  75% in 0.0044 secs
  90% in 0.0052 secs
  95% in 0.0059 secs
  99% in 0.0078 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0002 secs, 0.0001 secs, 0.0003 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0000 secs

Status code distribution:
  [200] 100000 responses
```

```bash
actix (24 workers) | cpu count

Summary:
  Success rate:	1.0000
  Total:	0.3583 secs
  Slowest:	0.0086 secs
  Fastest:	0.0000 secs
  Average:	0.0002 secs
  Requests/sec:	279113.0297

  Total data:	3.81 MiB
  Size/request:	40 B
  Size/sec:	10.65 MiB

Response time histogram:
  0.000 [1]     |
  0.001 [99870] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.002 [86]    |
  0.003 [7]     |
  0.003 [9]     |
  0.004 [7]     |
  0.005 [14]    |
  0.006 [0]     |
  0.007 [0]     |
  0.008 [2]     |
  0.009 [4]     |

Latency distribution:
  10% in 0.0001 secs
  25% in 0.0001 secs
  50% in 0.0001 secs
  75% in 0.0002 secs
  90% in 0.0004 secs
  95% in 0.0005 secs
  99% in 0.0006 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0004 secs, 0.0001 secs, 0.0010 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0002 secs

Status code distribution:
  [404] 100000 responses
```

```bash
actix | 48 workers

Summary:
  Success rate:	1.0000
  Total:	0.3261 secs
  Slowest:	0.0072 secs
  Fastest:	0.0000 secs
  Average:	0.0002 secs
  Requests/sec:	306626.7157

  Total data:	3.81 MiB
  Size/request:	40 B
  Size/sec:	11.70 MiB

Response time histogram:
  0.000 [1]     |
  0.001 [99591] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.001 [369]   |
  0.002 [9]     |
  0.003 [5]     |
  0.004 [3]     |
  0.004 [5]     |
  0.005 [8]     |
  0.006 [6]     |
  0.006 [2]     |
  0.007 [1]     |

Latency distribution:
  10% in 0.0001 secs
  25% in 0.0001 secs
  50% in 0.0001 secs
  75% in 0.0002 secs
  90% in 0.0003 secs
  95% in 0.0005 secs
  99% in 0.0006 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0003 secs, 0.0001 secs, 0.0006 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0000 secs

Status code distribution:
  [404] 100000 responses
```


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
