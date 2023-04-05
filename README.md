
![Logo](https://lh3.googleusercontent.com/Yld6qcVtyU2HdajoO31ms16wgLn1qjUldKVMi4TTjC4FCvWAuvLv_QyFoi9jMsQwVp_IDndXjY-r1bBFS2_YRQJjTIULzMBDETTFPnHInNZOJKDELdz5NvtrS8qIS7YhXJnBu1f8-kdIH2PUnB78jyarXqCKzsKWDdLgGvTMMP-ok5ofkgnptgDAwrD9oopyv8nzShtkWPt1iQxS5Z1fCHj_RB2Pav6XKr-k0-KVhcVTHktX0rSTPoJ8BhYTGlbpdPkjkAF21qV-8UzWxzAThG4mpKEBf_rH-qWP9e1PHz_v3-UW9rCiCX3vdwGD-DTCQFN6CP2v3tKfca_V-M_A6ApXuOQdF8zkkS2ODRJq0AbgzabyYePqxb3RFQzHJ1FxbA6_c16fvv4oT6UQXx0eToaV5W7aOoUjDxui6S2mYiGXrmEgTvnc5zEYFx-hRwyeK19Gb5ZS9iyKhDL9xEC_7-hkh8Q-Za7UWJDGH8qENhT9VIjT_ft2ObCHJpTA89PksE5d2kfrDc2JywzNmYR3g-BuwDx0c7iXhyWyyTapujfSz820Sd0s47RJx6MdM-Y-kmdW1LTbfBQZnS6AIw3ngwqDqIX0q56Vg0PyBlSXwLDcOTRJHp2DvVW7lzSYet9tF33KrtqDP68ZkO2Lv05jZKs_ehKqMBPR25GkMhrHecS3wPHY2Wt8kfN0g_CRyqL3GnF2zxSJ1lGSvsUUKVaU2-fz3spn8-uB4vGHfiI4vAy73l3uln9MkbW3GA1M9CZFQqJHcFTCybUH-NJA1gm5ufXw6tfOEIozYTsBlUJoUYYQcwGYDcRRVwFaLhqDA1EUWiNzJUOt7F_UW8A25XvxJa0OK9cqb9yQmXyHisgwIP3vvjq3fUOjjvfnWgGQ0xDhCy8Rgc-meLyfgDQ5JSID0MCjrI9U5bQNUVlmEZ-9yMZfishA=w600-h250-s-no?authuser=0)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
# MasterPannel
Software used for remote file management using protocols SSH and SFTP. Files are securely transferred, copied, and received with all bits of sensitive information secured and encrypted. Features a LAN IP scanner so you can find your computers more easily on a LAN and a client is added for ease of setup on remote computers. You can also recursively deploy files on separate computers and upload multiple files at once. You can save computer information so you don't have to type in the IP, Username, and Password every time like in the CLI.
## Screenshots

![App Screenshot](https://lh3.googleusercontent.com/Rb8Dyxxqxwd0F-OkkcdW290weItroYZvCOCjYEpM7RSwntlkqnv-msKAkwSkoIvzF-qe1dddem0bXDm-zQya83ghV5YwEOAket9R_cNja1UgkoevI9xKNKcrIHOzSUdzxzYg62zcnVAYlY_P9JNuTSMKkL19AcPoDEVkOmYPTGUew5SEgRiZPUxwqBgH_0__zdFGydfjAiHqd0sz7XPocQ9SEOjdNI-z8tvo0hP2oJ9XuIg-l98Jk9bHVBgtY2uFhPR1_p1QSv1YdduupoBIlljMLQRicUDkb0z30pER5E7pZDJ5YRxZrCvCpTr2yGqR6GH2DGBYr5M9kux12x_YSDnwHQ3E6OljwOn2o_FfRm_-_TSb9hocM6X0euPhycQbbd10x7QZj1sYB4B8fI3NEtnxrzpC3v2TN_hyilpkxR4ol4Mjj9F29MoLr0vFou5FE06oTfB0B5SWIGW8YIQmbEzy7j9p4kQyskYP-M7suiFFhYWFE7NSwsEIOWEFo8LBfzPPY3xphcrROk7HMppv9bzFoYXXZO75TN9jgXhi-Gv_eUutn6eY63PTgZnMlbe0G9gz9w1mmHxg9p_0D4MeiP-yISi-qgLuKXosm04BeivJhKtdRp_cfO0EhatiaTKoxRkaLaaFUrWzbo5RnBhCCk8ammqocw8XkiwXuqoTGOQn0vw6iz_CgaT2sMj5ncbxKcpRqawFV4kwn905unKc6K5WX1BoS_s2LQU178S55CdOhFZtlp4hk8RV66a5-4L33mNbYyRyTMOJzIC535buXWOV15rsbTeWxlWvbTqDj4az-P0MsBz9Pg7-4DG6egsVKWGx-3UYDYj-yjJiabTG0pTzJvFh0tOgbJwkJYzuqiz4tkgrWwWk3YthZfHxeutZqLS_S8Lk9V9i7DVCqH0QNAVZpBkQdh60JjXOyshBThCsYh5P=w799-h499-s-no?authuser=0)

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
