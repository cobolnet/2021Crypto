<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

<div align="center">    
 
# Hexa Encrytion v1.1

<!-- [![Paper](http://img.shields.io/badge/paper-arxiv.1001.2234-B31B1B.svg)](https://www.nature.com/articles/nature14539)
[![Conference](http://img.shields.io/badge/NeurIPS-2019-4b44ce.svg)](https://papers.nips.cc/book/advances-in-neural-information-processing-systems-31-2018)
[![Conference](http://img.shields.io/badge/ICLR-2019-4b44ce.svg)](https://papers.nips.cc/book/advances-in-neural-information-processing-systems-31-2018)
[![Conference](http://img.shields.io/badge/AnyConference-year-4b44ce.svg)](https://papers.nips.cc/book/advances-in-neural-information-processing-systems-31-2018)   -->
<!-- 
ARXIV   
[![Paper](http://img.shields.io/badge/arxiv-math.co:1480.1111-B31B1B.svg)](https://www.nature.com/articles/nature14539) -->

<!-- ![CI testing](https://github.com/PyTorchLightning/deep-learning-project-template/workflows/CI%20testing/badge.svg?branch=master&event=push) -->


<!--  
Conference   
-->   
</div>
 
## Description   
스도쿠 퍼즐은 9x9의 크기의 칸을 각 행, 열 그리고 3x3의 박스에 숫자를 1부터 9까지 중복되지 않게 입력하여 완성하는 퍼즐입니다.
이 스도쿠 퍼즐을 16x16 크기로 확장한 헥사 도쿠에서 아이디어를 얻어 암호 알고리즘을 만들었습니다.


## How to run   
먼저, 의존성 패키지를 설치하세요   
```bash
# install numpy and others

python3 -m virtualenv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```   

## Encryption
```bash
python3 encryption.py
```

```bash
 ___  ___  _______      ___    ___ ________                                                     
|\  \|\  \|\  ___ \    |\  \  /  /|\   __  \                                                    
\ \  \\\  \ \   __/|   \ \  \/  / | \  \|\  \                                                   
 \ \   __  \ \  \_|/__  \ \    / / \ \   __  \                                                  
  \ \  \ \  \ \  \_|\ \  /     \/   \ \  \ \  \                                                 
   \ \__\ \__\ \_______\/  /\   \    \ \__\ \__\                                                
    \|__|\|__|\|_______/__/ /\ __\    \|__|\|__|                                                
                       |__|/ \|__|                                                              
                                                                                                
                                                                                                
 _______   ________   ________  ________      ___    ___ ________  ___  ________  ________      
|\  ___ \ |\   ___  \|\   ____\|\   __  \    |\  \  /  /|\   __  \|\  \|\   __  \|\   ___  \    
\ \   __/|\ \  \\ \  \ \  \___|\ \  \|\  \   \ \  \/  / | \  \|\  \ \  \ \  \|\  \ \  \\ \  \   
 \ \  \_|/_\ \  \\ \  \ \  \    \ \   _  _\   \ \    / / \ \   ____\ \  \ \  \\\  \ \  \\ \  \  
  \ \  \_|\ \ \  \\ \  \ \  \____\ \  \\  \|   \/  /  /   \ \  \___|\ \  \ \  \\\  \ \  \\ \  \ 
   \ \_______\ \__\\ \__\ \_______\ \__\\ _\ __/  / /      \ \__\    \ \__\ \_______\ \__\\ \__\
    \|_______|\|__| \|__|\|_______|\|__|\|__|\___/ /        \|__|     \|__|\|_______|\|__| \|__|
                                            \|___|/                                             
Hexa Encryption v1.1                                                                                        
----- 평문을 입력하세요. -----
안녕하세요!!!
----- 키를 입력하세요 -----
This is Key!
----- 암호화를 시작합니다. -----
5c8f6b36c00d567e4734858e4a37592d7da0f020293ba32fb14d71cdd933d693
----- 암호문이 완성되었습니다. -----
소요시간 : 0.8464460372924805초
```

## Decryption
```bash
python3 Decryption.py
```

```bash
 ___  ___  _______      ___    ___ ________                                                    
|\  \|\  \|\  ___ \    |\  \  /  /|\   __  \                                                   
\ \  \\\  \ \   __/|   \ \  \/  / | \  \|\  \                                                  
 \ \   __  \ \  \_|/__  \ \    / / \ \   __  \                                                 
  \ \  \ \  \ \  \_|\ \  /     \/   \ \  \ \  \                                                
   \ \__\ \__\ \_______\/  /\   \    \ \__\ \__\                                               
    \|__|\|__|\|_______/__/ /\ __\    \|__|\|__|                                               
                       |__|/ \|__|                                                             
                                                                                               
                                                                                               
 ________  _______   ________  ________      ___    ___ ________  ___  ________  ________      
|\   ___ \|\  ___ \ |\   ____\|\   __  \    |\  \  /  /|\   __  \|\  \|\   __  \|\   ___  \    
\ \  \_|\ \ \   __/|\ \  \___|\ \  \|\  \   \ \  \/  / | \  \|\  \ \  \ \  \|\  \ \  \\ \  \   
 \ \  \ \\ \ \  \_|/_\ \  \    \ \   _  _\   \ \    / / \ \   ____\ \  \ \  \\\  \ \  \\ \  \  
  \ \  \_\\ \ \  \_|\ \ \  \____\ \  \\  \|   \/  /  /   \ \  \___|\ \  \ \  \\\  \ \  \\ \  \ 
   \ \_______\ \_______\ \_______\ \__\\ _\ __/  / /      \ \__\    \ \__\ \_______\ \__\\ \__\
    \|_______|\|_______|\|_______|\|__|\|__|\___/ /        \|__|     \|__|\|_______|\|__| \|__|
                                           \|___|/                                             
                                                                                               
                                                                                                                                          
Hexa Decryption v1.1                                                                                        
----- 암호문을 입력하세요. -----
5c8f6b36c00d567e4734858e4a37592d7da0f020293ba32fb14d71cdd933d693
----- 키를 입력하세요 -----
This is Key!
----- 복호화를 시작합니다. -----
안녕하세요!!!
----- 평문이 완성되었습니다. -----
소요시간 : 0.8663084506988525초
```

## 개발 환경
<table>
  <tr>
    <td align="center">스택</a></td>
    <td align="center">운영체제</td>
    <td align="center">사용 언어</td>
  </tr>
  <tr>
    <td align="center">Floodnut</a></td>
    <td align="center"><a>Ubuntu 20.04 LTS<br/>MacOS Big Sur</a></td>
   <td align="center"><a>Python 3.8.10</a></td>
  </tr>
  <tr>
    <td align="center">cobolnet</a></td>
    <td align="center"><a>Windows 10<br/>MacOS Big sur</a></td>
   <td align="center"><a>Python 3.9.</a></td>
  </tr>
  <tr>
  <td align="center">nsih</a></td>
  <td align="center"><a>Windows 10</a></td>
 <td align="center"><a>Python 3.9.</a></td>
</tr>
</table>

## 동작 환경
Python 3.8 이상이 설치된 환경


## 알고리즘 설명
추후 추가 예정입니다!


## 버그 제보
버그 제보는 이슈를 통해 부탁드립니다!


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Floodnut"><img src="https://avatars.githubusercontent.com/u/15941204?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Floodnut</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/cobolnet"><img src="https://avatars.githubusercontent.com/u/82963112?v=4?s=100" width="100px;" alt=""/><br /><sub><b>cobolne</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/nsih"><img src="https://avatars.githubusercontent.com/u/81147612?v=4?s=100" width="100px;" alt=""/><br /><sub><b>nsih</b></sub></a><br /></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
