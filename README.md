# Threads Auto Blocker
一個能夠自動封鎖Threads用戶的程式

# 說明
本專案使用了 `metathreads` 和 `threads-api` 兩個套件

表單支援兩種形式
- 本地檔案
    - 隨便哪種檔案形式，一行放一個使用者名稱(個人檔案網址也可以)

- Google Sheet
    - 僅支援公開的連結，將名單放在第一列(僅支援個人檔案網址)

當專案無法運行時，請嘗試刪除 `.session.json` 和 `.token`

> [!WARNING]  
> 使用本專案有**極高的機率**被 Instagram 判定為自動化程式，請自行斟酌

# 前置作業
將 Threads(Instagram)的帳號密碼 和 表單的連結或路徑 放入 `config.json`

```
pip install -U -r requirements.txt
```

執行 `main.py`

# 聲明
本專案只是一個Threads自動化程式的練習，並沒有任何政治立場

# 參考資料
- [Danie1/threads-api](https://github.com/Danie1/threads-api)
- [iSarabjitDhiman/MetaThreads](https://github.com/iSarabjitDhiman/MetaThreads)