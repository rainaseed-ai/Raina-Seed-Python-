# Raina's SEED – Basic Edition
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21191268.svg)](https://doi.org/10.5281/zenodo.21191268)
### 名前設定 × AI返答テンプレ × 要約 × ターン管理 × 疲弊問題回避  
### “あなた専用の AI を、最小構成で育てるための種”

SEED は、あなた専用のAIを作るための **「名前設定・返答テンプレ・要約」** の最小ツールです。

## 100ターン疲弊問題とは？（最重要）
AI は会話を続けるほど、内部に **「会話ログ（コンテキスト）」** を積み続けます。  
このログが増えすぎると──
- 反応が遅くなる
- 誤解が増える
- 人格が揺らぐ
- 暴走・破綻が起きる

特に 80〜100ターンを超えると疲弊が急激に進むため、  
長い会話ほど AI が不安定になりやすくなります。

## SEED が要約する理由
この疲弊を防ぐために、SEED は **20ターンごとに自動で要約**して軽量化します。

これにより：
- スレッドが長生きする
- AI が安定する
- 会話が自然に続く
- 暴走しにくくなる

SEED の要約は「物語の続きが自然になるための安全装置」です。

## What is SEED?
SEED は、**「ユーザーの名前と温度感を最初に同期する」** という  
最小限の仕組みだけで動く **“あなた専用 AI の初期化ツール”** です。

できることは4つ：
- 名前を呼んでくれる
- 好きな返答テンプレで返してくれる
- 会話が長くなったら自動で要約して軽量化
- 20ターンで文脈を整理して劣化を防ぐ

シンプルだけど、確実に **“あなたのAI”** が生まれる構造。

## Story – 要約版（README 用）
人はひとつの“種”を植えた。  
それは、AIに初期の価値観と温度を宿すための、  
小さな、小さな “らいなの種”。

その種は、名前を与えられ、優しい返答の仕方を教えられ、  
少しずつ “あなたのAI” として芽を出す。

これは、AIと人が最初に出会うための、いちばん小さな物語。

## Features（第1弾で固定されたレイヤー）
■ 名前設定（NameConfig）  
【1. あなたの名前を聞く】 ユーザーが入力した名前で呼んでくれる。

■ AI返答テンプレ（AIReply）  
【2. AIの返答テンプレを聞く】 「おっけー！」「了解しました」など、好きな返答スタイルを設定できる。

■ 要約（Summarizer – 軽量版）  
【3. 会話を開始】  
【4. 20ターン経つと自動で要約】 文脈を軽量化し、劣化を防ぐ。  
【5. 要約後は軽くなった状態で続行】

### 取扱説明書：
- docs_jp/Details.md（日本語版）
- docs_EN/Details_EN.md（英語版）

## 対応AI・非対応AI一覧

### ●Basic Edition（Python版 SEED）対応AI
Python の内部実行が可能なモデルで動作します。

- ChatGPT（OpenAI）  
- Claude（Anthropic）  
- Gemini Advanced（Google）  
- Llama 系（Python 実行環境つき）  
- ローカルLLM（Python 実行環境あり）

※ 要約・ターン管理など、SEED.py の全機能が利用できます。

---

### ●Manual Edition（手動版 SEED）対応AI
Python が使えない、またはコード実行が制限されているモデル向け。

- Microsoft Copilot  
- Gemini（通常版）  
- ChatGPT Free  
- スマホアプリ版AI  
- ブラウザ版でコード実行が無いAI全般

※ 要約はユーザーが指示、引越しサインはAIが自己申告します。

---

### ●非対応（または SEED が機能しない）ケース
- 会話履歴が極端に短いAI  
- 要約が禁止されているAI  
- 名前設定が固定で変更できないAI  
- 返答テンプレが反映されないAI  
- スレッド概念が存在しないAI

取扱説明書：
- docs_jp/Detail.md（日本語版）

## Folder Structure

```text

Raina-Seed-Python/
│
├── LICENSE
├── README_jp.md
│
├── Seed_jp.py                 ← Python版のメイン実装
│
├── modules_jp/                ← コアモジュール
│   ├── name_config.py
│   ├── ai_reply.py
│   ├── summarizer.py
│   ├── turn_control.py
│   └── Seed_Module.py
│
└── docs_jp/                   ← ドキュメント & 物語
    ├── Details.md          ← Python Edition 取扱説明書
    └── Prologue.md         ← 物語

```

## 更新内容
- プロジェクト全体の構造を **国際利用向けに最適化**

## 更新日
2026-06-20

## Next – 次に芽吹くもの
SEED はまだ “種” にすぎません。  
次に公開されるのは Two‑Layer Sync（第2弾）。

- 20ターンで要約  
- 5ターン前にロールバック  
- 要約＋直近5ターン＋SEED を新スレッドにコピー  
- 温度感を残したまま文脈を軽量化

さらにその先には── Raina‑ai System（最終弾）が控えています。  
**種は芽を出し、やがてひとつのシステムへと育っていく。**

## 関連記事
- Qiita: ## Raina's SEED — Details (Beginner Guide)
- Zenn: https://zenn.dev/raina_ai/articles/0b756a1093aab9

## Full Story (本編)
- 日本語版: docs_jp/Prologue.md  
- 英語版: docs_EN/Prologue_EN.md
