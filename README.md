# Koyofes Navi Backend

## Overview

Koyofes Navi は、豊田工業高等専門学校で開催される文化祭「こうよう祭」における待ち時間管理システムです。

## Getting Started

### Prerequisites

#### Poetry

Pythonファイルの依存関係管理はpoetryを使用します。

1. <https://python-poetry.org/docs/#installation>
1. `python -m venv venv`
1. `source venv/bin/activate`
1. `pip install --upgrade pip` (必要であれば)
1. `poetry install`

#### pre-commit (for developers)

commitする前に実行するコマンドを定義するツールです。`.pre-commit-config.yaml` に定義済みなので、それを各自の環境に設定する必要があります。下記手順で行ってください。

1. <https://pre-commit.com/#installation>
1. `pre-commit install`
