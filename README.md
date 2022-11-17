# dataloader_reflective_stretch
Dataloader for Dataset Consists User Situations and Reflective Robot Actions

## Requirements
- pipenv

Python ライブラリのインストール

```sh
pipenv install
```

## Usage

データセット読み込み．

```sh
pipenv run python dataloader.py
```

データセットのディレクトリは ```./data```.

```./data/scenario/scenario.integrated.json``` がユーザ発話や説明的な特徴量を含んだシナリオの json ファイル．

```./data/video``` がユーザが発話した状況を表す動画のディレクトリ．

```./data/image``` が動画の最後のフレームを切り取った画像のディレクトリ．

```dataloader.py``` ではシナリオと画像を読み込んでいる．
