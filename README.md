
![Logo](https://lh3.googleusercontent.com/nXuyIkRk3ydUmijFq5Rgs89ehCm0reisO1KWJa7Vs_DpvCWielPgP7UlVq8nUhvXY-7bC7vf3tZhenOW80tcUamLFODT38SB3fFj419DwWalZDOryNAVwr6ym27Cp4eP8Z9z9_rwB_9iZPjGKFNhxXJTRAADFtyDg0tYZmXK-QNSZWC-yh79V4oiIapu_bWvmatlrgPcepTSJ6_-HPfns5Ny6d1rCQ9txZ9U5SZDJ-n79_oCLo-DTLeGR514nTzGQxs3j3pJTEd3vTgXglXffeCZSYGCkv5pg7rChVplX-3lJ-yBHB1o3L_rLBQYi1GW7xxXWV3DfO1jze0LmJk7AY1cuHBNNHu1gvLqfSoDpFuTWvtQ5p95KpNSvTVMTzXcQsQCBNfgiRvTQG1Ur8hemM4JW4HLrohx5uLnWy3D9WRjCNII_waBkkF_zpm_1OUVGKeJseXrkxZPIkM9WwcTlLxdheSnw29lB3F9cQBOW5mGm6fjljOUqHgn1WZA5eaEEvHwE0dx0dMna9lqE6Fm469ZPeiNq1fxT-K4we4-1MiAGjRjlKtVik28vr2xBP4zBaE69fU9bPdE8uvJdu-SaRRgt0Zm0bSK-iGbu66wGq8WaoCp0UQqHyoQccO8oR7DGXFMTLyaonNluAZdstlFSu6H6rw-DIhkURJHfTdsc6GzdpCvgII7f1FM1Mrz7nmtJRPH4-ggZKSi7-mJ3rLDC_7SpFgTZxk_y2Mv5pkjQu_A8WB96Kl2gkOemwfBMgfNvSKZoxFCY8HwFS6Eg8-0ETw35LSMz-wzuHl8RdbB_Kc8PE4pNf0iFA0QhU06W6Kc-ROYU2NiNjbNmKlXdVN79UBsVIpuo1KzeA9uHvviS9sH4tB6f6rBEkbNTjMy_R_MnBnXur-KQ3sF1zAheINcdZ189VmCSKCAzSM0H4V-Mft3I8Rv=w600-h250-s-no?authuser=0)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
# MasterPannel
Software used for remote file management using protocols SSH and SFTP. Files are securely transferred, copied, and received with all bits of sensitive information secured and encrypted. Features a LAN IP scanner so you can find your computers more easily on a LAN and a client is added for ease of setup on remote computers. You can also recursively deploy files on separate computers and upload multiple files at once. You can save computer information so you don't have to type in the IP, Username, and Password every time like in the CLI.
## Screenshots

![App Screenshot](https://lh3.googleusercontent.com/1qAb4vVIgFpjShV1gkwkzdeZDdOvJqaQYcQUuO08N89lFuQIlGsNq-6n-wBDEFxOhMtI-5UrK8-SESH_788a93wnJJMRlUdruziflRgIV-sFJlhvF-J__ILZblVFwcwrgcrvOKjYQep5QNT1c8azPrt48pta7ZhXpgYNhunatbuH4ZHpmtQ0PJOWh-gaiAYmr7d7oF12UFzj_UaA5VuafkYKp49PC4mVhnlcc9a-gDO0IimNhxkLcNS2JzfBpY_D3_fqXtcJ8_FrPx3nDVxcOVFCu1zzk-DSartl8E2zZj6pKDwdj5fYuY51TF9ESd-yVP037eJ_FDAMCGWF51RSXRrtKC8BbR6Uc7-mtbuzxB8LfdnKUtPj-r66EyMHic-tZ5eLKeJkGd-WBprjrB4f5HwKX4AcW0nqZ99DaIxszpnh1J41xc7iLRPFnnb9E0BPhwdE6yGGKNgZBslRdc1oNz4YWQDEkwFRhe5PkdMps4UiOcEAg6h_Kmb9jnsPGsVLPigDt8UEzUL6gUYrokE8TJI2TtiYpBeqFkMsyt4tio3cadQ27C203Qo-vkWaQuJqVRKIuwp-xEr2VQLU-zflVhhUQi_7_pa-i1pUqSKWAxmTnjN0pUqWoJcvlHpM9rpAT3tdClxhQvHFyZdk6rHURlk5-JmifQ1r8Au0sLdCdo_-qn8mLqDHmcHLx0ghjsbupj3vt2fnenCmu9OfAwL_T0YI-nDvNU-L5Y5SImgxuLaXpX4rSSvwU99DY3xgG0E2WhXSGTLGNWbtiDvmsdOirbVTEOLz8otTQFTdet_78EE9gpAGe91ADooaI-Ts-usEUw9TgHu-LMGsfnFMgXmoh0-zkIh2G3wx_LEYV0itIB4sztQajgp8MmgzwVuLQy7tyI-9wWSPOgsqMWasY5wTy_BuMETg_W7h9Ms8IN8ti5WvBQpw=w800-h530-s-no?authuser=0)


## Installation

Download dependencies:

```bash
  pip install tk

  pip install paramiko

  pip install scp

  pip install subprocess.run
```
Change the directory and install:
```bash
  cd Desktop/

  git clone https://github.com/s5y-ux/MasterPannel

  cd MasterPannel/
  
  python3 main.py
```